"""Client for the resume.lol MCP endpoint.

The endpoint is plain JSON-RPC over HTTP (streamable-HTTP, so replies arrive as
SSE frames). Talking to it directly rather than through the MCP tool layer means
the pipeline runs the same way from a script, a session, or CI.

A resume there is three documents:
    markdown   the content
    css        styling for the rendered HTML
    meta_css   @page rules - paper size and margins

The API key is read from RLOL_KEY, falling back to the header stored by
`claude mcp add` in ~/.claude.json, so it never has to live in this repo.
"""

from __future__ import annotations

import json
import os
import pathlib
import urllib.request

URL = "https://www.resume.lol/api/mcp"
_CONFIG = pathlib.Path.home() / ".claude.json"


class ResumeLolError(RuntimeError):
    pass


def _key_from_claude_config() -> str | None:
    """Recover the bearer token from the MCP server entry, if one was added."""
    try:
        cfg = json.loads(_CONFIG.read_text(encoding="utf-8"))
    except Exception:
        return None

    def walk(node):
        if isinstance(node, dict):
            servers = node.get("mcpServers")
            if isinstance(servers, dict):
                for name, spec in servers.items():
                    if "resume" not in name.lower() or not isinstance(spec, dict):
                        continue
                    auth = (spec.get("headers") or {}).get("Authorization", "")
                    if auth.lower().startswith("bearer "):
                        return auth[7:].strip()
            for v in node.values():
                found = walk(v)
                if found:
                    return found
        return None

    return walk(cfg)


def api_key() -> str:
    key = os.environ.get("RLOL_KEY") or _key_from_claude_config()
    if not key:
        raise ResumeLolError(
            "No resume.lol key. Set RLOL_KEY, or add the MCP server with:\n"
            "  claude mcp add resumes-lol --transport http "
            "https://www.resume.lol/api/mcp --header \"Authorization: Bearer <key>\"")
    return key


def _rpc(method: str, params: dict | None = None, timeout: int = 90) -> dict:
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": method,
                       "params": params or {}}).encode()
    req = urllib.request.Request(URL, data=body, method="POST", headers={
        "Authorization": f"Bearer {api_key()}",
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        raw = resp.read().decode("utf-8", "replace")

    frames = [ln[5:].strip() for ln in raw.splitlines() if ln.startswith("data:")]
    payload = json.loads(frames[-1]) if frames else json.loads(raw)
    if "error" in payload:
        raise ResumeLolError(json.dumps(payload["error"], indent=2))
    return payload.get("result", {})


def call(tool: str, **arguments):
    """Invoke a tool and return its parsed payload.

    Results come back as MCP content blocks; the useful ones are JSON encoded
    inside a text block, so decode that when possible and hand back the raw
    string when it is genuinely prose (the authoring guide, the HTML export).
    """
    result = _rpc("tools/call", {"name": tool, "arguments": arguments})
    blocks = [b.get("text", "") for b in result.get("content", [])
              if b.get("type") == "text"]
    text = "\n".join(blocks)
    if result.get("isError"):
        raise ResumeLolError(text or json.dumps(result, indent=2))
    try:
        return json.loads(text)
    except (json.JSONDecodeError, ValueError):
        return text


def list_tools() -> list[str]:
    return [t["name"] for t in _rpc("tools/list").get("tools", [])]


def list_resumes():
    return call("list_resumes")


def get_resume(resume_id: str):
    return call("get_resume", resume_id=resume_id)


def create_resume(name: str, markdown: str = "", css: str = "", meta_css: str = ""):
    return call("create_resume", name=name, markdown=markdown, css=css,
                meta_css=meta_css)


def update_resume(resume_id: str, *, markdown=None, css=None, meta_css=None,
                  expected_updated_at=None):
    args = {"resume_id": resume_id}
    for k, v in (("markdown", markdown), ("css", css), ("meta_css", meta_css),
                 ("expected_updated_at", expected_updated_at)):
        if v is not None:
            args[k] = v
    return call("update_resume", **args)


def get_resume_html(resume_id: str) -> str:
    out = call("get_resume_html", resume_id=resume_id)
    if isinstance(out, dict):
        for k in ("html", "content", "body"):
            if k in out:
                return out[k]
        return json.dumps(out)
    return out


if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "tools":
        print("\n".join(list_tools()))
    else:
        print(json.dumps(list_resumes(), indent=2))

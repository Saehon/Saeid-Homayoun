# OpenCloud bridge for GPT/Codex and Claude

This repository uses OpenCloud as a shared execution layer for supported AI agents.

## Supported paths

- ChatGPT Work / supported no-terminal clients: hosted MCP endpoint `https://mcp.opencloud.ai`
- Claude.ai / Claude Desktop / Claude mobile: hosted MCP endpoint `https://mcp.opencloud.ai`
- Codex with terminal access: OpenCloud CLI v3.10.3
- Claude Code with terminal access: OpenCloud CLI v3.10.3

## Security

Do not commit OpenCloud tokens, OAuth credentials, session files, API keys, or connection packs.
OpenCloud credentials belong in the operating-system credential store. The local `.opencloud/` state is ignored.

## Local setup

Install the checksum-verified pinned CLI from the official OpenCloud documentation, then verify:

```bash
curl -fsSL https://docs.opencloud.ai/install.sh | bash
opencloud --cli-version
opencloud auth status
opencloud login
opencloud doctor
```

Expected CLI: `3.10.3`.

For Codex plugin marketplace support:

```bash
codex plugin marketplace add opencloud-ai/agent-plugins
```

For Claude plugin marketplace support:

```bash
claude plugin marketplace add opencloud-ai/agent-plugins
claude plugin install opencloud@opencloud-platform
claude plugin enable opencloud@opencloud-platform
```

Human OAuth/consent remains required by OpenCloud and the client.

Official docs: https://docs.opencloud.ai/getting-started/mcp

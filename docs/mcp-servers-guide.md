# MCP Servers Comprehensive Guide

This guide contains our research on the best MCP servers for Claude Desktop and Claude Code integration.

## Overview

Model Context Protocol (MCP) servers extend Claude's capabilities by providing access to external resources and services. However, both Claude Desktop and Claude Code perform better when not overloaded with too many MCP servers.

## Top MCP Servers by Category

### 1. Localhost & Development Access

#### MCP-Proxy ⭐️ (Essential)
**Purpose**: Bridge Claude's security restrictions for localhost access

```json
{
  "mcpServers": {
    "local-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:3000/sse"],
      "env": {
        "API_ACCESS_TOKEN": "${LOCAL_API_TOKEN}"
      }
    }
  }
}
```

**Key Features**:
- Converts between stdio and SSE protocols
- Enables access to any localhost port
- Essential for local development server access
- Minimal performance overhead

#### Puppeteer MCP Server
**Purpose**: Browser automation for localhost testing

**Features**:
- Navigate to localhost URLs
- Execute JavaScript in local contexts
- Capture screenshots
- Requires `ALLOW_DANGEROUS: "true"` flag

### 2. File System Access

#### Desktop Commander ⭐️
**Purpose**: Advanced file system and terminal control

**Features**:
- Terminal command execution
- Surgical code editing (edit_block format)
- Process management
- Cross-platform support
- Security features (command blacklists)
- Audit logging

#### Official Filesystem Server
**Purpose**: Basic file operations with security

**Features**:
- Secure directory sandboxing
- File search capabilities
- Docker containerization support
- Most stable option

### 3. Database Connectivity

#### MCP Alchemy ⭐️
**Purpose**: Universal database access via SQLAlchemy

```json
{
  "database": {
    "command": "uvx",
    "args": ["mcp-alchemy"],
    "env": {
      "DB_URL": "postgresql://user:pass@localhost/db"
    }
  }
}
```

**Supported Databases**:
- PostgreSQL
- MySQL/MariaDB
- SQLite
- SQL Server
- Oracle
- Any SQLAlchemy-compatible DB

**Features**:
- Smart result truncation
- Connection pooling
- Claude Desktop artifacts integration
- SQL injection prevention

### 4. API Integration

#### Apollo MCP Server
**Purpose**: GraphQL API integration

**Features**:
- Dynamic tool generation from GraphQL ops
- Query optimization (60% reduction in API calls)
- Declarative policy enforcement
- Multi-API orchestration

#### Any OpenAPI Server
**Purpose**: REST API integration

**Features**:
- Dynamic API interaction
- Semantic endpoint search
- Complex authentication support
- Reduced context bloat for LLMs

### 5. Development Tools

#### GitHub MCP Server
**Purpose**: Repository and workflow management

**Features**:
- Repository management
- Automated issue triage
- Pull request reviews
- GitHub Copilot integration
- Significant performance improvements in Go version

### 6. Communication & Productivity

#### Slack MCP Server
**Purpose**: Team communication integration

#### Email MCP Servers
**Purpose**: Email management and automation

#### Linear/Asana MCP
**Purpose**: Project management integration

## Performance Considerations

### Optimal Server Count
- No hard limits, but performance degrades with overload
- Focus on essential servers for your workflow
- Monitor response times and memory usage
- Remove underutilized servers

### Resource Usage
- Most servers: <100MB RAM
- Minimal CPU except during operations
- Connection pooling improves database performance
- Caching reduces repeated operations

## Security Best Practices

### Container Isolation
```yaml
services:
  mcp-server:
    image: mcp-server:latest
    security_opt:
      - apparmor:docker-default
    cap_drop:
      - ALL
    read_only: true
```

### Authentication
- OAuth 2.1 with PKCE for external services
- Token rotation
- Least privilege access
- Audit logging for all operations

## Installation Requirements

### Prerequisites
- Node.js 18+ (JavaScript servers)
- Python 3.8+ with UV (Python servers)
- Database drivers as needed
- Docker (optional but recommended)

### Common Issues

#### macOS: "spawn npx ENOENT"
```bash
# Add to PATH
export PATH="/opt/homebrew/bin:/usr/local/bin:$PATH"
```

#### WSL Configuration
```json
{
  "command": "wsl.exe",
  "args": ["-e", "/usr/bin/node", "/path/to/server"]
}
```

## Recommendations by Use Case

### For Claude Code
- Start with NO MCP servers (test native tools first)
- Add only for genuine gaps:
  - MCP Alchemy (if using databases)
  - Container Sandbox (for secure execution)
  - Custom project-specific servers

### For Claude Desktop
- MCP-Proxy (essential for localhost)
- Filesystem Server (documentation access)
- Communication tools (Slack/Email)
- Project management (Linear/Asana)
- Document management (Google Drive)

## Future Developments

### Emerging Features
- Streaming support for real-time communication
- Stateless connections for better scalability
- Proactive server behavior
- Enhanced security models

### Community Growth
- New servers weekly
- Increasing enterprise adoption
- Standardization efforts
- "USB-C for AI applications"

---

*Based on research conducted June 2025*
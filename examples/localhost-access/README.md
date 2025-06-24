# Localhost Access Examples

This directory contains examples for accessing localhost services with Claude Desktop using MCP-Proxy.

## Prerequisites

1. MCP-Proxy installed globally:
```bash
npm install -g mcp-proxy
```

2. Claude Desktop configured with MCP-Proxy

## Example 1: Accessing Local Documentation

### Setup

1. Start your documentation server:
```bash
# Example with Docusaurus
cd my-docs
npm run start  # Usually runs on localhost:3000

# Example with MkDocs
mkdocs serve  # Usually runs on localhost:8000

# Example with VitePress
npm run docs:dev  # Usually runs on localhost:5173
```

2. Configure Claude Desktop:
```json
{
  "mcpServers": {
    "docs-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:3000/sse"],
      "env": {
        "API_ACCESS_TOKEN": "docs-access-token"
      }
    }
  }
}
```

3. Test in Claude Desktop:
```
Claude: Can you fetch and analyze my documentation at localhost:3000?
```

## Example 2: Local API Development

### Backend API Access

1. Start your API server:
```javascript
// express-server.js
const express = require('express');
const app = express();

app.get('/api/status', (req, res) => {
  res.json({ status: 'running', timestamp: new Date() });
});

app.listen(8080, () => {
  console.log('API running on localhost:8080');
});
```

2. Configure proxy for API:
```json
{
  "mcpServers": {
    "api-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:8080/sse"],
      "env": {
        "API_ACCESS_TOKEN": "api-dev-token"
      }
    }
  }
}
```

## Example 3: Full-Stack Development

### Frontend + Backend Setup

```javascript
// Full configuration for full-stack development
{
  "mcpServers": {
    "frontend-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:3000/sse"],
      "env": {
        "API_ACCESS_TOKEN": "frontend-token"
      }
    },
    "backend-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:8080/sse"],
      "env": {
        "API_ACCESS_TOKEN": "backend-token"
      }
    },
    "database-ui-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:5432/sse"],
      "env": {
        "API_ACCESS_TOKEN": "db-ui-token"
      }
    }
  }
}
```

## Example 4: Security Considerations

### Secure Token Generation

```bash
# Generate secure tokens for each service
openssl rand -hex 32 > .frontend-token
openssl rand -hex 32 > .backend-token
openssl rand -hex 32 > .database-token
```

### Environment Configuration

```bash
# .env.local
FRONTEND_TOKEN=$(cat .frontend-token)
BACKEND_TOKEN=$(cat .backend-token)
DATABASE_TOKEN=$(cat .database-token)

# Restrict access by IP
ALLOWED_IPS=127.0.0.1,::1
```

## Troubleshooting

### Common Issues

1. **"Connection refused" error**
   - Verify your service is running on the expected port
   - Check firewall settings
   - Ensure MCP-Proxy is running

2. **"Unauthorized" error**
   - Verify API_ACCESS_TOKEN matches between config and server
   - Check token encoding/formatting

3. **"Timeout" error**
   - Increase timeout in MCP-Proxy configuration
   - Check if service is responding slowly
   - Verify network connectivity

### Debug Commands

```bash
# Test MCP-Proxy directly
curl -H "Authorization: Bearer your-token" http://localhost:3000

# Check if service is listening
lsof -i :3000  # macOS/Linux
netstat -an | findstr :3000  # Windows

# Test with Claude Code
claude -p "fetch http://localhost:3000/api/status" --allowedTools "WebFetch"
```

## Best Practices

1. **Use different tokens for each service**
2. **Never commit tokens to version control**
3. **Rotate tokens regularly**
4. **Monitor access logs**
5. **Use HTTPS in production**
6. **Implement rate limiting**
7. **Validate all inputs**

---

*For more examples, see the main documentation.*
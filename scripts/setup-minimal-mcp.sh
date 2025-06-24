#!/bin/bash

# Setup Minimal MCP Configuration
# This script sets up the essential MCP servers for Claude Desktop and Claude Code

set -e

echo "🚀 Setting up minimal MCP configuration..."

# Check prerequisites
command -v node >/dev/null 2>&1 || { echo "❌ Node.js is required but not installed. Aborting." >&2; exit 1; }
command -v python3 >/dev/null 2>&1 || { echo "❌ Python 3 is required but not installed. Aborting." >&2; exit 1; }

# Create config directories
echo "📁 Creating configuration directories..."
mkdir -p ~/.claude
mkdir -p ~/.claude/commands
mkdir -p .claude/commands

# Install MCP-Proxy for localhost access
echo "📦 Installing MCP-Proxy..."
npm install -g mcp-proxy

# Create minimal Claude Desktop config
echo "⚙️ Creating Claude Desktop configuration..."
cat > ~/.claude/claude_desktop_config.json << 'EOF'
{
  "mcpServers": {
    "local-proxy": {
      "command": "npx",
      "args": ["-y", "mcp-proxy", "http://localhost:3000/sse"],
      "env": {
        "API_ACCESS_TOKEN": "${LOCAL_API_TOKEN}"
      }
    },
    "filesystem": {
      "command": "npx",
      "args": [
        "-y",
        "@modelcontextprotocol/server-filesystem",
        "${HOME}/Documents"
      ]
    }
  }
}
EOF

# Create minimal Claude Code project config
echo "⚙️ Creating Claude Code project configuration..."
cat > .mcp.json << 'EOF'
{
  "mcpServers": {}
}
EOF

# Create example custom command
echo "📝 Creating example custom command..."
cat > .claude/commands/quick-analysis.md << 'EOF'
# Quick Codebase Analysis

Analyze the current codebase:
1. Map the project structure
2. Identify key components
3. List main dependencies
4. Suggest improvements

Do NOT make any changes, just analyze and report.
EOF

# Create environment template
echo "🔐 Creating environment template..."
cat > .env.example << 'EOF'
# Claude Configuration
ANTHROPIC_API_KEY=your_anthropic_api_key_here
LOCAL_API_TOKEN=your_local_api_token_here

# Optional: Database connections
# DATABASE_URL=postgresql://user:pass@localhost/dbname

# Optional: External services
# GITHUB_TOKEN=your_github_token_here
# SLACK_TOKEN=your_slack_token_here
EOF

# Test Claude Code installation
echo "\n✅ Testing Claude Code..."
if command -v claude >/dev/null 2>&1; then
    echo "✓ Claude Code is installed"
    claude --version
else
    echo "⚠️ Claude Code not found. Please install it from the Anthropic website."
fi

# Final instructions
echo "\n🎉 Minimal MCP setup complete!"
echo "\nNext steps:"
echo "1. Copy .env.example to .env and add your API keys"
echo "2. Start your local development server on port 3000"
echo "3. Test localhost access with: claude -p \"fetch http://localhost:3000\""
echo "4. Customize .claude/commands/ for your workflow"
echo "\nFor Claude Desktop, the config is at: ~/.claude/claude_desktop_config.json"
echo "For Claude Code project config: .mcp.json"

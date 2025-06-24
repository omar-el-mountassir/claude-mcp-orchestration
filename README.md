# 🤖 Claude MCP Orchestration

> Orchestrating Claude Desktop & Claude Code with MCP servers - Programmable workflows, custom commands, and integration patterns

## 🎯 Vision

Transform Claude Desktop and Claude Code into a unified, programmable development environment that leverages the strengths of each tool while avoiding MCP server overload.

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/omar-el-mountassir/claude-mcp-orchestration.git
cd claude-mcp-orchestration
```

### 2. Install Prerequisites
- **Claude Desktop** (latest version)
- **Claude Code** (research preview)
- **Node.js 18+**
- **Python 3.8+** with UV package manager
- **Docker Desktop** (optional, for containerized MCP servers)

### 3. Set Up Your First Workflow
```bash
# Copy example configurations
cp config/claude-desktop-config.example.json ~/.claude/claude_desktop_config.json
cp config/.env.example .env

# Install the minimal MCP setup
./scripts/setup-minimal-mcp.sh
```

## 📚 Repository Structure

```
claude-mcp-orchestration/
├── README.md                 # You are here
├── ROADMAP.md               # Strategic implementation roadmap
├── docs/                    # Research and documentation
│   ├── mcp-servers-guide.md   # Comprehensive MCP server analysis
│   ├── claude-code-capabilities.md
│   ├── integration-patterns.md
│   └── performance-optimization.md
├── workflows/               # Programmable workflow examples
│   ├── feature-development/
│   ├── code-review/
│   ├── documentation/
│   └── project-planning/
├── commands/                # Custom Claude Code commands
│   ├── .claude/commands/    # Project-specific commands
│   └── global/              # User-wide commands
├── scripts/                 # Automation and integration scripts
│   ├── setup-minimal-mcp.sh
│   ├── claude-orchestrator.py
│   └── workflow-runner.js
├── config/                  # Configuration templates
│   ├── claude-desktop-config.example.json
│   ├── mcp-servers/
│   └── .env.example
└── examples/               # Working examples
    ├── localhost-access/
    ├── database-workflows/
    └── full-stack-development/
```

## 🔧 Core Concepts

### 1. Strategic MCP Distribution

**Claude Code** (Development Engine):
- Leverages built-in tools (Task, Bash, WebFetch, etc.)
- Minimal MCP servers only for genuine gaps
- Programmable via CLI for automation

**Claude Desktop** (Knowledge Hub):
- Documentation and research
- Communication and project management
- Strategic planning and reporting

### 2. Programmable Workflows

```bash
# Example: Complete feature development
claude -p "Read issue #123, plan implementation, write tests, code, document" \
  --allowedTools "Task,Edit,Bash,Write,Read"
```

### 3. Custom Commands

Create reusable workflows in `.claude/commands/`:
```markdown
# .claude/commands/feature-pipeline.md
Implement feature from issue #$ARGUMENTS:
1. Analyze requirements
2. Create implementation plan
3. Write tests first (TDD)
4. Implement solution
5. Update documentation
6. Create PR with full context
```

## 🎯 Use Cases

### 1. Localhost Documentation Access
- Access your workflow documentation at `localhost:3000`
- Use MCP-Proxy for secure localhost connectivity
- See `examples/localhost-access/`

### 2. Full-Stack Development
- Coordinated frontend/backend development
- Automated testing and deployment
- See `workflows/full-stack-development/`

### 3. Team Collaboration
- Automated PR reviews
- Documentation updates
- Project status reporting
- See `workflows/team-collaboration/`

## 📊 Performance Guidelines

- **Quality over Quantity**: Focus on essential MCP servers
- **Monitor Performance**: Use included monitoring scripts
- **Iterate and Optimize**: Start minimal, add as needed

## 🤝 Contributing

This is a living repository! Contributions welcome:

1. Fork the repository
2. Create your feature branch
3. Add your workflows/commands/examples
4. Submit a PR with clear description

## 📖 Documentation

- [Complete MCP Servers Guide](docs/mcp-servers-guide.md)
- [Claude Code Capabilities Deep Dive](docs/claude-code-capabilities.md)
- [Integration Patterns](docs/integration-patterns.md)
- [Performance Optimization](docs/performance-optimization.md)

## 🚧 Roadmap

See [ROADMAP.md](ROADMAP.md) for the complete implementation plan.

## 📄 License

MIT License - See [LICENSE](LICENSE) for details.

## 🙏 Acknowledgments

- Anthropic team for Claude Desktop and Claude Code
- MCP server developers
- Community contributors

---

**Questions?** Open an issue or reach out!

**Found this helpful?** Give it a ⭐!
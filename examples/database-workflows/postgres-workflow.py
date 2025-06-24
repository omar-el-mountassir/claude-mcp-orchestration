#!/usr/bin/env python3
"""
PostgreSQL Workflow Example
Demonstrates database operations with Claude Code and MCP Alchemy
"""

import os
import subprocess
import json
from datetime import datetime

# Database configuration
DB_URL = os.getenv('DATABASE_URL', 'postgresql://localhost/dev_db')

def setup_mcp_alchemy():
    """
    Configure MCP Alchemy for PostgreSQL access
    """
    config = {
        "mcpServers": {
            "postgres-dev": {
                "command": "uvx",
                "args": ["mcp-alchemy"],
                "env": {
                    "DB_URL": DB_URL
                }
            }
        }
    }
    
    # Save to project MCP config
    with open('.mcp.json', 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ MCP Alchemy configured for: {DB_URL}")

def run_database_workflow():
    """
    Execute a complete database workflow
    """
    
    # Workflow 1: Schema Analysis
    print("\n📊 Analyzing Database Schema...")
    subprocess.run([
        "claude", "-p",
        "Analyze the database schema and create a visual diagram of relationships. "
        "List all tables, their columns, data types, and foreign key relationships.",
        "--allowedTools", "Task,Write"
    ])
    
    # Workflow 2: Performance Analysis
    print("\n⚡ Running Performance Analysis...")
    subprocess.run([
        "claude", "-p",
        "think hard about database performance: "
        "1. Identify missing indexes, "
        "2. Find slow queries, "
        "3. Suggest optimization strategies, "
        "4. Create index recommendations",
        "--allowedTools", "Write"
    ])
    
    # Workflow 3: Data Validation
    print("\n✓ Validating Data Integrity...")
    subprocess.run([
        "claude", "-p",
        "Check data integrity across all tables: "
        "1. Find orphaned records, "
        "2. Validate foreign key constraints, "
        "3. Check for duplicate data, "
        "4. Identify data anomalies",
        "--allowedTools", "Write"
    ])
    
    # Workflow 4: Migration Script
    print("\n🔄 Generating Migration Scripts...")
    subprocess.run([
        "claude", "-p",
        "Create a migration script to: "
        "1. Add missing indexes identified earlier, "
        "2. Add data validation constraints, "
        "3. Create a rollback script, "
        "4. Include safety checks",
        "--allowedTools", "Write"
    ])

def run_specific_query(query: str):
    """
    Run a specific database query through Claude
    """
    subprocess.run([
        "claude", "-p",
        f"Execute this SQL query safely and format the results: {query}",
        "--allowedTools", "Read"
    ])

if __name__ == "__main__":
    print("🐘 PostgreSQL Workflow Example")
    print("=" * 40)
    
    # Setup MCP Alchemy
    setup_mcp_alchemy()
    
    # Run the workflow
    run_database_workflow()
    
    # Example: Run a specific query
    # run_specific_query("SELECT COUNT(*) FROM users WHERE created_at > NOW() - INTERVAL '7 days'")
    
    print("\n✅ Workflow completed!")
    print(f"\nGenerated files:")
    print("- schema-diagram.md")
    print("- performance-analysis.md")
    print("- data-validation-report.md")
    print("- migration-scripts.sql")
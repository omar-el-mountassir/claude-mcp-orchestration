# Feature Development Workflows

Automated workflows for complete feature development cycles using Claude Code and Claude Desktop.

## Overview

These workflows demonstrate how to leverage Claude's capabilities for end-to-end feature development, from planning to deployment.

## Workflow 1: TDD Feature Development

### Description
Test-Driven Development workflow that ensures quality through test-first implementation.

### Script: `tdd-feature.py`

```python
#!/usr/bin/env python3
"""
TDD Feature Development Workflow
Develops features using Test-Driven Development with Claude Code
"""

import subprocess
import json
import sys
from datetime import datetime

def log(message):
    print(f"[{datetime.now().strftime('%H:%M:%S')}] {message}")

def run_claude_code(prompt, tools=None, think_level="think"):
    """Execute Claude Code with specified parameters"""
    cmd = ["claude", "-p", f"{think_level} {prompt}"]
    
    if tools:
        cmd.extend(["--allowedTools"] + tools)
    
    log(f"Running: {' '.join(cmd[:3])}...")
    result = subprocess.run(cmd, capture_output=True, text=True)
    
    if result.returncode != 0:
        log(f"Error: {result.stderr}")
        return None
    
    return result.stdout

def tdd_workflow(issue_number):
    """Execute TDD workflow for a GitHub issue"""
    
    # Step 1: Analyze the issue
    log("Step 1: Analyzing issue...")
    analysis = run_claude_code(
        f"Read GitHub issue #{issue_number} and create a detailed analysis. "
        "Do NOT write any code yet. Focus on understanding requirements.",
        tools=["Bash", "Read"],
        think_level="think hard"
    )
    
    if not analysis:
        return False
    
    # Step 2: Write tests first
    log("Step 2: Writing tests...")
    tests = run_claude_code(
        f"Based on the analysis, write comprehensive tests for issue #{issue_number}. "
        "Write ONLY tests, no implementation. Ensure tests fail initially.",
        tools=["Write", "Edit"],
        think_level="think"
    )
    
    # Step 3: Verify tests fail
    log("Step 3: Verifying tests fail...")
    verify = run_claude_code(
        "Run the tests and confirm they fail. Do NOT implement anything yet.",
        tools=["Bash", "Read"]
    )
    
    # Step 4: Implement feature
    log("Step 4: Implementing feature...")
    implementation = run_claude_code(
        "Now implement the feature to make all tests pass. "
        "Use ultrathink to ensure the best implementation.",
        tools=["Edit", "Write", "Read", "Bash"],
        think_level="ultrathink"
    )
    
    # Step 5: Verify tests pass
    log("Step 5: Verifying tests pass...")
    final_verify = run_claude_code(
        "Run all tests and ensure they pass. Fix any remaining issues.",
        tools=["Bash", "Edit", "Read"]
    )
    
    # Step 6: Create PR
    log("Step 6: Creating pull request...")
    pr = run_claude_code(
        f"Create a pull request for issue #{issue_number} with: "
        "1. Descriptive title, 2. Summary of changes, "
        "3. Test results, 4. Closes #{issue_number}",
        tools=["Bash", "Write"]
    )
    
    log("TDD workflow completed!")
    return True

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./tdd-feature.py <issue_number>")
        sys.exit(1)
    
    issue_number = sys.argv[1]
    success = tdd_workflow(issue_number)
    
    sys.exit(0 if success else 1)
```

### Usage

```bash
# Make executable
chmod +x workflows/feature-development/tdd-feature.py

# Run for issue #123
./workflows/feature-development/tdd-feature.py 123
```

## Workflow 2: Full-Stack Feature

### Description
Coordinated frontend and backend development with Claude Desktop for planning and Claude Code for implementation.

### Script: `full-stack-feature.js`

```javascript
#!/usr/bin/env node

/**
 * Full-Stack Feature Development
 * Coordinates frontend and backend development
 */

const { spawn } = require('child_process');
const fs = require('fs').promises;
const path = require('path');

async function runCommand(command, args = []) {
    return new Promise((resolve, reject) => {
        const proc = spawn(command, args);
        let output = '';
        let error = '';
        
        proc.stdout.on('data', (data) => {
            output += data.toString();
            process.stdout.write(data);
        });
        
        proc.stderr.on('data', (data) => {
            error += data.toString();
            process.stderr.write(data);
        });
        
        proc.on('close', (code) => {
            if (code === 0) {
                resolve(output);
            } else {
                reject(new Error(`Command failed: ${error}`));
            }
        });
    });
}

async function claudeCode(prompt, tools = [], thinkLevel = 'think') {
    const args = ['-p', `${thinkLevel} ${prompt}`];
    
    if (tools.length > 0) {
        args.push('--allowedTools', ...tools);
    }
    
    return runCommand('claude', args);
}

async function fullStackWorkflow(featureName) {
    console.log(`🚀 Starting full-stack development for: ${featureName}`);
    
    try {
        // Phase 1: Architecture Planning
        console.log('\n📋 Phase 1: Architecture Planning');
        await claudeCode(
            `Plan the architecture for feature: ${featureName}. ` +
            'Consider: 1. Frontend components needed, ' +
            '2. Backend API endpoints, 3. Database schema changes, ' +
            '4. Integration points. Create a detailed plan.',
            ['Write'],
            'think hard'
        );
        
        // Phase 2: Parallel Development using Task
        console.log('\n🔧 Phase 2: Parallel Development');
        await claudeCode(
            `Use Task to spawn 3 parallel agents for ${featureName}: ` +
            '1. Frontend Agent: Create React components and UI, ' +
            '2. Backend Agent: Implement API endpoints, ' +
            '3. Database Agent: Set up schema and migrations. ' +
            'Coordinate their work to ensure compatibility.',
            ['Task', 'Write', 'Edit', 'Bash'],
            'ultrathink'
        );
        
        // Phase 3: Integration
        console.log('\n🔗 Phase 3: Integration');
        await claudeCode(
            'Integrate the frontend with backend: ' +
            '1. Connect API endpoints, 2. Handle error states, ' +
            '3. Add loading indicators, 4. Test data flow',
            ['Edit', 'Read', 'Bash']
        );
        
        // Phase 4: Testing
        console.log('\n✅ Phase 4: Comprehensive Testing');
        await claudeCode(
            'Run comprehensive tests: ' +
            '1. Unit tests for components, 2. API integration tests, ' +
            '3. End-to-end tests, 4. Fix any issues found',
            ['Bash', 'Edit', 'Read']
        );
        
        // Phase 5: Documentation
        console.log('\n📚 Phase 5: Documentation');
        await claudeCode(
            'Create comprehensive documentation: ' +
            '1. API documentation, 2. Component documentation, ' +
            '3. User guide, 4. Update README',
            ['Write', 'Edit']
        );
        
        console.log('\n✨ Full-stack feature development completed!');
        
    } catch (error) {
        console.error('\n❌ Error:', error.message);
        process.exit(1);
    }
}

// Main execution
const featureName = process.argv[2];

if (!featureName) {
    console.error('Usage: ./full-stack-feature.js "<feature-name>"');
    process.exit(1);
}

fullStackWorkflow(featureName);
```

## Workflow 3: Microservices Feature

### Description
Develop features across multiple microservices with coordinated changes.

### Command: `.claude/commands/microservice-feature.md`

```markdown
# Microservices Feature Development

Develop feature across microservices: $ARGUMENTS

## Phase 1: Service Discovery
Use Task to spawn agents for each affected service:
1. Identify all services that need changes
2. Analyze dependencies between services
3. Create a dependency graph
4. Plan the implementation order

## Phase 2: Contract Definition
1. Define API contracts between services
2. Create shared data models
3. Document communication protocols
4. Generate OpenAPI specifications

## Phase 3: Parallel Implementation
Use Task to implement changes in each service:
- Each agent handles one service
- Maintain API compatibility
- Implement with feature flags
- Write service-specific tests

## Phase 4: Integration Testing
1. Start all services locally
2. Test service-to-service communication
3. Verify data consistency
4. Test failure scenarios

## Phase 5: Deployment Strategy
1. Create deployment plan
2. Update CI/CD pipelines
3. Plan rollback procedures
4. Document deployment order

Use ultrathink for critical architectural decisions.
```

## Best Practices

### 1. Always Start with Planning
- Use `think hard` or `ultrathink` for architecture
- Prevent premature implementation
- Document decisions

### 2. Leverage Parallel Execution
- Use Task tool for independent work
- Coordinate results effectively
- Maintain consistency

### 3. Iterative Development
- Small, verifiable steps
- Continuous testing
- Regular commits

### 4. Error Handling
- Build in retry logic
- Graceful degradation
- Clear error messages

---

*More workflows coming soon!*
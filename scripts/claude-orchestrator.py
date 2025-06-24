#!/usr/bin/env python3
"""
Claude Orchestrator
Coordinates workflows between Claude Desktop and Claude Code
"""

import subprocess
import json
import os
import sys
import time
from datetime import datetime
from typing import Optional, List, Dict, Any
import asyncio
from enum import Enum

class ClaudeTool(Enum):
    """Available Claude tools"""
    TASK = "Task"
    BASH = "Bash"
    EDIT = "Edit"
    WRITE = "Write"
    READ = "Read"
    WEBFETCH = "WebFetch"
    WEBSEARCH = "WebSearch"
    BATCH = "Batch"
    GLOB = "Glob"
    GREP = "Grep"
    LS = "LS"

class ThinkLevel(Enum):
    """Claude thinking levels"""
    NORMAL = ""
    THINK = "think"
    THINK_HARD = "think hard"
    THINK_HARDER = "think harder"
    ULTRATHINK = "ultrathink"
    MEGATHINK = "megathink"

class ClaudeOrchestrator:
    """Orchestrates workflows between Claude Desktop and Claude Code"""
    
    def __init__(self, debug: bool = False):
        self.debug = debug
        self.workflow_history = []
        
    def log(self, message: str, level: str = "INFO"):
        """Log messages with timestamp"""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"[{timestamp}] [{level}] {message}")
        
    def run_claude_code(
        self,
        prompt: str,
        tools: Optional[List[ClaudeTool]] = None,
        think_level: ThinkLevel = ThinkLevel.NORMAL,
        timeout: Optional[int] = None
    ) -> Optional[str]:
        """Execute Claude Code with specified parameters"""
        
        # Build command
        cmd = ["claude"]
        
        # Add thinking level to prompt if specified
        if think_level != ThinkLevel.NORMAL:
            prompt = f"{think_level.value} {prompt}"
        
        cmd.extend(["-p", prompt])
        
        # Add allowed tools
        if tools:
            tool_names = [tool.value for tool in tools]
            cmd.extend(["--allowedTools"] + tool_names)
        
        # Log execution
        self.log(f"Running Claude Code: {' '.join(cmd[:3])}...")
        if self.debug:
            self.log(f"Full command: {' '.join(cmd)}", "DEBUG")
        
        try:
            # Execute command
            result = subprocess.run(
                cmd,
                capture_output=True,
                text=True,
                timeout=timeout
            )
            
            if result.returncode != 0:
                self.log(f"Error: {result.stderr}", "ERROR")
                return None
            
            # Record in history
            self.workflow_history.append({
                "timestamp": datetime.now().isoformat(),
                "type": "claude_code",
                "prompt": prompt,
                "tools": [tool.value for tool in tools] if tools else [],
                "think_level": think_level.value,
                "success": True
            })
            
            return result.stdout
            
        except subprocess.TimeoutExpired:
            self.log("Command timed out", "ERROR")
            return None
        except Exception as e:
            self.log(f"Exception: {str(e)}", "ERROR")
            return None
    
    async def run_parallel_tasks(
        self,
        tasks: List[Dict[str, Any]]
    ) -> List[Optional[str]]:
        """Run multiple Claude Code tasks in parallel"""
        
        async def run_task(task):
            return await asyncio.to_thread(
                self.run_claude_code,
                task["prompt"],
                task.get("tools"),
                task.get("think_level", ThinkLevel.NORMAL),
                task.get("timeout")
            )
        
        self.log(f"Running {len(tasks)} tasks in parallel...")
        results = await asyncio.gather(*[run_task(task) for task in tasks])
        
        return results
    
    def create_workflow(
        self,
        name: str,
        description: str,
        steps: List[Dict[str, Any]]
    ) -> Dict[str, Any]:
        """Create a reusable workflow definition"""
        
        workflow = {
            "name": name,
            "description": description,
            "created": datetime.now().isoformat(),
            "steps": steps
        }
        
        # Save workflow
        workflow_file = f"workflows/{name.lower().replace(' ', '-')}.json"
        os.makedirs("workflows", exist_ok=True)
        
        with open(workflow_file, 'w') as f:
            json.dump(workflow, f, indent=2)
        
        self.log(f"Created workflow: {name}")
        return workflow
    
    def execute_workflow(self, workflow: Dict[str, Any]) -> bool:
        """Execute a workflow definition"""
        
        self.log(f"Executing workflow: {workflow['name']}")
        
        for i, step in enumerate(workflow["steps"]):
            self.log(f"Step {i+1}/{len(workflow['steps'])}: {step.get('name', 'Unnamed')}")
            
            # Check step type
            step_type = step.get("type", "claude_code")
            
            if step_type == "claude_code":
                result = self.run_claude_code(
                    step["prompt"],
                    [ClaudeTool(tool) for tool in step.get("tools", [])],
                    ThinkLevel(step.get("think_level", "")),
                    step.get("timeout")
                )
                
                if not result and step.get("required", True):
                    self.log(f"Required step failed: {step.get('name')}", "ERROR")
                    return False
                    
            elif step_type == "parallel":
                # Run parallel tasks
                parallel_tasks = step.get("tasks", [])
                results = asyncio.run(self.run_parallel_tasks(parallel_tasks))
                
                # Check if any required tasks failed
                for j, (task, result) in enumerate(zip(parallel_tasks, results)):
                    if not result and task.get("required", True):
                        self.log(f"Required parallel task {j+1} failed", "ERROR")
                        return False
                        
            elif step_type == "wait":
                # Wait step
                wait_time = step.get("seconds", 1)
                self.log(f"Waiting {wait_time} seconds...")
                time.sleep(wait_time)
                
            elif step_type == "conditional":
                # Conditional execution
                condition = step.get("condition")
                if condition and eval(condition):
                    # Execute conditional steps
                    sub_workflow = {
                        "name": f"{workflow['name']} - Conditional",
                        "steps": step.get("steps", [])
                    }
                    self.execute_workflow(sub_workflow)
        
        self.log(f"Workflow completed: {workflow['name']}")
        return True
    
    def save_history(self, filename: str = "workflow-history.json"):
        """Save workflow execution history"""
        
        with open(filename, 'w') as f:
            json.dump(self.workflow_history, f, indent=2)
        
        self.log(f"Saved workflow history to {filename}")

# Example workflows
def create_example_workflows(orchestrator: ClaudeOrchestrator):
    """Create example workflow definitions"""
    
    # TDD Workflow
    tdd_workflow = orchestrator.create_workflow(
        "TDD Feature Development",
        "Develop features using Test-Driven Development",
        [
            {
                "name": "Analyze Requirements",
                "type": "claude_code",
                "prompt": "Analyze the requirements for the new feature. Do NOT write code.",
                "tools": ["READ"],
                "think_level": "think hard"
            },
            {
                "name": "Write Tests",
                "type": "claude_code",
                "prompt": "Write comprehensive tests based on requirements. No implementation.",
                "tools": ["WRITE", "EDIT"],
                "think_level": "think"
            },
            {
                "name": "Implement Feature",
                "type": "claude_code",
                "prompt": "Implement the feature to make all tests pass.",
                "tools": ["EDIT", "WRITE", "READ", "BASH"],
                "think_level": "ultrathink"
            }
        ]
    )
    
    # Parallel Analysis Workflow
    parallel_workflow = orchestrator.create_workflow(
        "Parallel Code Analysis",
        "Analyze code from multiple perspectives simultaneously",
        [
            {
                "name": "Parallel Analysis",
                "type": "parallel",
                "tasks": [
                    {
                        "prompt": "Analyze code for security vulnerabilities",
                        "tools": ["READ", "GREP"],
                        "think_level": "think hard"
                    },
                    {
                        "prompt": "Analyze code for performance issues",
                        "tools": ["READ", "GREP"],
                        "think_level": "think hard"
                    },
                    {
                        "prompt": "Analyze code for maintainability",
                        "tools": ["READ"],
                        "think_level": "think"
                    }
                ]
            },
            {
                "name": "Synthesize Results",
                "type": "claude_code",
                "prompt": "Synthesize all analysis results into a comprehensive report",
                "tools": ["WRITE"],
                "think_level": "think"
            }
        ]
    )

if __name__ == "__main__":
    # Example usage
    orchestrator = ClaudeOrchestrator(debug=True)
    
    # Create example workflows
    create_example_workflows(orchestrator)
    
    # Example: Run a simple task
    result = orchestrator.run_claude_code(
        "Analyze the current directory structure",
        [ClaudeTool.LS, ClaudeTool.READ],
        ThinkLevel.THINK
    )
    
    # Save history
    orchestrator.save_history()

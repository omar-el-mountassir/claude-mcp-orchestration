# Performance Optimization Guide

Optimizing Claude Desktop and Claude Code performance while maintaining functionality.

## Performance Metrics

### Key Indicators
1. **Response Time**: Time from prompt to completion
2. **Memory Usage**: RAM consumption per MCP server
3. **Token Usage**: API tokens consumed per operation
4. **Success Rate**: Percentage of successful completions
5. **Context Window**: Effective use of available context

## Optimization Strategies

### 1. MCP Server Optimization

#### Minimal Server Approach
```json
{
  "mcpServers": {
    "// Start with only essential servers": "comment",
    "essential-only": {
      "command": "...",
      "env": {
        "CACHE_ENABLED": "true",
        "CONNECTION_POOL_SIZE": "5",
        "TIMEOUT": "30000"
      }
    }
  }
}
```

#### Server Performance Tuning
```python
# Database server optimization
{
  "database": {
    "command": "uvx",
    "args": ["mcp-alchemy"],
    "env": {
      "DB_URL": "postgresql://localhost/db",
      "POOL_SIZE": "10",
      "POOL_TIMEOUT": "30",
      "POOL_RECYCLE": "3600",
      "ECHO": "false",  # Disable SQL logging
      "RESULT_LIMIT": "1000"  # Limit result size
    }
  }
}
```

### 2. Claude Code Optimization

#### Tool Selection
```python
def optimize_tool_selection(task):
    """
    Select minimal tools for each task
    """
    tool_mapping = {
        "read_only": ["Read", "Grep", "LS"],
        "write_simple": ["Write"],
        "edit_complex": ["Edit", "Read"],
        "full_development": ["Edit", "Write", "Read", "Bash", "Task"],
        "analysis": ["Read", "Task", "Write"]
    }
    
    # Determine task type and return minimal tools
    task_type = analyze_task_type(task)
    return tool_mapping.get(task_type, ["Read"])
```

#### Thinking Level Optimization
```python
class ThinkingOptimizer:
    """
    Use appropriate thinking levels for tasks
    """
    
    @staticmethod
    def get_optimal_thinking(task_complexity, task_type):
        """
        Returns optimal thinking level based on task
        """
        if task_complexity == "trivial":
            return ""  # No special thinking
        elif task_complexity == "simple":
            return "think"
        elif task_complexity == "moderate":
            return "think hard"
        elif task_complexity == "complex":
            return "think harder"
        elif task_complexity == "critical" or task_type == "architecture":
            return "ultrathink"
        else:
            return "think"
```

### 3. Context Management

#### Efficient Context Usage
```python
class ContextOptimizer:
    """
    Optimize context window usage
    """
    
    def __init__(self, max_context_tokens=8000):
        self.max_context_tokens = max_context_tokens
        self.context_buffer = []
    
    def add_context(self, content, priority=5):
        """
        Add content with priority (1-10, 10 being highest)
        """
        self.context_buffer.append({
            "content": content,
            "priority": priority,
            "tokens": self.estimate_tokens(content)
        })
    
    def get_optimized_context(self):
        """
        Return context that fits within token limit
        """
        # Sort by priority
        sorted_context = sorted(
            self.context_buffer,
            key=lambda x: x["priority"],
            reverse=True
        )
        
        # Build context within token limit
        final_context = []
        total_tokens = 0
        
        for item in sorted_context:
            if total_tokens + item["tokens"] <= self.max_context_tokens:
                final_context.append(item["content"])
                total_tokens += item["tokens"]
        
        return "\n\n".join(final_context)
    
    def estimate_tokens(self, text):
        """
        Rough token estimation (4 chars = 1 token)
        """
        return len(text) // 4
```

#### Session Management
```bash
# Clear sessions regularly
#!/bin/bash

# Claude Code session management
if [ $(claude sessions list | wc -l) -gt 10 ]; then
    echo "Cleaning old Claude Code sessions..."
    claude sessions clear --older-than 1h
fi

# Use focused sessions
claide new-session "feature-x-implementation"
```

### 4. Parallel Processing

#### Efficient Task Distribution
```python
import asyncio
from concurrent.futures import ThreadPoolExecutor

class ParallelOrchestrator:
    """
    Optimize parallel task execution
    """
    
    def __init__(self, max_workers=3):
        self.executor = ThreadPoolExecutor(max_workers=max_workers)
    
    async def run_parallel_analysis(self, codebase_path):
        """
        Analyze different aspects in parallel
        """
        tasks = [
            self.analyze_security(codebase_path),
            self.analyze_performance(codebase_path),
            self.analyze_quality(codebase_path)
        ]
        
        results = await asyncio.gather(*tasks)
        return self.synthesize_results(results)
    
    async def analyze_security(self, path):
        return await asyncio.to_thread(
            claude_code,
            f"Analyze {path} for security issues only",
            tools=["Read", "Grep"],
            think_level="think hard"
        )
```

### 5. Caching Strategies

#### Response Caching
```python
import hashlib
import json
import time

class ResponseCache:
    """
    Cache Claude responses for repeated queries
    """
    
    def __init__(self, cache_dir=".claude-cache", ttl=3600):
        self.cache_dir = cache_dir
        self.ttl = ttl
        os.makedirs(cache_dir, exist_ok=True)
    
    def get_cache_key(self, prompt, tools, think_level):
        """
        Generate cache key from parameters
        """
        key_data = {
            "prompt": prompt,
            "tools": sorted(tools),
            "think_level": think_level
        }
        
        key_string = json.dumps(key_data, sort_keys=True)
        return hashlib.sha256(key_string.encode()).hexdigest()
    
    def get(self, prompt, tools, think_level):
        """
        Retrieve from cache if valid
        """
        cache_key = self.get_cache_key(prompt, tools, think_level)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        if os.path.exists(cache_file):
            with open(cache_file, 'r') as f:
                cached = json.load(f)
            
            if time.time() - cached["timestamp"] < self.ttl:
                return cached["response"]
        
        return None
    
    def set(self, prompt, tools, think_level, response):
        """
        Cache the response
        """
        cache_key = self.get_cache_key(prompt, tools, think_level)
        cache_file = os.path.join(self.cache_dir, f"{cache_key}.json")
        
        with open(cache_file, 'w') as f:
            json.dump({
                "timestamp": time.time(),
                "response": response
            }, f)
```

### 6. Resource Monitoring

#### Performance Monitor
```python
import psutil
import time

class PerformanceMonitor:
    """
    Monitor Claude and MCP server performance
    """
    
    def __init__(self):
        self.metrics = []
    
    def measure_operation(self, operation_name, func, *args, **kwargs):
        """
        Measure performance of an operation
        """
        # Before
        start_time = time.time()
        start_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        # Execute
        result = func(*args, **kwargs)
        
        # After
        end_time = time.time()
        end_memory = psutil.Process().memory_info().rss / 1024 / 1024  # MB
        
        # Record metrics
        self.metrics.append({
            "operation": operation_name,
            "duration": end_time - start_time,
            "memory_delta": end_memory - start_memory,
            "timestamp": time.time()
        })
        
        return result
    
    def get_report(self):
        """
        Generate performance report
        """
        if not self.metrics:
            return "No metrics recorded"
        
        avg_duration = sum(m["duration"] for m in self.metrics) / len(self.metrics)
        max_memory = max(m["memory_delta"] for m in self.metrics)
        
        return f"""
        Performance Report:
        - Operations: {len(self.metrics)}
        - Avg Duration: {avg_duration:.2f}s
        - Max Memory Delta: {max_memory:.2f}MB
        - Slowest Operation: {max(self.metrics, key=lambda x: x['duration'])['operation']}
        """
```

## Performance Best Practices

### 1. Start Lean
- Begin with minimal configuration
- Add servers/tools only when needed
- Monitor impact of each addition

### 2. Batch Operations
```python
# Instead of multiple small operations
for file in files:
    claude_code(f"Analyze {file}")

# Batch into single operation
claide_code(f"Analyze these files: {', '.join(files)}")
```

### 3. Use Appropriate Models
- Use Claude Code for heavy lifting
- Use Desktop for planning/review
- Don't use ultrathink for simple tasks

### 4. Clean Up Regularly
- Clear old sessions
- Remove unused MCP servers
- Clean cache periodically

### 5. Monitor and Iterate
- Track performance metrics
- Identify bottlenecks
- Optimize based on data

## Troubleshooting Performance Issues

### High Memory Usage
1. Check for memory leaks in MCP servers
2. Limit result sizes in database queries
3. Clear Claude Code sessions
4. Restart MCP servers periodically

### Slow Response Times
1. Reduce number of active MCP servers
2. Use appropriate thinking levels
3. Optimize context size
4. Check network connectivity

### Token Usage Optimization
1. Use focused prompts
2. Implement response caching
3. Batch similar operations
4. Use summaries for long contexts

---

*Performance optimization is an ongoing process. Monitor, measure, and iterate.*
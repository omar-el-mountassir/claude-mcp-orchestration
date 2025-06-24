#!/usr/bin/env python3
"""
Automated Code Review Workflow
Combines multiple perspectives for comprehensive code review
"""

import subprocess
import json
import sys
from datetime import datetime
import os

def run_claude_code(prompt, tools=None, think_level="think"):
    """Execute Claude Code with review focus"""
    cmd = ["claude", "-p", f"{think_level} {prompt}"]
    
    if tools:
        cmd.extend(["--allowedTools"] + tools)
    
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout if result.returncode == 0 else None

def multi_perspective_review(pr_number):
    """
    Review code from multiple perspectives using Task
    """
    
    print(f"🔍 Starting multi-perspective review for PR #{pr_number}")
    
    review_prompt = f"""
    Use Task to spawn 5 specialized review agents for PR #{pr_number}:
    
    1. Security Reviewer:
       - Check for vulnerabilities
       - Review authentication/authorization
       - Identify data exposure risks
       - Check input validation
    
    2. Performance Analyst:
       - Identify bottlenecks
       - Check for N+1 queries
       - Review algorithm complexity
       - Memory usage concerns
    
    3. Code Quality Inspector:
       - Check design patterns
       - Review naming conventions
       - Identify code smells
       - Assess maintainability
    
    4. Test Coverage Analyst:
       - Review test completeness
       - Check edge cases
       - Identify missing tests
       - Assess test quality
    
    5. Architecture Reviewer:
       - Check architectural decisions
       - Review component coupling
       - Assess scalability
       - Identify technical debt
    
    Each agent should:
    - Read the PR changes
    - Analyze their specific area
    - Provide findings with severity (High/Medium/Low)
    - Suggest specific improvements
    
    Synthesize all findings into a comprehensive review.
    """
    
    return run_claude_code(
        review_prompt,
        tools=["Task", "Read", "Bash", "Write"],
        think_level="ultrathink"
    )

def generate_review_report(review_results, pr_number):
    """
    Generate formatted review report
    """
    
    report_prompt = f"""
    Create a professional code review report for PR #{pr_number}:
    
    Review Results:
    {review_results}
    
    Format the report with:
    1. Executive Summary
    2. Critical Issues (must fix)
    3. Important Issues (should fix)
    4. Suggestions (nice to have)
    5. Positive Aspects
    6. Recommended Actions
    
    Use markdown formatting.
    Save as 'pr-{pr_number}-review.md'
    """
    
    return run_claude_code(
        report_prompt,
        tools=["Write"],
        think_level="think"
    )

def post_review_comment(pr_number, review_file):
    """
    Post review as PR comment
    """
    
    post_prompt = f"""
    Post the review from {review_file} as a comment on PR #{pr_number}.
    
    Use gh CLI to:
    1. Read the review file
    2. Post as a comment
    3. Add appropriate labels based on findings
    4. Request changes if critical issues found
    """
    
    return run_claude_code(
        post_prompt,
        tools=["Read", "Bash"],
        think_level="think"
    )

def automated_review_workflow(pr_number):
    """
    Complete automated review workflow
    """
    
    print(f"\n🤖 Automated Code Review for PR #{pr_number}")
    print("=" * 50)
    
    try:
        # Step 1: Multi-perspective review
        print("\n📊 Step 1: Conducting multi-perspective review...")
        review_results = multi_perspective_review(pr_number)
        
        if not review_results:
            print("❌ Review failed")
            return False
        
        # Step 2: Generate report
        print("\n📝 Step 2: Generating review report...")
        report = generate_review_report(review_results, pr_number)
        
        # Step 3: Post to PR
        print("\n💬 Step 3: Posting review to PR...")
        review_file = f"pr-{pr_number}-review.md"
        post_result = post_review_comment(pr_number, review_file)
        
        print("\n✅ Review completed successfully!")
        print(f"📄 Review saved to: {review_file}")
        
        return True
        
    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        return False

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: ./automated-review.py <pr_number>")
        sys.exit(1)
    
    pr_number = sys.argv[1]
    success = automated_review_workflow(pr_number)
    
    sys.exit(0 if success else 1)
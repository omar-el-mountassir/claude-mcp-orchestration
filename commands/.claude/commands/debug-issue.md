# Debug GitHub Issue

Debug and fix issue #$ARGUMENTS

## Systematic Debugging Process:

### 1. Issue Analysis
- Read issue details with `gh issue view $ARGUMENTS`
- Identify the reported problem
- Note reproduction steps
- Check for additional context in comments

### 2. Reproduction
- Set up the environment
- Follow reproduction steps exactly
- Confirm the issue exists
- Document actual vs expected behavior

### 3. Investigation
- Use grep to search for relevant code
- Identify the problematic component
- Trace the execution flow
- Add debug logging if needed

### 4. Root Cause Analysis
- Identify why the issue occurs
- Check for edge cases
- Verify assumptions in the code
- Look for related issues

### 5. Solution Development
- Design a fix that addresses root cause
- Consider impact on other components
- Ensure backward compatibility
- Write the fix

### 6. Testing
- Test the specific issue is resolved
- Run existing tests
- Add new tests for this case
- Check for regressions

### 7. Documentation
- Update code comments
- Add to changelog
- Update relevant documentation
- Prepare clear PR description

Use appropriate thinking level based on issue complexity.
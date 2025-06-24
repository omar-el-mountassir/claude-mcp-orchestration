# Refactor with Test Coverage

Refactor code while maintaining/improving test coverage: $ARGUMENTS

## Refactoring Protocol:

### Phase 1: Current State Analysis
1. **Analyze existing code**
   - Understand current implementation
   - Identify code smells
   - Map dependencies
   - Document current behavior

2. **Review existing tests**
   - Run current test suite
   - Check coverage
   - Identify missing test cases
   - Note fragile tests

### Phase 2: Test Enhancement
1. **Add missing tests**
   - Write tests for uncovered code
   - Add edge case tests
   - Ensure behavior is documented in tests
   - All tests must pass

2. **Refactor tests if needed**
   - Improve test readability
   - Remove duplication
   - Add better assertions
   - Use appropriate test patterns

### Phase 3: Incremental Refactoring
1. **Plan refactoring steps**
   - Break into small, safe changes
   - Maintain functionality at each step
   - Keep tests passing

2. **Execute refactoring**
   - Make one change at a time
   - Run tests after each change
   - Commit working states
   - Use think hard for complex decisions

### Phase 4: Optimization
1. **Performance improvements**
   - Profile if needed
   - Optimize critical paths
   - Maintain readability

2. **Code quality**
   - Apply design patterns
   - Improve naming
   - Enhance documentation
   - Reduce complexity

### Phase 5: Final Validation
1. **Comprehensive testing**
   - Run full test suite
   - Check coverage improved
   - Manual testing if needed
   - Performance comparison

2. **Documentation**
   - Update API docs
   - Add refactoring notes
   - Document new patterns

Use ultrathink for architectural decisions.
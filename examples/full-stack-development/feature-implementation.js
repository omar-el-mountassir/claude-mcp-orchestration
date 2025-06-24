#!/usr/bin/env node

/**
 * Full-Stack Feature Implementation Example
 * Demonstrates coordinated frontend/backend development
 */

const { spawn } = require('child_process');
const fs = require('fs').promises;
const path = require('path');

// Configuration
const FEATURE_NAME = process.argv[2] || 'user-authentication';
const PROJECT_ROOT = process.cwd();

/**
 * Execute Claude Code with specific parameters
 */
async function executeClaudeCode(prompt, tools = [], thinkLevel = '') {
    const args = ['-p'];
    
    if (thinkLevel) {
        args.push(`${thinkLevel} ${prompt}`);
    } else {
        args.push(prompt);
    }
    
    if (tools.length > 0) {
        args.push('--allowedTools', ...tools);
    }
    
    return new Promise((resolve, reject) => {
        const claude = spawn('claude', args);
        let output = '';
        
        claude.stdout.on('data', (data) => {
            output += data.toString();
            process.stdout.write(data);
        });
        
        claude.stderr.on('data', (data) => {
            process.stderr.write(data);
        });
        
        claude.on('close', (code) => {
            if (code === 0) {
                resolve(output);
            } else {
                reject(new Error(`Claude Code exited with code ${code}`));
            }
        });
    });
}

/**
 * Main workflow for full-stack feature implementation
 */
async function implementFullStackFeature() {
    console.log(`\n🚀 Implementing Full-Stack Feature: ${FEATURE_NAME}`);
    console.log('='.repeat(50));
    
    try {
        // Phase 1: Architecture Planning
        console.log('\n📐 Phase 1: Architecture Planning');
        await executeClaudeCode(
            `Create a detailed architecture plan for ${FEATURE_NAME} including: ` +
            '1. Frontend components structure (React/Vue/Angular), ' +
            '2. Backend API endpoints (REST/GraphQL), ' +
            '3. Database schema changes, ' +
            '4. Authentication/Authorization flow, ' +
            '5. State management approach. ' +
            'Save the plan to architecture-plan.md',
            ['Write'],
            'think hard'
        );
        
        // Phase 2: Database Setup
        console.log('\n🗄️ Phase 2: Database Setup');
        await executeClaudeCode(
            'Based on the architecture plan, create: ' +
            '1. Database migration files, ' +
            '2. Seed data for development, ' +
            '3. Database models/entities, ' +
            '4. Validation schemas',
            ['Write', 'Read'],
            'think'
        );
        
        // Phase 3: Backend Implementation
        console.log('\n⚙️ Phase 3: Backend API Implementation');
        await executeClaudeCode(
            `Implement the backend for ${FEATURE_NAME}: ` +
            '1. Create API endpoints, ' +
            '2. Implement business logic, ' +
            '3. Add input validation, ' +
            '4. Implement error handling, ' +
            '5. Add authentication middleware, ' +
            '6. Write unit tests',
            ['Write', 'Edit', 'Read', 'Bash'],
            'ultrathink'
        );
        
        // Phase 4: Frontend Implementation
        console.log('\n🎨 Phase 4: Frontend Implementation');
        await executeClaudeCode(
            `Create the frontend for ${FEATURE_NAME}: ` +
            '1. Build React/Vue components, ' +
            '2. Implement state management, ' +
            '3. Create forms with validation, ' +
            '4. Add error handling, ' +
            '5. Implement responsive design, ' +
            '6. Write component tests',
            ['Write', 'Edit', 'Read'],
            'think hard'
        );
        
        // Phase 5: Integration
        console.log('\n🔗 Phase 5: Frontend-Backend Integration');
        await executeClaudeCode(
            'Integrate frontend with backend: ' +
            '1. Connect API endpoints, ' +
            '2. Implement data fetching with loading states, ' +
            '3. Handle API errors gracefully, ' +
            '4. Add authentication tokens, ' +
            '5. Implement real-time updates if needed',
            ['Edit', 'Read'],
            'think'
        );
        
        // Phase 6: Testing
        console.log('\n🧪 Phase 6: End-to-End Testing');
        await executeClaudeCode(
            'Create and run comprehensive tests: ' +
            '1. Write E2E tests for critical paths, ' +
            '2. Test error scenarios, ' +
            '3. Test authentication flows, ' +
            '4. Performance testing, ' +
            '5. Accessibility testing',
            ['Write', 'Bash', 'Read'],
            'think'
        );
        
        // Phase 7: Documentation
        console.log('\n📚 Phase 7: Documentation');
        await executeClaudeCode(
            'Create comprehensive documentation: ' +
            '1. API documentation with examples, ' +
            '2. Frontend component documentation, ' +
            '3. Setup and deployment guide, ' +
            '4. User guide with screenshots, ' +
            '5. Update main README',
            ['Write', 'Edit', 'Read']
        );
        
        // Phase 8: Code Review Preparation
        console.log('\n👀 Phase 8: Code Review Preparation');
        await executeClaudeCode(
            'Prepare for code review: ' +
            '1. Run linters and fix issues, ' +
            '2. Ensure consistent code style, ' +
            '3. Add meaningful comments, ' +
            '4. Create PR description, ' +
            '5. List testing instructions',
            ['Edit', 'Bash', 'Write']
        );
        
        console.log('\n✅ Full-Stack Feature Implementation Complete!');
        console.log('\n📁 Generated artifacts:');
        console.log('  - architecture-plan.md');
        console.log('  - backend/');
        console.log('  - frontend/');
        console.log('  - tests/');
        console.log('  - docs/');
        console.log('\n🎉 Ready for review and deployment!');
        
    } catch (error) {
        console.error('\n❌ Error during implementation:', error.message);
        process.exit(1);
    }
}

// Helper function to create project structure
async function ensureProjectStructure() {
    const dirs = [
        'backend/src/controllers',
        'backend/src/models',
        'backend/src/routes',
        'backend/src/middleware',
        'backend/tests',
        'frontend/src/components',
        'frontend/src/pages',
        'frontend/src/services',
        'frontend/src/store',
        'frontend/tests',
        'database/migrations',
        'database/seeds',
        'docs/api',
        'docs/guides'
    ];
    
    for (const dir of dirs) {
        await fs.mkdir(path.join(PROJECT_ROOT, dir), { recursive: true });
    }
}

// Main execution
(async () => {
    if (!FEATURE_NAME) {
        console.error('Usage: ./feature-implementation.js "<feature-name>"');
        process.exit(1);
    }
    
    // Ensure project structure exists
    await ensureProjectStructure();
    
    // Run the implementation workflow
    await implementFullStackFeature();
})();
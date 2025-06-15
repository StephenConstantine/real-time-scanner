#!/usr/bin/env python3
"""Test runner script for Real-Time Event Exploration System.

This script provides a convenient way to run different types of tests
with appropriate configurations and reporting.
"""

import sys
import subprocess
import argparse
from pathlib import Path


def run_command(cmd, description):
    """Run a command and handle the output."""
    print(f"\n{'='*50}")
    print(f"Running: {description}")
    print(f"Command: {' '.join(cmd)}")
    print(f"{'='*50}")
    
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, check=False)
        
        if result.stdout:
            print(result.stdout)
        
        if result.stderr:
            print("STDERR:")
            print(result.stderr)
        
        if result.returncode != 0:
            print(f"\n❌ {description} failed with exit code {result.returncode}")
            return False
        else:
            print(f"\n✅ {description} completed successfully")
            return True
            
    except Exception as e:
        print(f"\n❌ Error running {description}: {e}")
        return False


def main():
    """Main test runner function."""
    parser = argparse.ArgumentParser(description="Run tests for Real-Time Event Exploration System")
    parser.add_argument(
        '--type', '-t',
        choices=['all', 'unit', 'integration', 'fast', 'slow', 'coverage'],
        default='unit',
        help='Type of tests to run (default: unit)'
    )
    parser.add_argument(
        '--verbose', '-v',
        action='store_true',
        help='Verbose output'
    )
    parser.add_argument(
        '--file', '-f',
        help='Run specific test file'
    )
    parser.add_argument(
        '--function', '-k',
        help='Run tests matching pattern'
    )
    parser.add_argument(
        '--coverage', '-c',
        action='store_true',
        help='Run with coverage report'
    )
    parser.add_argument(
        '--html-coverage',
        action='store_true',
        help='Generate HTML coverage report'
    )
    
    args = parser.parse_args()
    
    # Ensure we're in the right directory
    project_root = Path(__file__).parent
    print(f"Running tests from: {project_root}")
    
    # Base pytest command
    cmd = ['python3', '-m', 'pytest']
    
    # Add verbosity
    if args.verbose:
        cmd.append('-vv')
    
    # Add coverage if requested
    if args.coverage or args.html_coverage or args.type == 'coverage':
        cmd.extend(['--cov=modules', '--cov-report=term-missing'])
        if args.html_coverage or args.type == 'coverage':
            cmd.append('--cov-report=html')
    
    # Add specific file if provided
    if args.file:
        cmd.append(f"tests/{args.file}")
    
    # Add pattern matching if provided
    if args.function:
        cmd.extend(['-k', args.function])
    
    # Handle test type selection
    if args.type == 'unit':
        cmd.extend(['-m', 'unit or not (integration or slow or network or ai)'])
        description = "Unit Tests"
    elif args.type == 'integration':
        cmd.extend(['-m', 'integration'])
        description = "Integration Tests"
    elif args.type == 'fast':
        cmd.extend(['-m', 'not (slow or network or ai)'])
        description = "Fast Tests"
    elif args.type == 'slow':
        cmd.extend(['-m', 'slow'])
        description = "Slow Tests"
    elif args.type == 'coverage':
        description = "All Tests with Coverage"
    else:  # all
        description = "All Tests"
    
    # Run the tests
    success = run_command(cmd, description)
    
    if args.html_coverage or args.type == 'coverage':
        coverage_dir = project_root / 'htmlcov'
        if coverage_dir.exists():
            print(f"\n📊 HTML coverage report generated at: {coverage_dir / 'index.html'}")
    
    # Exit with appropriate code
    sys.exit(0 if success else 1)


if __name__ == '__main__':
    main()


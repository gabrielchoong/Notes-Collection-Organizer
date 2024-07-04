#!/bin/bash

# Define functions for each task
sync_readme() {
    echo "Syncing README.md to docs/..."
    cp README.md docs/
}

run_tests() {
    echo "Running tests..."
    echo "eg. pytest tests/"
}

show_help() {
    echo "Usage: $0 {sync-readme|run-tests|all|help}"
    echo "  sync-readme   : Sync README.md to docs/"
    echo "  run-tests     : Run test suite"
    echo "  all           : Execute all tasks sequentially"
    echo "  help          : Show this help message"
}

# Parse command line arguments
case "$1" in
    sync-readme)
        sync_readme
        ;;
    run-tests)
        run_tests
        ;;
    all)
        sync_readme
        run_tests
        ;;
    help|--help|-h)
        show_help
        ;;
    *)
        echo "Invalid option: $1"
        show_help
        exit 1
        ;;
esac

#!/bin/bash

copy_from_template() {
    echo "Copying template/docs-template.md to $1..."
    cp template/docs-template.md "$1"
}

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
    echo "  copy-from-template  : Copy template file to destination file"
    echo "  sync-readme         : Sync README.md to docs/"
    echo "  run-tests           : Run test suite"
    echo "  all                 : Execute all tasks sequentially"
    echo "  help                : Show this help message"
}

# Parse command line arguments
case "$1" in
    copy-from-template)
        if [ -z "$2" ]; then
            echo "Error: No destination file specified."
            show_help
            exit 1
        fi
        copy_from_template "$2"
        ;;
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

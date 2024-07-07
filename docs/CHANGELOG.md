# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

<!-- This is a comment in Markdown 

Types of changes

Added: for new features.
Changed: for changes in existing functionality.
Deprecated: for soon-to-be removed features.
Removed: for now removed features.
Fixed: for any bug fixes.
Security: in case of vulnerabilities.

-->

## [Unreleased]

### Work In Progress

- Optimise `--update` option.

## [v0.3.1] - 2024-07-07

### Added

- `--update` option updates tags used in all notes into `docs/tags.txt`.

### Changed

- `--target-folder` now creates folder if `path/to/folder` doesn't exist, instead of giving an error.


## [v0.3.0] - 2024-07-07

### Added

- `--search` option is now functional.

## [0.2.1] - 2024-07-05

### Main Feature

- Only patch notes were added. No functionality change.

### Patch Notes

- Added install guide in `INSTALL.md`.
- Added instructions in `USAGE.md`.
- Slightly updated `README.md`
- Updated `docs-template.md` and `note-template.md` in `template/`.

## [0.2.0] - 2024-07-05

### Main Features

- Functionality to create notes without a template.
- Added `tasks.sh` for file versions and backup.
- Minor bug fixes regarding the new `--no-template` option.

### Added

- Initial version of the `tasks.sh` script with `sync-readme`, `run-tests`, and `all` options.
- Function to create notes from a template.
- Function to create blank notes.
- Ability to add tags to notes.
- `tasks.sh` to automate common tasks.
- Functions in `utils.py` are now modularised in `scripts/` folder.
- `.gitignore` for executables

### Changed

- Updated argument parsing to handle `--no-template` option.
- Separated `search_notes` function into its own function.
- Moved note creation functions to `create_note.py`.
- Updated `.markdownlint.json` to include `MD024: false`.

### Fixed

- Bug where notes were being created with both template and blank options.
- Bug where tags are broken with `--no-template` option.

## [0.1.0] - 2024-07-04

### Main Features

- Basic functionality to create notes from a template.

### Added

- This `CHANGELOG.md` file to hopefully serve as an evolving example of a standardized open source project CHANGELOG.
- Initial setup of the notes organizer project.
- Basic functionality to create notes from a template.
- Command-line interface for creating notes.

# DEVELOPMENT.md

## Project Overview

The Digital Notes Collection project is designed to streamline and manage note-taking using templates and flexible options for creating notes with or without templates. This project aims to improve the efficiency of note-taking and organization.

## Features Implemented

1. **Initial Setup**
   - Created the initial project structure.
   - Set up version control with GitHub.

2. **Command Line Interface (CLI)**
   - Implemented argument parsing for various options using `argparse`.
   - Added options for creating notes with a template and creating blank notes.

3. **Note Creation Functions**
   - `create_note_from_template(titles, create_tags, target_folder)`: Creates a new note based on a specified template.
   - `create_note_without_template(titles, create_tags, target_folder)`: Creates a new blank note without a template.

4. **Template Handling**
   - Added functionality to check for the existence of a template file and raise an error if not found.
   - Implemented reading template content from a file.

5. **Handling Different Options**
   - Ensured that the `--no-template` option works correctly without arguments and only creates a blank note when specified.

6. **Error Handling**
   - Added error handling for missing template files.

7. **Utility Scripts**
   - Created `tasks.sh` for general shell scripting tasks.
   - Implemented various tasks such as syncing README files and running tests.
   - Added the option to run all tasks sequentially.

8. **File Organization**
   - Organized utility functions into a separate `scripts/` folder for better manageability.
   - Kept track of tasks in `tasks.sh`.

9. **Documentation**
   - Maintained a `README.md` for project description and usage instructions.
   - Planned to create a `CHANGELOG.md` to keep track of changes and updates.

## Main Features in Version 0.2.0

- Functionality to create notes without a template.
- Added `tasks.sh` for file versions and backup.
- Minor bug fixes regarding the new `--no-template` option.

## Notes

- Recent development highlights include better management of note creation options and improved error handling.
- Future updates may include additional features and refinements based on user feedback and project requirements.

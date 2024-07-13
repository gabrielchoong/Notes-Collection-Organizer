# Notes Collection Organizer

## Overview

The Notes Collection Organizer is a tool designed to help manage digital notes efficiently. This project is in the early stages of development.

## Features

- Template-based note creation
- Tag-based search functionality

## Installation

Clone the repository:

```bash
git clone https://github.com/gabrielchoong/Notes-Collection-Organizer.git
cd notes-collection
```

Dependencies

- There are no dependencies at the moment

## Usage

### Creating a New Note

To create a new note based on a template:

```bash
python utils.py --create "Title of Your Note" --target-folder "notes"
```

### Searching Notes

To search for notes based on tags:

```bash
python utils.py --search tag1 tag2
```

## Development Status

The following features are currently being developed or are not fully functional:

- `--update` only works for adding tags, not removing them currently.
- a `.config` file will be used for future versions `> v0.3.1`.
- see [here](https://github.com/gabrielchoong/Notes-Collection-Organizer/issues/1#issue-2393893617) for updates.

## Contact

For any questions or suggestions, please contact me at my [discord](https://discord.com/users/791233489232068618).

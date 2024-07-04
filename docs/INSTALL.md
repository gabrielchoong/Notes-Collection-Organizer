# Overview

This **Note Organiser** uses the command line for interacting with notes. If you are unfamiliar with the terminal, I will provide step-by-step explanations for each command.

## Installation

### Prerequisites

**Git**

- The **Note Organiser** works best with a version control system (VCS) such as Git. Git saves the history of a repository, making it easy to view file activity.
- Follow the [official guide](https://github.com/git-guides/install-git) for installing Git.

**Python**

- This project is developed under Python version `3.9.19`. Any Python version greater than this should work seamlessly with the **Note Organiser**.
- Please follow the instructions on the [official Python website](https://www.python.org/downloads/) to install Python.

### Steps

If you haven't installed Git on your system, download the latest release from the repository and unzip the contents.

1. **Clone the repository**

```bash
git clone https://github.com/gabrielchoong/Notes-Collection-Organizer.git
cd Notes-Collection-Organizer
```

2. **Verify the installation**

```bash
python utils.py --help
```

You should see a result similar to this:

```bash
usage: utils.py [-h] [--search [TAG ...]] [--create TITLE [TITLE ...]] [--no-template] [--tags TAG [TAG ...]] [--target-folder FOLDER]

Digital Notes Organizer.

optional arguments:
  -h, --help            show this help message and exit
  --search [TAG ...]    search notes based on given tag(s)
  --create TITLE [TITLE ...]
                        create new notes based on template with specified title(s)
  --no-template         create new notes without a template with specified title(s)
  --tags TAG [TAG ...]  add tags directly to the new note(s)
  --target-folder FOLDER
                        specify the target folder to save the new notes (default: current folder)
```

Congratulations! You have successfully installed the **Note Organiser**. For usage guides, please refer to [USAGE.md](USAGE.md).

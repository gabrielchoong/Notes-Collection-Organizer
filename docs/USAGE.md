# Overview

After the initial installation, you will find two utility scripts: `utils.py` and `tasks.sh` in the root folder. If not, please verify the installation process.

## Features

### `utils.py`

- Create notes based on a template.
- Create notes without a template.

### `tasks.sh`

- Copy a file from template to `path/to/file`.
- Sync `README.md` to `docs/`.

If you do not intend to modify the **Note Organizer**, you can ignore `tasks.sh`.

### Prerequisites

Ensure `python >= 3.9` is installed on your system. You can verify by typing either of the commands:

```bash
python --version
```

```bash
python3 --version
```

If you wish to install Python on your system, please refer to the [official page](https://www.python.org/downloads/).

## Creating your first Note

### Basic Usage

```bash
python utils.py --create note1 --target-folder notes/
```

### Advanced Usage

```bash
python utils.py --create note1 --target-folder notes/ --tags tag1 tag2 ...
```

Alternatively, without using a template:

```bash
python utils.py --create note1 --target-folder notes/ --tags tag1 tag2 ... --no-template
```

### Available Options

```bash
python utils.py --help
```

If `python` is not recognized, try `python3` instead.

## Modifying the Project

You can ignore this part if you don't intend to modify the **Note Organizer**. However, it's recommended to try out the commands in case you want to modify anything in the future.

In the project root folder, you will find `tasks.sh`. This file aims to simplify the process of modifying the **Note Organizer**.

### Commands

In your terminal, type:

```bash
chmod +x tasks.sh
./tasks.sh
```

The first command lets you run `./tasks.sh` directly. Alternatively, you could use `bash tasks.sh` manually.

You should see a few options show up like this:

```bash
Invalid option:
Usage: ./tasks.sh {sync-readme|run-tests|all|help}
  copy-from-template  : Copy template file to destination file
  sync-readme         : Sync README.md to docs/
  run-tests           : Run test suite
  all                 : Execute all tasks sequentially
  help                : Show this help message
```

Here, you will see every possible option you can run with `tasks.sh`. Here are some example commands:

```bash
./tasks.sh sync-readme # Sync README.md in project root to docs/README.md
```

```bash
./tasks.sh run-tests # Verify project health
```

```bash
./tasks.sh help # Show help message
```

Not recommended unless you are developing new features:

```bash
./tasks.sh all # Run every option available
```

# DEVELOPMENT.md

## Project Overview

The Digital Notes Collection project is designed to streamline and manage note-taking using templates and flexible options for creating notes with or without templates. This project aims to improve the efficiency of note-taking and organization.

## Important

This project assumes the markdown format `.md` is used for every note. If you already use a plain text file `.txt` to store your notes, I highly encourage you to try out this alternative note format. More information can be found [here](https://www.markdownguide.org/basic-syntax/).

## Features in Version 0.3.2

- Create a note with the `--create` option.
- Target Folder can be specified with the `--target-folder` option.
  - By default, the app will create a folder called `notes/` within the project root.
- A template can be used for creating new notes. This can be disabled using the `--no-template` option. You can also customise the template directory and template contents in the `config.ini` file.
- Tags are highly advised to be used when creating new notes. This can be done using the `--tag` option and passing tag(s) desired, separated with a space in between.
  - Tags can be modified in the future after the creation of the note.
- Search a note with the `--search` option.
  - Currently, it can only search tags used in all notes.
- Update all notes used with the `--update` option.
  - This option will search every note within a note folder, grabbing the tags and store it in a `tags.txt` file which is located in the `docs/` directory in the project root.

### Using config.ini

- Starting from v0.3.2, a `config.ini` file will be used to store user variables. This is different from all verions before, where variables are manually assigned.

## Planned Features

Currently, as I'm developing this project on my own, I will only be updating this project every two days. There are certain features that I want to add in the future, including:

- Search option with varying arguments (date, name, title etc.).
- Sort option for notes. Although I'm not sure why is this feature required as most file manager already have a sort function.
- Conversion of `.md` files to `.pdf` format. This is the top priority for any file conversions for this project.
- GUI of some sort. However I recommend you use Visual Studio Code or any other text editors with the markdown preview function.
  - It's likely to be written in electron as well.
- OCR to convert handwritten notes into markdown format.
- File sharing. This is likely not going to come in anytime soon.

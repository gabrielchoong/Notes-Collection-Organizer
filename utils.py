import argparse

from scripts.create_note import create_note_from_template, create_note_without_template

def search_notes(tags):
    if tags is None:
        print('Searching notes with no tags specified')
    else:
        print(f'Searching notes with tags: {tags}')
        # Implement search function

def main():

    """
    Main entry point for the Digital Notes Organizer script.

    This function sets up the argument parser, processes command-line arguments,
    and calls the appropriate functions to handle creating and searching notes.

    Command-line arguments:
        --search TAG [TAG ...]    Search notes based on given tag(s).
        --create TITLE [TITLE ...]    Create new notes based on template with specified title(s).
        --tags TAG [TAG ...]    Add tags directly to the new note(s).
        --target-folder FOLDER    Specify the target folder to save the new notes (default: current folder).
    """


    parser = argparse.ArgumentParser(description='Digital Notes Organizer.',
                                     formatter_class=argparse.RawTextHelpFormatter)

    parser.add_argument(
        '--search', dest='search_tags', nargs='*', metavar='TAG',
        help='search notes based on given tag(s)',
    )

    parser.add_argument(
        '--create', dest='title', type=str, nargs='+', metavar='TITLE',
        help='create new notes based on template with specified title(s)',
    )

    parser.add_argument(
        '--no-template', dest='title_blank', action='store_true',
        help='create new notes without a template with specified title(s)',
    )

    parser.add_argument(
        '--tags', dest='create_tags', type=str, nargs='+', metavar='TAG',
        help='add tags directly to the new note(s)',
    )

    parser.add_argument(
        '--target-folder', dest='target_folder', type=str, default='.', metavar='FOLDER',
        help='specify the target folder to save the new notes (default: current folder)',
    )
    

    args = parser.parse_args()

    if args.search_tags is not None:
        search_notes(args.search_tags)

    if args.title:
        if args.title_blank:
            create_note_without_template(args.title, args.create_tags, args.target_folder)
        else:
            create_note_from_template(args.title, args.create_tags, args.target_folder)


if __name__ == "__main__":
    main()
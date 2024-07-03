import os
import argparse
from datetime import datetime

def create_note_from_template(titles, tags, target_folder):
    # Define the path to your templates folder
    templates_folder = 'template'

    # Construct the path to the template file
    template_filename = os.path.join(templates_folder, 'note-template.md')

    # Check if the template file exists
    if not os.path.exists(template_filename):
        raise FileNotFoundError(f"Template file '{template_filename}' not found.")

    # Read the contents of note-template.md
    with open(template_filename, 'r', encoding='utf-8') as f:
        template_content = f.read()

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    date = now.strftime("%d-%m-%Y")

    for title in titles:
        # Generate a new filename based on the current timestamp and title
        new_filename = f"{timestamp}-{title.replace(' ', '-').lower()}.md"

        # Construct the full path to the new note file
        note_path = os.path.join(target_folder, new_filename)

        # Replace the title and date in the YAML front matter
        modified_content = template_content.replace('Title of Your Note', title).replace('Date of Creation or Last Update', date)

        # Add tags to the YAML front matter if provided
        if tags:
            tags_str = ', '.join(tags)
            modified_content = modified_content.replace('tags: [List of Tags]', f'tags: [{tags_str}]')

        # Write the modified content to a new Markdown file
        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)

        print(f"Created new note: {new_filename}")

def search_notes(tags):
    if tags is None:
        print('Searching notes with no tags specified')
    else:
        print(f'Searching notes with tags: {tags}')
        # Implement your search logic here based on tags

def main():
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
        create_note_from_template(args.title, args.create_tags, args.target_folder)

if __name__ == "__main__":
    main()
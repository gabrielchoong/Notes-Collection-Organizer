import os
import re
from datetime import datetime

def list_tags(tags_list_file):

    user_input = input("List tags used? [y/n]: ")

    if user_input == 'y':
        with open(tags_list_file, 'r') as f:
            tags_list = set(tag.strip().lower() for tag in f.readlines())
            tags_list = sorted(tags_list)

        for tags in tags_list:
            print(tags)

    else:
        print('OK')

def update_tags(tags_list_file, notes_folder, action=None):

    """
    Update tags.txt with new tags found in notes.

    Args:
        tags_list_file (str): Path to the tags.txt file.
        notes_folder (str): Path to the folder containing notes.
    """

    new_tags = set()
    tag_regex = re.compile(r'tags:\s*\[(.*?)\]', re.IGNORECASE | re.DOTALL)

    # Python doesn't recognise `~` as the home directory
    notes_folder = os.path.expanduser(notes_folder)

    if not os.path.exists(notes_folder):
        raise FileNotFoundError(f"Notes folder '{notes_folder}' not found.")

    with open(tags_list_file, 'r') as f:
        tags_list = set(tag.strip().lower() for tag in f.readlines())

    for note_filename in os.listdir(notes_folder):
        if note_filename.endswith('.md'):
            with open(os.path.join(notes_folder, note_filename), 'r') as f:
                note_content = f.read()

            front_matter_end = note_content.find('---', note_content.find('---') + 3)
            if front_matter_end != -1:
                note_content = note_content[:front_matter_end]

            match = tag_regex.search(note_content)

            if match:
                note_tags = [tag.strip().lower() for tag in match.group(1).split(',') if tag.strip()]

                # Check for new tags not in tags.txt
                for tag in note_tags:
                    if tag not in tags_list:
                        new_tags.add(tag)

    # Update tags.txt with new tags
    if new_tags:
        with open(tags_list_file, 'a') as f:
            for tag in new_tags:
                f.write(f'{tag}\n')

        print(f'Updated tags.txt with {len(new_tags)} new tag(s): {new_tags}')
    else:
        print('No new tags found in notes.')

    list_tags(tags_list_file)

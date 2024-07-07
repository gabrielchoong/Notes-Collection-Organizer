import os
import re
from scripts.config import load_config

config = load_config()

# Used in search_notes()
def find_tags_linear(list1, list2):
    set1 = set(list1)
    duplicates = [item for item in list2 if item in set1]
    return duplicates

def search_notes(tags):
    """
    Search for notes containing specified tags in their YAML front matter within the 'notes' folder.

    Args:
        tags (list of str): List of tags to search for within note YAML front matter.

    Prints:
        - Information about the search operation and results.

    Notes:
        - Assumes YAML front matter format 'tags: [tag1, tag2, ...]'.
        - Tags are matched case-insensitively.
        - Stops looking for tags after encountering the second '---' in each note file.

    Raises:
        FileNotFoundError: If 'tags.txt' file in 'docs' folder is not found.

    """

    print(f'Searching notes with tags: {tags}')

    notes_folder = config['notesfolder']
    tags_list_file = config['tagslistfile']

    with open(tags_list_file, 'r') as f:
        tags_list = f.read().split()
    
    duplicates = find_tags_linear(tags, tags_list)
    print(f'Found {len(duplicates)} distinct tags: {duplicates}')

    notes_with_matching_tags = []

    # Regular expression to find tags in note content
    tag_regex = re.compile(r'tags:\s*\[(.*?)\]', re.IGNORECASE | re.DOTALL)

    for note_filename in os.listdir(notes_folder):

        # Driver code
        if note_filename.endswith('.md'):
            with open(os.path.join(notes_folder, note_filename), 'r') as f:
                note_content = f.read()

            # stop looking for tags after hitting the second "---"
            front_matter_end = note_content.find('---', note_content.find('---') + 3)
            if front_matter_end != -1:
                note_content = note_content[:front_matter_end] # truncate end of YAML front matter

            match = tag_regex.search(note_content)

            if match:
                note_tags = [tag.strip() for tag in match.group(1).split(',') if tag.strip()]

                if any(tag in duplicates for tag in note_tags):
                    notes_with_matching_tags.append(note_filename)

    print(f'Found {len(notes_with_matching_tags)} notes with matching tags: {notes_with_matching_tags}')

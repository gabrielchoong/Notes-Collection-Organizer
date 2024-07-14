import os
import re
from scripts.config import load_config

config = load_config()
notes_folder = config['notesfolder']
tags_list_file = config['tagslistfile']

tag_regex = re.compile(r'tags:\s*(\[.*?\]|\s*((?:\s*-\s*\w+)+))', re.IGNORECASE | re.DOTALL | re.MULTILINE)

def extract_tags_and_check_duplicates(
    note_filename: str,
    note_content: str,
    tag_regex: re.Pattern,
    duplicates: list[str]
) -> list[str]:
    match = tag_regex.search(note_content)
    notes_with_matching_tags = []

    if match:
        note_tags = [tag.strip() for tag in re.split(r'[,-]', match.group(1)) if tag.strip()]

        if any(tag in duplicates for tag in note_tags):
            notes_with_matching_tags.append(note_filename)

    return notes_with_matching_tags

def _matching_tags(duplicates: list[str]) -> list[str]:
    for note_filename in os.listdir(notes_folder):

        if note_filename.endswith('.md'):
            with open(os.path.join(notes_folder, note_filename), 'r', encoding='utf-8') as f:
                note_content = f.read()

            # stop looking for tags after hitting the second "---"
            front_matter_end = note_content.find('---', note_content.find('---') + 3)

            if front_matter_end != -1:
                note_content = note_content[:front_matter_end] # truncate end of YAML front matter

            match = extract_tags_and_check_duplicates(note_filename, note_content, tag_regex, duplicates)

    return match

def find_tags_linear(list1: list[str], list2: list[str]) -> list[str]:
    set1 = set(list1)
    duplicates = [item for item in list2 if item in set1]
    return duplicates

def _tags_list(tags_list_file: str) -> list[str]:
    with open(tags_list_file, 'r') as f:
        tags_list = f.read().split()

    return tags_list

def search_notes(tags: list[str]) -> None:

    print(f'Searching notes with tags: {tags}')

    tags_list = _tags_list(tags_list_file)
    
    duplicates = find_tags_linear(tags, tags_list)

    print(f'Found {len(duplicates)} distinct tags: {duplicates}')

    match = _matching_tags(duplicates)

    print(f'Found {len(match)} notes with matching tags: {match}')

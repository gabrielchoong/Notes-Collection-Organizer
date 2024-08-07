
import os
from scripts.config import load_config
from datetime import datetime

config = load_config()

def ensure_folder_exists(folder_path):

    """
    Ensure that the specified folder exists. If not, create it.
    
    Args:
        folder_path (str): Path to the folder.
    """

    if not os.path.exists(folder_path):

        print(f"Folder does not exist. Creating folder {folder_path}")
        os.makedirs(folder_path)

def create_note_from_template(titles, tags, target_folder=None):

    """
    Create new notes from a template with specified titles and save them to a target folder.

    Args:
        titles (list of str) : List of titles for the new notes.
        tags (list of str) : List of tags to be added to the new notes.
        target_folder (str) : Path to the folder where the new notes will be saved.

    Raises:
        FileNotFoundError: If the template file does not exist, or path is incorrect.
    """

    if target_folder is None:
        target_folder = os.path.expanduser(config['notesfolder'])

    ensure_folder_exists(target_folder)

    # Changing date format will mess up existing files. Proceed with caution.
    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    date = now.strftime("%d-%m-%Y")


    templates_folder = config['templatesfolder']
    template_file = config['templatefile']
    template_filename = os.path.join(templates_folder, template_file)

    if not os.path.exists(template_filename):
        raise FileNotFoundError(f"Template file '{template_filename}' not found.")

    with open(template_filename, 'r', encoding='utf-8') as f:
        template_content = f.read()
    

    # Driver code.
    for title in titles:

        new_filename = f"{timestamp}-{title.replace(' ', '-').lower()}.md"

        note_path = os.path.join(target_folder, new_filename)

        modified_content = template_content.replace('Title of Your Note', title).replace('Date of Creation or Last Update', date).replace('Your Name', config['author'])

        if tags:
            tags_str = ', '.join(tags)
            modified_content = modified_content.replace('tags: [List of Tags]', f'tags: [{tags_str}]')

        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(modified_content)

        print(f"Created new note: {new_filename} in {target_folder}")

def create_note_without_template(titles, tags, target_folder=None):

    """
    Create new blank notes with specified titles and save them to a target folder.

    Args:
        titles (list of str): List of titles for the new notes.
        tags (list of str): List of tags for the new notes.
        target_folder (str): Path to the folder where the new notes will be saved.
    """

    if target_folder is None:
        target_folder = os.path.expanduser(config['notesfolder'])

    ensure_folder_exists(target_folder)

    now = datetime.now()
    timestamp = now.strftime("%Y-%m-%d-%H-%M-%S")
    date = now.strftime("%d-%m-%Y")


    # Driver code
    for title in titles:

        new_filename = f"{timestamp}-{title.replace(' ', '-').lower()}.md"
        note_path = os.path.join(target_folder, new_filename)

        content = f"""---\ntitle: {title}\ndate: {date}\nauthor: {config['author']}\ntags: {[', '.join(tags)] if tags else '[List of Tags]'}\n---\n# {title}\n"""

        if tags:
            tags_str = ', '.join(tags)
            content = content.replace('tags: [List of Tags]', f'tags: [{tags_str}]')

        with open(note_path, 'w', encoding='utf-8') as f:
            f.write(content)

        print(f"Created new blank note: {new_filename} in {target_folder}")

import configparser

def load_config():
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    return {
        'notesfolder': config.get('DEFAULT', 'notesfolder', fallback='notes'),
        'tagslistfile': config.get('DEFAULT', 'tagslistfile', fallback='docs/tags.txt'),
        'templatesfolder': config.get('DEFAULT', 'templatesfolder', fallback='template'),
        'templatefile': config.get('DEFAULT', 'templatefile', fallback='note-template.md'),
        'author': config.get('DEFAULT', 'author', fallback='Your Name')
    }
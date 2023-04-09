import os

def list_files_matching_pattern(pattern, start_dir='.'):
    """
    Returns a list of all files in the given folder (and its subfolders)
    that match the given pattern.
    """
    file_list = []
    for root, _, files in os.walk(start_dir, topdown=True):
        for file in files:
            if file.endswith(pattern):
                file_list.append(os.path.join(root, file))
    return file_list


def get_file_contents(filename):
    """
    Returns the contents of the given file as a string.
    """
    with open(filename, 'r') as file:
        contents = file.read()
    return contents

def replace_file_with_content(filename, content):
    with open(filename, 'w') as file:
        file.write(content)
    
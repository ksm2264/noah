from dotenv import load_dotenv
from bot.memory.file_semantic_grouping import FileGrouping
from bot.cli import list_files_matching_pattern, replace_file_with_content
import os
import openai
from bot.agents.find_target_groups import find_groups
from bot.agents.code_writer import write_code\


idea = '''
A rhythm game that uses a MIDI keyboard as a controller, 
and uses MIDI files to render scrolling notes onto an on screen keyboard.
 It scores the user based on how accurately in time they are able to 
 press the correct keys at the correct time. 
 The user can load any MIDI file of a piano track
 '''

def implement_feature(feature_request):

    file_list = list_files_matching_pattern('.py', 'src/')
    # print(file_list)
    store = FileGrouping(idea, file_list)
    store.build_store()

    # print(store.store)

    category_lookup = store.store

    categories = list(category_lookup.keys())

    targets = find_groups(idea, categories, feature_request)

    # print(targets)

    target_files = []
    for target in targets:
        target_files+=store.store[target]
        
    code_dict = write_code(feature_request, target_files)

    for file, content in code_dict.items():
        # print(f'replacing file: {file} with content: {content}')
        replace_file_with_content(file, content)

    return True
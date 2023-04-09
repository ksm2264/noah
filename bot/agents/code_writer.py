# -*- coding: utf-8 -*-
"""
Created on Sat Apr  8 21:04:54 2023

@author: karl
"""

import openai

from bot.cli import get_file_contents

gpt_model = "gpt-3.5-turbo"

def write_code(feature_description, files_to_change):

    system_message = '''
    Given a desired new feature, and files,
    respond with the changed version of each of the files to implement the feature.
    Respond by alternating file names and contents like so:
    @@@file_nam1e@@@file_content1@@@file_name2@@@file_content_2@@@ etc.
    Only respond with that format
    '''
    
    files_dict = {}
    
    for file in files_to_change:
        files_dict[file] = get_file_contents(file)

    user_message = f'feature: {feature_description}, files to change: {files_dict}'
    print(feature_description)
    messages = [
        {"role":"system",
         "content":system_message},
        {"role":"user",
         "content":user_message}
    ]

    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages
    )

    response_dict = response.to_dict()
    raw_text = response_dict['choices'][0]['message']['content']

    split_txt = raw_text.split('@@@')

    if len(split_txt)%2 == 1:
        split_txt = split_txt[1:]

    changed_files = {}
    
    for i in range(0, len(split_txt), 2):
        key = split_txt[i]
        value = split_txt[i+1]
        changed_files[key] = value
            
    return changed_files
    

from cli import get_file_contents
import openai
import json

gpt_model = "gpt-3.5-turbo"
# gpt_model = "gpt-4"

def get_categories(app_summary, existing_categories, file_name):

    system_message = '''
    list out which categories this file belongs to.
    use existing groups, and/or come up with new ones.
    these categories should be software domains. (e.g. controller, input_handler, etc)
    respond only with JSON:'["category_1", "category_2"]'
    '''

    file_content = get_file_contents(file_name)

    user_message = f'app_summary: {app_summary}, existing groups: {existing_categories}, file content: {file_content}'
    print(existing_categories)
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

    categories = json.loads(raw_text)
            
    return categories

def attempt_prompt(messages):
    
   


    return success, categories
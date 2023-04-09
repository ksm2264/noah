import openai

gpt_model = 'gpt-3.5-turbo'

def json_cleaner(raw_txt): 

    system_message = '''
    you are responsible for cleaning invalid json outputs, fix them such that they are valid
    e.g.:
    '["item_1", "item_2"]'
    Make sure that you only respond with the cleaned JSON, and nothing else.
    '''

    messages = [
            {"role":"system",
            "content":system_message},
            {"role":"user",
            "content":f'please fix this JSON: {raw_txt}'}
        ]

    response = openai.ChatCompletion.create(
        model=gpt_model,
        messages=messages
    )

    response_dict = response.to_dict()
    raw_text = response_dict['choices'][0]['message']['content']

    return raw_text
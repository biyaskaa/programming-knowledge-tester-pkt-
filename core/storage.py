import json

def load_questions(path, enc):
    with open(path, 'r', encoding=enc) as f:
        data = json.load(f)
    return data


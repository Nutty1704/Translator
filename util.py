import json

def get_language_code(l: str) -> str:
    with open('lang.json', 'r') as f:
        lang = json.load(f)

    try:
        return lang[l]
    except KeyError:
        for k, v in lang.items():
            if l in k:
                return v
        
        return ''

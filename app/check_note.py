import requests

def check_spelling(text):
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    params = {
        "text": text,
        "lang": "ru"

    }
    response = requests.get(url, params=params)
    return response.json()

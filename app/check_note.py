import requests


def correct_text(text):
    url = "https://speller.yandex.net/services/spellservice.json/checkText"
    params = {
        "text": text,
        "lang": "ru",
        "options": 1 + 4,
    }

    response = requests.get(url, params=params)
    errors = response.json()

    corrected_text = text

    for error in errors:
        word_with_error = error['word']
        suggested_correction = error['s'][0] if error['s'] else word_with_error
        corrected_text = corrected_text.replace(word_with_error,
                                                suggested_correction)

    return corrected_text

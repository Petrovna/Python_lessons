import requests
import json

KEY = 'trnsl.1.1.20161216T160124Z.4a07c4b6a2f01566.ade260e6c684818698899fd08a9c15d72faca843'
URL = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

def translate_me(file_in, file_out, lang_in, lang_out):
    with open(file_in) as file_input:
        mytext = file_input.read()

    params = {
        'key': KEY,
        'text': mytext,
        'lang': lang_in +'-'+lang_out,
    }
    with open(file_out, 'w') as file_output:
        response = requests.get(URL, params=params)
        trans = (response.json()['text'])
        file_output.write(''.join(trans))


translate_me('DE.txt', 'DE_RU.txt', 'de', 'ru')
translate_me('ES.txt', 'ES_RU.txt', 'es', 'ru')
translate_me('FR.txt', 'FR_RU.txt', 'fr', 'ru')



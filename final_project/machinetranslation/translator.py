import os
import json
from dotenv import load_dotenv
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

load_dotenv()

apikey = os.getenv('apikey')
url = os.getenv('url')

authenticator = IAMAuthenticator(apikey)
translator = LanguageTranslatorV3(
               version='2018-05-01',
               authenticator=authenticator
               )
translator.set_service_url(url)

def english_to_french(english_text):
    french_text = translator.translate(
        text=english_text,
        source='en',
        target='fr'
    ).get_result()

    return french_text['translations'][0]['translation']

def french_to_english(french_text):
    english_text = translator.translate(
        text=french_text,
        source='fr',
        target='en'
    ).get_result()

    return english_text['translations'][0]['translation']

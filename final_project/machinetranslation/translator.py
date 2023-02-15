import os
from ibm_watson import LanguageTranslatorV3,ApiException
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
     version='2018-05-01',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def englishToFrench(englishText):
    """
    Translates english text to french via Watson API
    """
    try:
        response = language_translator.translate(text=englishText, model_id='en-fr')
        frenchText = response.get_result()['translations'][0]['translation']
    except ApiException as exception:
        print("Api failed with error: " +str(exception.code) + ": " + exception.message +"\n")
        return ""
    return frenchText

def frenchToEnglish(frenchText):
    """
    Translates french text to english via Watson API
    """
    try:
        response = language_translator.translate(text=frenchText, model_id='fr-en')
        englishText = response.get_result()['translations'][0]['translation']
    except ApiException as exception:
        print("Api failed with error: " +str(exception.code) + ": " + exception.message + "\n")
        return ""
    return englishText


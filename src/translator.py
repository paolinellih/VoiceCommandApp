import asyncio
from googletrans import Translator

async def translate_to_portuguese(text):
    translator = Translator()
    # `await` the translation to handle the coroutine properly
    translation = await translator.translate(text, src='en', dest='pt')
    return translation.text
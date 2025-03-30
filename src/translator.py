import asyncio
from deep_translator import GoogleTranslator

async def translate_to_portuguese(text):
    translated_text = GoogleTranslator(source="auto", target="pt").translate(text)
    return translated_text
import gtts
from datetime import datetime


def audio_generate(text: str, filename: str) -> None:
    audio = gtts.gTTS(text, lang="fr", tld="fr")
    audio.save(filename)
    return None

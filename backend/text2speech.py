import gtts
from datetime import datetime


def audio_generate(text):
    filename = f"./recording/bot-gen-{str(datetime.now().now())}.wav"
    audio = gtts.gTTS(text, lang="fr", slow=True)
    audio.save(filename)
    return filename

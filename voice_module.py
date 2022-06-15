import requests
import subprocess

import soundrecord as sr
import speech2text as stt
import text2speech as tts

bot_response = ""

while bot_response not in ["À bientôt", "Au revoir", "À plus", "Bye"]:
    message = "Bye"
    start = input("Voulez vous enregistrer n message (N/y): ")
    if start.lower() == "y":
        vocal_in = sr.recording()
        message = stt.prediction(file=vocal_in)

    print("you ->", message)
    response = requests.post(
        "http://localhost:5002/webhooks/rest/webhook", json={"message": message}
    )
    print("bot -> ", end=" ")
    for r in response.json():
        bot_response = r["text"] or "Pouvez-vous repeter svp?"
        vocal_response = tts.audio_generate(bot_response)
        print(bot_response)
        subprocess.call(["mpg321", "-q", vocal_response])

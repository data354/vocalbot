from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import src.speech2text as stt
import requests
import gtts
import io
from time import time
from typing import Dict, Union
from fastapi.staticfiles import StaticFiles
from scipy.io.wavfile import read, write


app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.mount("/assets", StaticFiles(directory="src/assets"), name="assets")


@app.post("/audio/send")
async def speech_to_text(audio: bytes = File()) -> Dict[str, str]:

    message = stt.prediction(file=audio)
    print("user ->", message)
    response = requests.post(
        "http://localhost:5002/webhooks/rest/webhook", json={"message": message}
    )
    print("bot -> ", end=" ")

    tmp = "".join(r["text"] + " " for r in response.json())
    bot_response = tmp or "Pouvez-vous repeter s'il vous plait?"
    audio_gen = gtts.gTTS(bot_response, lang="fr", tld="fr")
    filename = f"bot-gen-{time()}.mp3"
    audio_gen.save(f"src/assets/recording/{filename}")
    # # then, let's save it to a BytesIO object, which is a buffer for bytes object
    # fp = io.BytesIO()
    # audio_gen.write_to_fp(fp)
    # audio_utter = fp.read()
    # print(type(audio_utter))
    # print(audio_utter)
    return {"bot_uttered": bot_response, "audio": filename}


@app.post("/message/send")
async def text(message: str = File()):

    print("user ->", message)
    response = requests.post(
        "http://localhost:5002/webhooks/rest/webhook", json={"message": message}
    )
    print("bot -> ", end=" ")
    bot_response = ""
    for r in response.json():
        bot_response += r["text"] + "\n\n"
        print("*", bot_response)
    return {"bot_uttered": bot_response}

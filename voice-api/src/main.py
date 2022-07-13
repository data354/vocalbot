from time import time

import gtts
import requests
from typing import Dict
from fastapi import FastAPI, File
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware

import src.speech2text as stt
import src.text2speech as tts


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

RASA_URL = "http://localhost:5002/webhooks/rest/webhook"

app.mount("/assets", StaticFiles(directory="src/assets"), name="assets")


@app.post("/audio/send")
async def speech_to_text(audio: bytes = File()) -> Dict[str, str]:

    message = stt.prediction(file=audio)
    print("user ->", message)
    response = requests.post(RASA_URL, json={"message": message})

    tmp = "".join(r["text"] + " " for r in response.json())
    bot_response = tmp or "Pouvez-vous repeter s'il vous plait?"
    print("bot -> ", bot_response)
    filename = f"bot-gen-{time()}.mp3"
    tts.audio_generate(
        bot_response.replace("*", ""), filename=f"src/assets/recording/{filename}"
    )
    return {"bot_uttered": bot_response, "audio": filename}


@app.post("/message/send")
async def text(message: str = File()) -> Dict[str, str]:

    print("user ->", message)
    response = requests.post(RASA_URL, json={"message": message})
    print("bot -> ", end=" ")
    bot_response = "".join(r["text"] + " " for r in response.json())
    print("bot ->", bot_response)
    return {"bot_uttered": bot_response}

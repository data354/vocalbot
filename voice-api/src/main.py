from fastapi import FastAPI, UploadFile, File
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import src.speech2text as stt

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


# class AudioData(BaseModel):
#     audio: list


@app.post("/audio/send")
async def speech_to_text(audio: bytes = File()):

    message = stt.prediction(file=audio)
    print("user ->", message)
    return {"bot_utter": message}

import contextlib
import sys

import queue
import sounddevice as sd
import soundfile as sf
from datetime import datetime
from time import time

channels = 1
samplerate = 44100

q = queue.Queue()


def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())
    return None


def recording() -> str:
    """Record, save audio and return the audio file name"""
    filename = f"./recording/record-{str(datetime.now().date())}-{time()}.wav"
    with contextlib.suppress(KeyboardInterrupt):
        # Make sure the file is opened before recording anything:
        with sf.SoundFile(
            filename, mode="x", samplerate=samplerate, channels=channels
        ) as file:
            with sd.InputStream(
                samplerate=samplerate, channels=channels, callback=callback
            ):
                print("#" * 80)
                print("press Ctrl+C to stop the recording")
                print("#" * 80)
                while True:
                    file.write(q.get())

    return filename

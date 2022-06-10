import librosa
from transformers import (
    Wav2Vec2ForCTC,
    Wav2Vec2Processor,
)
import torch


model_name = "jonatasgrosman/wav2vec2-large-xlsr-53-french"  # "facebook/wav2vec2-large-xlsr-53-french"
device = "cpu"  # "cuda"

asr = Wav2Vec2ForCTC.from_pretrained(model_name).to(device)
processor = Wav2Vec2Processor.from_pretrained(model_name)


def make_prediction(file: str) -> str:
    speech_array, sampling_rate = librosa.load(file, sr=16000)
    features = processor(
        speech_array, sampling_rate=sampling_rate, padding=True, return_tensors="pt"
    )
    input_values = features.input_values.to(device)
    attention_mask = features.attention_mask.to(device)
    with torch.no_grad():
        logits = asr(input_values, attention_mask=attention_mask).logits
    pred_ids = torch.argmax(logits, dim=-1)
    return processor.batch_decode(pred_ids)[0]

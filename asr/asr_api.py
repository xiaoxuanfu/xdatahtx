from fastapi import FastAPI, File, UploadFile, HTTPException
from fastapi.responses import JSONResponse
import soundfile as sf
import torch
import io
import torchaudio
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

app = FastAPI()

# Load the pre-trained model and processor
processor = Wav2Vec2Processor.from_pretrained("facebook/wav2vec2-large-960h")
model = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h").eval()  # Ensure model is in eval mode

@app.get("/ping")
async def ping():
    return "pong"

@app.post("/asr")
async def transcribe_audio(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        audio_input, sample_rate = sf.read(io.BytesIO(contents), dtype='float32')

        # Check and resample if the audio is not at 16000Hz
        if sample_rate != 16000:
            resampler = torchaudio.transforms.Resample(orig_freq=sample_rate, new_freq=16_000)
            audio_input = resampler(torch.tensor(audio_input, dtype=torch.float32))

        input_values = processor(audio_input, sampling_rate=16_000, return_tensors="pt").input_values
        with torch.no_grad():
            logits = model(input_values).logits
        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = processor.batch_decode(predicted_ids)[0]
        duration = len(audio_input) / 16000  # Use the resampled rate

        return JSONResponse(content={"transcription": transcription, "duration": f"{duration:.2f}"})
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


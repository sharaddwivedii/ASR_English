import torch
import torchaudio
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC

processor = Wav2Vec2Processor.from_pretrained("./wav2vec2-finetuned")
model = Wav2Vec2ForCTC.from_pretrained("./wav2vec2-finetuned")

def transcribe_audio(file_path):
    # Load audio file
    speech_array, sampling_rate = torchaudio.load(file_path)
    
    # Resample if necessary (to 16kHz)
    if sampling_rate != 16000:
        resampler = torchaudio.transforms.Resample(sampling_rate, 16000)
        speech_array = resampler(speech_array)

    # Process the audio
    input_values = processor(speech_array.squeeze().numpy(), sampling_rate=16000, return_tensors="pt").input_values

    # Generate transcription
    with torch.no_grad():
        logits = model(input_values).logits

    # Decode the logits to text
    predicted_ids = torch.argmax(logits, dim=-1)
    transcription = processor.batch_decode(predicted_ids)
    
    return transcription[0]

if __name__ == "__main__":
    # Example usage
    import sys
    if len(sys.argv) < 2:
        print("Please provide a path to an audio file.")
    else:
        file_path = sys.argv[1]
        transcription = transcribe_audio(file_path)
        print("Transcription:", transcription)

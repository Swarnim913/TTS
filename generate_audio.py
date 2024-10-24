import re
from transformers import SpeechT5Processor, SpeechT5ForTextToSpeech, SpeechT5HifiGan
from datasets import load_dataset
import torch
import soundfile as sf
import csv
import os

# Load pre-trained models and processor
processor = SpeechT5Processor.from_pretrained("microsoft/speecht5_tts")
model = SpeechT5ForTextToSpeech.from_pretrained("microsoft/speecht5_tts")
vocoder = SpeechT5HifiGan.from_pretrained("microsoft/speecht5_hifigan")

# Load a pre-trained speaker embedding for better audio quality
# Using an embedding from the CMU Arctic X-Vectors dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embeddings = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

# Create directories for text and audio files
os.makedirs("dataset/text", exist_ok=True)
os.makedirs("dataset/audio", exist_ok=True)

# Function to add hyphens after all capital letters, with special rule for the first word
def add_hyphens_to_capitals(text):
    words = text.split()
    result = []

    # Handle the first word separately
    first_word = words[0]
    if len(re.findall(r'[A-Z]', first_word)) > 1:
        # If the first word has more than one capital letter, add hyphens between them
        first_word = ', '.join(list(first_word))
    result.append(first_word)

    # Handle the rest of the words
    for word in words[1:]:
        modified_word = re.sub(r'([A-Z])', r'\1, ', word)
        result.append(modified_word)

    return ' '.join(result)

# Read the dataset CSV and generate audio
with open('technical_tts_dataset.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for i, row in enumerate(reader):
        original_text = row['text']
        
        # Save the original text file
        text_filename = f"dataset/text/sentence{i+1}.txt"
        with open(text_filename, 'w') as text_file:
            text_file.write(original_text)

        # Modify the text by adding hyphens to abbreviations
        modified_text = add_hyphens_to_capitals(original_text)

        # Convert modified text to tokens, specifying 'text' explicitly
        inputs = processor(text=modified_text, return_tensors="pt")

        # Generate speech using the model with pre-trained speaker embedding
        with torch.no_grad():
            speech = model.generate_speech(inputs["input_ids"], speaker_embeddings, vocoder=vocoder)

        # Save the audio file with an increased sampling rate for better quality
        audio_filename = f"dataset/audio/sentence{i+1}.wav"
        sf.write(audio_filename, speech.numpy(), 24000)  # Save at 24,000 Hz for improved quality

        print(f"Generated audio for: {modified_text} -> Saved as: {audio_filename}")

print("All audio files have been generated and saved in the 'dataset/audio' directory.")
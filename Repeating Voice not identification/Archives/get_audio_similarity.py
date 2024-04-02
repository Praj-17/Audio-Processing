from pydub import AudioSegment
import numpy as np
from transformers import Wav2Vec2Processor, Wav2Vec2ForCTC
from sklearn.metrics.pairwise import cosine_similarity
import os

os.environ["CUDA_VISIBLE_DEVICES"] = "-1"

def load_audio(file_path):
    audio = AudioSegment.from_file(file_path)
    samples = np.array(audio.get_array_of_samples())
    return samples, audio.frame_rate

def extract_wav2vec_embedding(wav2vec_model, processor, samples, sample_rate):
    inputs = processor(samples, return_tensors="pt", sampling_rate=sample_rate)
    with torch.no_grad():
        embeddings = wav2vec_model(**inputs).last_hidden_state.mean(dim=1)
    return embeddings

def calculate_cosine_similarity(embedding1, embedding2):
    similarity = cosine_similarity(embedding1, embedding2)
    return similarity[0][0]

def main():
    # Replace these with your file paths
    audio_file1 = "chunk0.mp3"
    audio_file2 = "chunk1.mp3"

    # Load Wav2Vec model and processor
    model_name = "facebook/wav2vec2-base-960h"
    print("Loading Model")
    processor = Wav2Vec2Processor.from_pretrained(model_name)
    wav2vec_model = Wav2Vec2ForCTC.from_pretrained(model_name)

    # Load audio files
    samples1, sample_rate1 = load_audio(audio_file1)
    samples2, sample_rate2 = load_audio(audio_file2)

    # Extract Wav2Vec embeddings
    embedding1 = extract_wav2vec_embedding(wav2vec_model, processor, samples1, sample_rate1)
    embedding2 = extract_wav2vec_embedding(wav2vec_model, processor, samples2, sample_rate2)

    # Calculate cosine similarity
    similarity = calculate_cosine_similarity(embedding1, embedding2)

    print(f"Cosine Similarity between {audio_file1} and {audio_file2}: {similarity}")

if __name__ == "__main__":
    main()

from pydub import AudioSegment
import librosa
import random
import soundfile as sf
def apply_pitch_shift(audio, n_steps):
    audio, sr = librosa.load(audio, sr=16000, mono=True)
    shifted = librosa.effects.pitch_shift(audio, sr=16000, n_steps=n_steps)
    sf.write('a.wav' , shifted, sr)

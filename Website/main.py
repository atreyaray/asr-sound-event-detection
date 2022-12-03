import streamlit as st
from audio_recorder_streamlit import audio_recorder
import numpy as np
import matplotlib.pyplot as plt
import librosa


# streamlit run Website/main.py

'''
# Sound Audio Detection

'''

audio_bytes = audio_recorder()
if audio_bytes:
    st.audio(audio_bytes, format="audio/wav")

    # convert bytes to numpy array
    audio = np.frombuffer(audio_bytes, dtype=np.int16)

    # plot audio waveform
    # use librosa to plot spectrogram 
    fig, ax = plt.subplots(1, 2, figsize=(10, 5))
    ax[0].plot(audio)
    ax[0].set(title="Audio Waveform")
    ax[0].label_outer()
    ax[1].specgram(audio, Fs=44100)
    ax[1].set(title="Audio Spectrogram")
    ax[1].label_outer()

    st.pyplot(fig)

    audio.shape
    
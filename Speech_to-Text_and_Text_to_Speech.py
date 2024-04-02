import streamlit as st
from gtts import gTTS
import speech_recognition as sr

def text_to_speech(text, language='en'):
    """Converts text to speech and plays the audio."""
    speech = gTTS(text=text, lang=language)
    with st.spinner("Generating audio..."):
        speech.save("output.mp3")
    st.audio("output.mp3", format="audio/mpeg")

def speech_to_text():
    """Records audio from microphone and transcribes it to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        st.write("Listening...")
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        st.write("You said:", text)
        return text
    except sr.UnknownValueError:
        st.write("Sorry, could not understand audio")
        return None

def text_to_speech_tab():
    st.title("Text-to-Speech")
    text_input = st.text_input("Enter text to convert to speech:")
    language_select = st.selectbox("Select language:", ("en", "es", "fr", "de", "it", "ja"))  # Example languages
    if st.button("Convert to Speech"):
        text_to_speech(text_input, language=language_select)

def speech_to_text_tab():
    st.title("Speech-to-Text")
    if st.button("Speak to Text"):
        user_text = speech_to_text()

tabs = ["Text-to-Speech", "Speech-to-Text"]
selected_tab = st.sidebar.radio("Select Tab", tabs)
if selected_tab == "Text-to-Speech":
    text_to_speech_tab()
elif selected_tab == "Speech-to-Text":
    speech_to_text_tab()

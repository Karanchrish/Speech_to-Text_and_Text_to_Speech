# Text-to-Speech & Speech-to-Text Converter

This Streamlit application provides two main functionalities: converting text to speech and transcribing speech to text. It utilizes the Google Text-to-Speech (gTTS) API for text-to-speech conversion and the SpeechRecognition library for speech-to-text transcription.

---
## Features

- **Text-to-Speech Conversion**: Enter text and select a language from the provided options, then click the "Convert to Speech" button. The application will generate an audio file of the speech which you can listen to.
  
- **Speech-to-Text Transcription**: Click the "Speak to Text" button to activate your microphone. Speak into the microphone, and the application will transcribe your speech into text.

## Prerequisites

- Python 3.x
- gtts
- streamlit

## Installation

1. Clone or download this repository to your local machine.
2. Install the required dependencies using pip:
   
```bash
pip install -r requirements.txt
```

4. Navigate to the directory where you cloned/downloaded the repository.
5. Run the Streamlit app using the following command:

```
streamlit run Speech_to-Text_and_Text_to_Speech.py
```
## Usage
- Upon running the app, it will open in your default web browser.
- You will see two tabs: "Text-to-Speech" and "Speech-to-Text".
- Select the desired tab based on the functionality you want to use.
- Follow the instructions provided on each tab to perform text-to-speech or speech-to-text conversion.

### Additional Notes:

- Ensure that your microphone is properly connected and configured for speech recognition.
- Note that the accuracy of speech-to-text transcription may vary depending on factors such as background noise and accent.

---

Feel Free to Contact me

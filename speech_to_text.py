import streamlit as st
import speech_recognition as sr


def speech_to_text(audio_file):
    r = sr.Recognizer()
    with sr.AudioFile(audio_file) as source:
        audio_data = r.record(source)
        text = r.recognize_google(audio_data, language='en-US')
        return text

def main():
    st.title("Speech to Text Conversion")

    # File Upload
    audio_file = st.file_uploader("Upload Audio File", type=["wav"])
    
    if audio_file is not None:
        st.audio(audio_file, format='audio/wav')

        if st.button("Convert to Text"):
            text = speech_to_text(audio_file)
            st.success("Converted Text:")
            st.write(text)

if __name__ == "__main__":
    main()

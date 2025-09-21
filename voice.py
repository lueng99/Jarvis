import speech_recognition as sr
from audio import speak

# --- Voice setup ---
recognizer = sr.Recognizer()
def listen():
    with sr.Microphone() as mic:
        recognizer.adjust_for_ambient_noise(mic, duration=0.3)
        audio = recognizer.listen(mic)
        try:
            text = recognizer.recognize_google(audio, language="en-US").lower()
            return text
        except sr.UnknownValueError:
            return ""
        except sr.RequestError:
            speak("I have no internet connection.")
            return ""
import speech_recognition as sr
import pyttsx3
import wikipedia
import pywhatkit
import subprocess
import os #for future modifications#

# --- Voice setup ---
recognizer = sr.Recognizer()

def initiate_engine():
    engine = pyttsx3.init()
    voices = engine.getProperty("voices")
    for voice in voices:
        if "english" in voice.name.lower():
            engine.setProperty("voice", voice.id)
            break
    engine.setProperty("rate", 170)  # speed
    engine.setProperty("volume", 1.0)  # volume
    return engine

def speak(text):
    print(f"🤖 Jarvis: {text}")
    engine = initiate_engine()   # Restarts the voice motors to evade problems.
    engine.say(text)
    engine.runAndWait()
    engine.stop()            # Cleans the word lane

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

def process_command(command):
    
    if "search on google" in command or "google" in command:
        query = command.replace("search on google", "").strip()
        speak(f"Searching Google for: {query}")
        pywhatkit.search(query)

    elif "wikipedia" in command:
        query = command.replace("wikipedia", "").strip()
        try:
            summary = wikipedia.summary(query, sentences=2, auto_suggest=False, redirect=True)
            speak(summary)
        except:
            speak("I couldn’t find anything on Wikipedia.")

    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)

    elif "open word" in command:
        speak("Opening Microsoft Word.")
        try:
            # Automatic option to star windows on microsft, if it doesnt work change the subprocess to the main directory
            subprocess.Popen(["start", "winword"], shell=True)
        except Exception as e:
            speak(f"An error occurred: {str(e)}")

    elif "goodbye" in command or "exit" in command:
        speak("Goodbye, sir.")
        exit()

    elif "who am i" in command:
        speak("You are Álvaro Luengo, my creator")

    else:
        speak("Sorry, I didn’t understand that command.")
        print(command)

# --- Main loop ---
while True:
    print("🎤 Waiting for keyword...")
    text = listen()

    if "jarvis" in text or "good morning jarvis" in text or "good afternoon jarvis" in text or "good night jarvis" in text or "hey jarvis":
        speak("Hello sir, what can i do for you?")
        command = listen()
        if command:
            print(f"✅ Command: {command}")
            process_command(command)

import wikipedia
import pywhatkit
from audio import speak
import os #for future modifications#

def process_command(command):
    
    if "search on google" in command or "google" in command:
        query = command
        for phrase in ["search on google", "search google for", "google"]:
            query= query.replace(phrase, "")
        query = query.strip()
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

    elif "goodbye" in command or "exit" in command:
        speak("Goodbye, sir.")
        exit()

    elif "who am i" in command:
        speak("You are Álvaro Luengo, my creator")

    elif "thank you" in command:
        speak("you're welcome")

    else:
        speak("Sorry, I didn’t understand that command.")
        print(command)


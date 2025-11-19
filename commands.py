
import pywhatkit
from audio import speak
import os #for future modifications#
from huggingface_hub import InferenceClient
import re


import google.generativeai as genai

# 1. Configuration
# Replace with your Google AI Studio API Key
genai.configure(api_key="INSERTE AQUI SU TOKEN")

# Initialize the model
# 2. Initialize the Flash Model
# 'gemini-1.5-flash' is optimized for speed and efficiency
model = genai.GenerativeModel('gemini-1.5-flash')


def process_command(command):
    #searches in google anything you command
    if "search on google" in command or "google" in command:
        query = command
        for phrase in ["search on google", "search google for", "google"]:
            query= query.replace(phrase, "")
        query = query.strip()
        speak(f"Searching Google for: {query}")
        pywhatkit.search(query)
#plays in yt anything you command
    elif "play" in command:
        song = command.replace("play", "").strip()
        speak(f"Playing {song} on YouTube.")
        pywhatkit.playonyt(song)
#exits and finalize the programm
    elif "goodbye" in command or "exit" in command:
        speak("Goodbye, sir.")
        exit()
#tells the name of the creator
    elif "who am i" in command:
        speak("You are Álvaro Luengo, my creator")
#Its always good to give thanks a machine
    elif "thank you" in command:
        speak("you're welcome")
#any other command that the system doesnt understand it will drop it to an llm
    else: 
            # Append instructions to keep it short
        commandresume = command + " (Summarize the answer in 5 lines or less for a voice output)"
        speak("I'm working on that")
        try:
            response = model.generate_content(commandresume)
            clean_response = response.tex
            speak(clean_response)
        except Exception as e:
            print(f"Error: {e}")
            speak("I lost the connection to the cloud.")









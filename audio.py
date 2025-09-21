from enginestart import initiate_engine

def speak(text):
    print(f"Jarvis: {text}")
    engine = initiate_engine()   # Restarts the voice motors to evade problems.
    engine.say(text)
    engine.runAndWait()
    engine.stop()            # Cleans the word lane

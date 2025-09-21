import pyttsx3
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

from voice import listen
from audio import speak
from commands import process_command

# --- Main loop ---
while True:
    print("🎤 Waiting for keyword...")
    text = listen()

    if "jarvis" in text:
        speak("Hello sir, what can i do for you?")
        command = listen()
        if command:
            process_command(command)
            
# Jarvis

My own version of the AI **Jarvis**, inspired by the fictional character Tony Stark (AKA Iron Man).
Jarvis is also a university projects which has the ambition to be the first completly customizable virtual assistant, with custom commands, voices and lots of thigs that make you feel comfortable working with it
## Requirements

* Python 3
* Microphone

### Python Packages

You will need to install the following libraries:

* [SpeechRecognition](https://pypi.org/project/SpeechRecognition/)
* [pyttsx3](https://pypi.org/project/pyttsx3/)
* [wikipedia](https://pypi.org/project/wikipedia/)
* [pywhatkit](https://pypi.org/project/pywhatkit/)

You can install them using pip:

```bash
pip install SpeechRecognition pyttsx3 huggingface_hub pywhatkit
```
For linux you will also need: 
```bash
pip install pyaudio
```

## How to Use

1. Execute the file `main.py` in your **Computer terminal**.

2. When it starts, it will display:

```
Waiting for keyword
```

3. Say one of the following keywords to activate Jarvis:

* "Jarvis"
* "Hey Jarvis"
* "Good morning/evening/night, Jarvis"

4. Once Jarvis responds, you can send commands. Some examples:

* `"search on google ..."` → Searches Google for your query
* `"play ..."` → Plays the video on YouTube that you ask for
* `"exit"` or `"goodbye"` → Closes the program

---

import speech_recognition as sr
import webbrowser
import pyttsx3
import threading
import time

engine = pyttsx3.init()
engine.setProperty('rate', 150)
engine.setProperty('volume', 1.0)

musiclibrary = {
    "music": {
        "tum tak": "https://youtu.be/1nWQs6IxTrY?si=MurEvO6hC9nOanmM",
        "kk": "https://youtu.be/-8C_2BBVWk8?si=4WexIuPlXq9tB3PS",
        "tum mile": "https://youtu.be/lSlXbnOikw8?si=dxVvvShAl-09cOwv"
    }
}

def speak(text):
    print(f"[TTS]: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_for_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Tommy active, listening for command...")
        audio = r.listen(source)
    try:
        command = r.recognize_google(audio)
        print(f"Command recognized: {command}")
        processcommand(command)
    except Exception as e:
        print(f"Could not understand command: {e}")

def processcommand(c):
    c = c.lower()
    if "open google" in c:
        speak("Opening Google")
        webbrowser.open("https://google.com")
    elif "open chat gpt" in c:
        speak("Opening ChatGPT")
        webbrowser.open("https://chatgpt.com/")
    elif "open youtube" in c:
        speak("Opening YouTube")
        webbrowser.open("https://www.youtube.com/watch?v=UrsmFxEIp5k")
    elif c.startswith("play"):
        try:
            song = c.split(" ", 1)[1]
            link = musiclibrary["music"].get(song)
            if link:
                speak(f"Playing {song}")
                webbrowser.open(link)
            else:
                speak(f"Sorry, {song} not found in music library.")
        except IndexError:
            speak("Please say a song name after play.")
    
    elif "news" in c:
        speak("Opening today's news")
        webbrowser.open("https://www.google.com/search?q=today%27s+news")

    elif "how are you" in c:
        speak("i am fine sir ! what about you")
        print("i am fine sir ! what about you")

def main():
    r = sr.Recognizer()
    speak(" Tommy is waiting for sanket sir")

    while True:
        print("Listening for wake word...")
        try:
            with sr.Microphone() as source:
                audio = r.listen(source, timeout=2, phrase_time_limit=1)
            wake_word = r.recognize_google(audio).lower()
            print(f"Heard: {wake_word}")

            if wake_word == "hey buddy":
                # Speak on a separate thread to avoid blocking main thread
                t = threading.Thread(target=speak, args=("yes Sanket sir",))
                t.start()
                t.join()  # Wait for speaking to finish before listening

                # After speech done, listen for command
                listen_for_command()

        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()

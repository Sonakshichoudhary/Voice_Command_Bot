import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import os
import commands

# Initialize the recognizer and speaker
listener = sr.Recognizer()
engine = pyttsx3.init()
engine.setProperty("rate", 150)

def talk(text):
    print(f"Bot: {text}")
    engine.say(text)
    engine.runAndWait()

def listen_command():
    try:
        with sr.Microphone() as source:
            print("Listening...")
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            print(f"You said: {command}")
            return command
    except sr.UnknownValueError:
        talk("Sorry, I didn't catch that.")
        return ""
    except Exception as e:
        talk("An error occurred.")
        print(e)
        return ""

def run_bot():
    talk("Hello! I'm your voice assistant. How can I help you?")
    while True:
        command = listen_command()

        if "time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            talk(f"The current time is {now}")

        elif "open youtube" in command:
            talk("Opening YouTube")
            webbrowser.open("https://www.youtube.com")

        elif "search for" in command:
            search_query = command.replace("search for", "").strip()
            url = f"https://www.google.com/search?q={search_query}"
            talk(f"Searching Google for {search_query}")
            webbrowser.open(url)

        elif "open chrome" in command:
            talk("Opening Chrome")
            commands.open_chrome()

        elif "play music" in command:
            talk("Playing music")
            commands.play_music()

        elif "shutdown" in command:
            talk("Are you sure you want to shutdown? Say yes to confirm.")
            confirmation = listen_command()
            if "yes" in confirmation:
                talk("Shutting down system")
                commands.shutdown()

        elif "exit" in command or "stop" in command:
            talk("Goodbye!")
            break

        else:
            talk("Sorry, I can't do that yet.")

if __name__ == "__main__":
    run_bot()

import os
import platform
import webbrowser

def open_chrome():
    system = platform.system()
    if system == "Windows":
        os.system("start chrome")
    elif system == "Darwin":
        os.system("open -a 'Google Chrome'")
    elif system == "Linux":
        os.system("google-chrome")
    else:
        print("Unsupported OS")

def play_music():
    music_path = os.path.expanduser("~/Music")
    os.system(f'xdg-open "{music_path}"' if platform.system() == "Linux" else f'start "" "{music_path}"')

def shutdown():
    system = platform.system()
    if system == "Windows":
        os.system("shutdown /s /t 1")
    elif system == "Linux" or system == "Darwin":
        os.system("shutdown now")

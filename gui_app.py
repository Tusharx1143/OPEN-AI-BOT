import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import threading
import speech_recognition as sr
from time import sleep
import os

# Initialize speech recognition engine
recognizer = sr.Recognizer()

def TakeCommand():
    with sr.Microphone() as source:
        print(": Listening....")
        recognizer.pause_threshold = 1
        audio = recognizer.listen(source)

    try:
        print(": Recognizing...")
        query = recognizer.recognize_google(audio, language='en-in')
        print(f": Your Command : {query}\n")
        return query.lower()
    except:
        return ""

def start_bot():
    text_box.delete("1.0", tk.END)
    text_box.insert(tk.END, "Welcome to Smart Bot!\n")
    os.system("start cmd /k python main.py")

def start_listening():
    while True:
        query = TakeCommand()
        text_box.insert(tk.END, f"User: {query}\n")
        if 'shutdown' in query.lower():
            text_box.insert(tk.END, "Smart Bot: Goodbye!\n")
            break
        elif 'go offline' in query.lower():
            text_box.insert(tk.END, "Smart Bot: Going offline!\n")
            break
        text_box.see(tk.END)
        sleep(0.5)

root = tk.Tk()
root.title("Smart Bot GUI")

# Create ScrolledText widget for conversation display
text_box = ScrolledText(root, wrap=tk.WORD, height=20, width=60)
text_box.pack(pady=10)

# Create thread to start the bot
threading.Thread(target=start_bot).start()

# Create thread to listen for voice commands
threading.Thread(target=start_listening).start()

root.mainloop()

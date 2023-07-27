import speech_recognition as sr
import os
import webbrowser
import openai 
import datetime
import pyttsx3  # Import the pyttsx3 library for text-to-speech on Windows

from config import apikey

chatStr = ""

def chat(query):
    global chatStr
    print(chatStr)
    openai.api_key = apikey
    chatStr += f"Tushar: {query}\n Smart BOT: "
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt= chatStr,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    speak(response["choices"][0]["text"])  # Use the 'speak' function to convert text to speech
    chatStr += f"{response['choices'][0]['text']}\n"
    return response["choices"][0]["text"]

def ai(prompt):
    openai.api_key = apikey
    text = f"OpenAI response for Prompt: {prompt} \n *************************\n\n"

    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    # todo: Wrap this inside of a  try catch block
    # print(response["choices"][0]["text"])
    text += response["choices"][0]["text"]
    if not os.path.exists("Openai"):
        os.mkdir("Openai")

    # with open(f"Openai/prompt- {random.randint(1, 2343434356)}", "w") as f:
    with open(f"Openai/{''.join(prompt.split('gpt')[1:]).strip()}.txt", "w") as f:
        f.write(text)

def speak(text):
    engine = pyttsx3.init()  # Initialize the text-to-speech engine
    engine.say(text)  # Convert the given text to speech
    engine.runAndWait()  # Wait for the speech to complete before proceeding

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        # r.pause_threshold =  0.6
        audio = r.listen(source)
        try:
            print("Recognizing...")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query
        except Exception as e:
            return "Some Error Occurred. Sorry from Smart BOT"

if __name__ == '__main__':
    print('Welcome to Smart BOT')
    speak("Smart BOT, here for help")
    while True:
        print("Listening...")
        query = takeCommand().lower()

        if "open youtube" in query:
            speak("Opening YouTube, sir...")
            webbrowser.open("https://www.youtube.com")

        elif "open wikipedia" in query:
            speak("Opening Wikipedia, sir...")
            webbrowser.open("https://www.wikipedia.com")

        elif "open google" in query:
            speak("Opening Google, sir...")
            webbrowser.open("https://www.google.com")

        elif "open music" in query:
            musicPath = ""  # Replace with the path to your music directory
            os.system(f"open {musicPath}")

        elif "the time" in query:
            hour = datetime.datetime.now().strftime("%H")
            min = datetime.datetime.now().strftime("%M")
            speak(f"Sir, the time is {hour} bajke {min} minutes")

        elif "using gpt" in query:
            ai(prompt=query)

        elif "shutdown" in query:
            speak("As you say")
            exit()

        elif "reset chat" in query:
            chatStr = ""

        else:
            print("Chatting...")
            chat(query)

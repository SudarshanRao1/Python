import speech_recognition as sr
import webbrowser
import pyttsx3
import time
import musiclibrary
import requests
from google import genai
from google.genai import types
#from gtts import gTTS
import edge_tts
import asyncio
import pygame
import os
import sys

if sys.platform == "win32":
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

recognizer = sr.Recognizer()

newsapi = "API_KEY"

client = genai.Client(api_key="API_KEY")

SYSTEM_PROMPT = """ You are Jarvis, an intelligent AI voice assistant.
     Rules:
                        - Address the user as "Sir".
                        - Keep responses short and natural.
                        - Answer any question clearly.
                        - Do not use Markdown.
                        - Be polite and helpful.
                                                """

async def speak_async(text):
   

    voice = "en-GB-RyanNeural"
    communicate = edge_tts.Communicate(text,voice)
    await communicate.save("temp.mp3")

    pygame.mixer.init()
    pygame.mixer.music.load("temp.mp3")
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    pygame.mixer.music.unload()
    os.remove("temp.mp3")

    ''' tts = gTTS('hello')
    tts.save('temp.mp3')

    pygame.mixer.init()
    pygame.mixer.music.load('temp.mp3')
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy():
        pygame.time.Clock().tick(10)
    
    pygame.mixer.music.unload()
    os.remove("temp.mp3")'''


def speak(text):

    asyncio.run(speak_async(text))

    # engine = pyttsx3.init(driverName="sapi5")
    # engine.say(text)
    # engine.runAndWait()
    # engine.stop()



def ai_process(command):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=command,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        return response.text

    except Exception as e:
        print("Gemini Error:", e)
        return "Sorry Sir, I am unable to contact Gemini right now."
                     
 
#    print(response.text)

def processcommand(c):

   # print(c)
    if "open google" in c.lower():
        webbrowser.open("https://google.com")
    elif "open whatsapp" in c.lower():
        webbrowser.open("https://web.whatsapp.com")
    elif "open linkedin" in c.lower():
        webbrowser.open("https://linkedin.com")
    elif "open youtube" in c.lower():
        webbrowser.open("https://youtube.com")
    elif c.lower().startswith("play"):
        song = c.lower().replace("play", "").strip()

        link = musiclibrary.music.get(song)

        if link:
            webbrowser.open(link)
        else:
            speak("Sorry, I couldn't find that song.")

    elif "news" in c.lower():
        r = requests.get(f"https://newsapi.org/v2/everything?q=india&language=en&sortBy=publishedAt&apiKey={newsapi}", timeout=10)
        print(r.status_code)
        print(r.text)

        if r.status_code == 200:
            data = r.json()
            articles = data.get('articles', [])

            for article in articles[:5]:
                speak(article['title'])
    elif "open telegram" in c.lower():
        webbrowser.open("https://web.telegram.org/k/")

    elif "open spotify" in c.lower():
        webbrowser.open("https://open.spotify.com/")        
   
    else:
        output = ai_process(c)
        print(output)
        speak(output)

    
if __name__ == "__main__":
    speak("Initializing Jarvis.....")
    # listen for the wake word jarvis
    while True:
        r = sr.Recognizer()

        # recognize speech using google

        print("Recognizing......")
        try:
            r = sr.Recognizer()
            with sr.Microphone() as source:
                print("Listening......")
                audio = r.listen(source)
            word = r.recognize_google(audio)
            
            #print(word)
            if "jarvis" in word.lower():
                #print("Wake word detected!")
                speak("yes sir!")
                #print("Finished speaking!")
                # for Listening the command
                with sr.Microphone() as source:
                    print("Jarvis Active")
                    audio = r.listen(source)
                    command = r.recognize_google(audio)
                    print(f"Command Heard:{command}")
                    processcommand(command)
        except Exception as e:
            print("Error; {0}".format(e))

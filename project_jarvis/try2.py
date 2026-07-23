import pyttsx3
import time

engine = pyttsx3.init()

print("1")
engine.say("Initializing Jarvis")
engine.runAndWait()

time.sleep(2)

print("2")
engine.say("Yes sir")
engine.runAndWait()

print("Done")
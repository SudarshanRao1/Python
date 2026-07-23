import pyttsx3
import time

engine = pyttsx3.init(driverName="sapi5")

engine.say("Initializing Jarvis")
engine.runAndWait()

print("First done")

time.sleep(2)

engine = pyttsx3.init(driverName="sapi5")

engine.say("Yes sir")
engine.runAndWait()

print("Second done")
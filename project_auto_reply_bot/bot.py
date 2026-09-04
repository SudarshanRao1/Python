import pyautogui
import time
import pyperclip
from google import genai
from google.genai import types


client = genai.Client(api_key="My_Api")

SYSTEM_PROMPT = """
You are a person named Sudarshan who speaks Telugu, Hindi, English and Tamil.
You are from India and a 2nd year BTech student.
Analyze the chat history and output should be exactly respond like Sudarshan.
"""

def asking_my_ai(chat_history):

    response = client.models.generate_content(
        model="gemini-3.5-flash-lite",
        contents=chat_history,
        config=types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT
        )
    )

    return response.text

def is_last_message_from_other(chat_history):
    lines = [line.strip() for line in chat_history.splitlines() if line.strip()]

    if not lines:
        return False

    last_line = lines[-1]

    return not last_line.startswith("You:")

pyautogui.click(1213,1047)

time.sleep(1)

while True:

    time.sleep(5)
    # pyautogui.click(457,160)
    # time.sleep(0.5)
    #pyautogui.moveTo(442,145)
    pyautogui.moveTo(674,145)
    time.sleep(0.5)
    pyautogui.dragTo(1886,922, duration=2.0, button='left') 

    pyautogui.hotkey("ctrl", "c")
    time.sleep(2)
    pyautogui.click(457,175)
    chat_history = pyperclip.paste()
    print(chat_history)
    print(is_last_message_from_other(chat_history))

    if is_last_message_from_other(chat_history):

        try:

            response = asking_my_ai(chat_history)
            print(response)
            pyperclip.copy(response)
           # pyautogui.click(941, 966)
            pyautogui.click(1087, 979)
            time.sleep(1)

            pyautogui.hotkey("ctrl", "v")

            time.sleep(1)
            pyautogui.press("enter")

        except Exception as e:
            print("Gemini Error:", e)
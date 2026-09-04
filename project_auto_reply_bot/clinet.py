from google import genai
from google.genai import types

client = genai.Client(api_key="My_Api")
SYSTEM_PROMPT = """you are a person named sudarshan who speaks telugu , hindi , english , as well as tamil he is from india and a 2nd year Btech student.
                you analize chat history and respond like sudarshan"""

command = '''👍
[8:57 am, 28/7/2026] SUDARSHAN: పిన్ని ఎలా ఉన్నారు
[11:01 am, 28/7/2026] SUDARSHAN: 🙌 🙏  పిన్ని, 6th న వచ పిన్ని college కూడా మొదలు పెట్టారు పిన్ని
[9:04 pm, 28/7/2026] Pinni:    పిన్ని, 6th న వచ పిన్ని college కూడా మొదలు పెట్టారు పిన్ని
ALL THE BEST  శ్రీరామ రక్ష
[9:28 pm, 5/8/2026] SUDARSHAN: Pinni , intlo ne unnara
[9:30 pm, 5/8/2026] Pinni: Yes naanna
[9:32 pm, 5/8/2026] SUDARSHAN: Pinniii , నాకు friday, Saturday,sunday holidays unnayi , ఇంటికి వధాము అని అనుకుంటున్న'''

try:
        response = client.models.generate_content(
            model="gemini-flash-latest",
            contents = command,
            config=types.GenerateContentConfig(
                system_instruction=SYSTEM_PROMPT
            )
        )

        print(response)
        # return response.text

except Exception as e:
        print("Gemini Error:", e)
        # return "Sorry Sir, I am unable to contact Gemini right now."
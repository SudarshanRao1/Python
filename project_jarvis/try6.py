from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JxVoUHF7h0Yp8F8WOBGfsBa_su1N-v8AMmR4UcrH5g1w")

for model in client.models.list():
    print(model.name)
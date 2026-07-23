from google import genai

client = genai.Client(api_key="AQ.Ab8RN6JxVoUHF7h0Yp8F8WOBGfsBa_su1N-v8AMmR4UcrH5g1w")

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="what is coding?"
)

print(response.text)
import requests

newsapi = "YOUR_API_KEY"

r = requests.get(
    f"https://newsapi.org/v2/top-headlines?country=in&apiKey={newsapi}"
)

print(r.status_code)
print(r.json())


#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"
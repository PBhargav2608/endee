from google import genai

client = genai.Client(api_key="AIzaSyDCxi1qD2ENBhZFB0mAVPKkxoTpZD6IeRs")

response = client.models.generate_content(
    model="gemini-1.5-flash-latest",
    contents="Say hello"
)

print(response.text)

#AIzaSyAZ3BpfbvioH5EHQrtD0DYbLkdsipDf1Ak
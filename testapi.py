from google import genai
from config import GOOGLE_API_KEY

client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="Say Hello"
)

print(response.text)
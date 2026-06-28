import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

if not GOOGLE_API_KEY:
    raise ValueError(
        "GOOGLE_API_KEY not found. Please create a .env file."
    )

MODEL_NAME = "gemini-2.5-flash"
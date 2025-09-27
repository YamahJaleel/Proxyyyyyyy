from fastapi import FastAPI, Request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_URL = "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"
API_KEY = os.getenv("GEMINI_API_KEY")

app = FastAPI()

@app.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_message = body.get("message", "")

    payload = {
        "contents": [
            {"parts": [{"text": user_message}]}
        ]
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(f"{API_URL}?key={API_KEY}", json=payload, headers=headers)
    data = response.json()

    try:
        reply = data["candidates"][0]["content"]["parts"][0]["text"]
    except Exception:
        reply = "Sorry, I couldn't generate a response."

    return {"reply": reply}

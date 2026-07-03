from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ResearchRequest(BaseModel):
    prompt: str = Field(..., min_length = 5, max_length = 150, description = "Character range in user input")
    temperature: float = Field(default = 0.7, ge = 0, le = 1, description="Creativity range for research model")
    max_tokens: int = Field(default = 50, gt = 0, le = 100, description = "Max tokens user can utilize")

@app.post("/generate")
async def generate_text(request, ResearchRequest):
    return{"status": "success", "received": request.prompt}

# API Integration
from openai import OpenAI
import json 

client = OpenAI()

response = client.chat.completions.create(
    model = 'gpt-4o-mini',
    messages = [
        {
            "role":"system",
            "content": 'You are a helpful research assistant tasked with gaining insightful and accurate data on the user's prompt',
            "content": "Use valid JSON ONLY."
        },
        {
        "role": "user",
        "content":"Research the basics of German"
        },
    ]
)
        

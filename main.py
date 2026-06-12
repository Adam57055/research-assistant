from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class ResearchRequest(BaseModel):
    prompt: str = Field(..., min_length = 5, max_length = 150, description = "Character range in user input")
    temperature: float = Field(default = 0.7, ge = 0, le = 1, description="Creativity range for research model")
    max_tokens: int = Field(default = 50, gt = 0, le = 100, description = "Max tokens user can utilize")



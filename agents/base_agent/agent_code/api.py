from agent_code.memory import MemoryManager
from agent_code.utils import log
from fastapi import FastAPI
from typing import List, Optional
from pydantic import BaseModel
import time
import asyncio
import json
from starlette.responses import StreamingResponse

class ChatMessage(BaseModel):
    role: str
    content: str

class ChatCompletionRequest(BaseModel):
    model: str = "mock-gpt-model"
    messages: List[ChatMessage]
    max_tokens: Optional[int] = 512
    temperature: Optional[float] = 0.1
    stream: Optional[bool] = False

async def _resp_async_generator(text_resp: str):
    tokens = text_resp.split(" ")

    for i, token in enumerate(tokens):
        chunk = {
            "id": i,
            "object": "chat.completion.chunk",
            "created": time.time(),
            "model": "blah",
            "choices": [{"delta": {"content": token + " "}}],
        }
        yield f"data: {json.dumps(chunk)}nn"
        await asyncio.sleep(1)
    yield "data: [DONE]nn"

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/chat/completions")
async def chat_completions(request: ChatCompletionRequest):

    if request.messages:
        resp_content = "As a mock AI Assistant, I can only echo your last message: " + request.messages[-1].content
    else:
        resp_content = "As a mock AI Assistant, I can only echo your last message, but there wasn't one!"
    
    if request.stream:
        return StreamingResponse(_resp_async_generator(resp_content), media_type="application/x-ndjson")

    return {
        "id": "1337",
        "object": "chat.completion",
        "created": time.time(),
        "model": request.model,
        "choices": [{
            "message": ChatMessage(role="assistant", content=resp_content)
        }]
    }

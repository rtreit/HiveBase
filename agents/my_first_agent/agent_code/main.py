# Import base-agent's utilities
from base_agent.agent_code.api import app  # Shared FastAPI app
from base_agent.agent_code.memory import MemoryManager  # Shared memory module
from base_agent.agent_code.utils import log  # Logging utilities
from fastapi import APIRouter

router = APIRouter()
memory = MemoryManager()

# Define agent-specific behavior
@router.get("/status")
def agent_status():
    log("Checking agent status")
    return {"status": "active", "memory_usage": memory.get_usage()}

# Register agent-specific routes with the FastAPI app
app.include_router(router, prefix="/agent")

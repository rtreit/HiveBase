from fastapi import FastAPI
from agent_code.memory import MemoryManager
from agent_code.utils import log

app = FastAPI()

# Memory manager instance
memory = MemoryManager()

@app.get("/health")
def health_check():
    log("Health check endpoint accessed.")
    return {"status": "healthy"}

@app.post("/execute")
def execute_task(task: dict):
    log(f"Received task: {task}")
    # Example: Use memory for task-specific context
    memory.store("last_task", task)
    return {"result": f"Task executed: {task}"}

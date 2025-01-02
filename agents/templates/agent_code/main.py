from fastapi import FastAPI

app = FastAPI()

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/execute")
def execute_task(task: dict):
    # Replace this with your agent's logic
    return {"result": f"Task executed: {task}"}

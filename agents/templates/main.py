from agent_code.main import app  # Import the FastAPI app from agent_code

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

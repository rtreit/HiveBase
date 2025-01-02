# Base image for Python
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy agent code
COPY agent_code/ /app/agent_code

# Expose the default API port
EXPOSE 8000

# Command to start the API server
CMD ["uvicorn", "agent_code.main:app", "--host", "0.0.0.0", "--port", "8000"]

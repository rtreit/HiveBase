# Base build stage
FROM python:3.11-slim AS builder

WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Final lightweight image
FROM python:3.11-slim

WORKDIR /app

# Create a non-root user
RUN groupadd -r agent && useradd -r -g agent agent

# Copy installed dependencies from the builder stage
COPY --from=builder /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages
COPY --from=builder /usr/local/bin /usr/local/bin

# Copy agent code
COPY agent_code/ /app/agent_code

# Set non-root user
USER agent

# Expose the default API port
EXPOSE 8000

# Start the API server using Gunicorn
CMD ["gunicorn", "-k", "uvicorn.workers.UvicornWorker", "-w", "4", "-b", "0.0.0.0:8000", "agent_code.api:app"]

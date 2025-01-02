# Start from the base agent image
FROM hivebase/base-agent:latest

# Set the working directory
WORKDIR /app

# Copy agent-specific code (this is a placeholder directory in the scaffold)
COPY agent_code/ /app/agent_code

# Optional: Copy custom requirements for additional dependencies
# Uncomment if your agent needs extra libraries beyond the base
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# Optional: Add configuration files
# COPY config/ /app/config

# Expose the default API port
EXPOSE 8000

# Default command to run the agent
CMD ["uvicorn", "agent_code.main:app", "--host", "0.0.0.0", "--port", "8000"]

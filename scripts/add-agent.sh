#!/bin/bash

# Exit immediately if a command exits with a non-zero status
set -e

# Check if agent name is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <agent-name>"
    exit 1
fi

AGENT_NAME=$1
BASE_DIR=$(dirname "$(dirname "$(realpath "$0")")")  # Get the base directory of the project
TEMPLATE_DIR="$BASE_DIR/agents/templates"
NEW_AGENT_DIR="$BASE_DIR/agents/$AGENT_NAME"

# Check if the new agent directory already exists
if [ -d "$NEW_AGENT_DIR" ]; then
    echo "Error: Agent '$AGENT_NAME' already exists in $NEW_AGENT_DIR"
    exit 1
fi

# Copy the template directory to create the new agent
echo "Creating new agent '$AGENT_NAME'..."
cp -r "$TEMPLATE_DIR" "$NEW_AGENT_DIR"

# Rename placeholder files (if necessary)
echo "Customizing files for '$AGENT_NAME'..."
mv "$NEW_AGENT_DIR/agent_code/main.py" "$NEW_AGENT_DIR/agent_code/${AGENT_NAME}_main.py"

# Update the Dockerfile to reflect the new agent code file
sed -i "s/agent_code\.main/agent_code.${AGENT_NAME}_main/g" "$NEW_AGENT_DIR/Dockerfile"

# Provide feedback
echo "Agent '$AGENT_NAME' created successfully!"
echo "You can find it in $NEW_AGENT_DIR"
echo "Next steps:"
echo "  1. Modify the agent logic in $NEW_AGENT_DIR/agent_code/${AGENT_NAME}_main.py"
echo "  2. Build the Docker image with:"
echo "      docker build -t hivebase/$AGENT_NAME:latest $NEW_AGENT_DIR"
echo "  3. Add your agent to the Helm chart for deployment."

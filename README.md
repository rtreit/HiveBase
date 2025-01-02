# HiveBase

HiveBase is meant to serve as a "base" for building a multi-agent AI system on Kubernetes which supports multiple agents working together to achieve a goal.

## Principles

* **Kubernetes Namespace Isolation**
  * The system runs within a Kubernetes namespace.
  * Deploying into a different namespace creates a separate instance of the agent "community."

* **Agent Community Collaboration**
  * Each agent is part of a community of other agents who can work together to solve tasks collaboratively.

* **Agent Containerization and API Contract**
  * Agents are containers adhering to a shared API contract.
  * Individual agents can be written in any programming language.

* **Agent Memory and Context**
  * Each agent maintains its own long-term and short-term memory.
  * Agents have domain-specific Retrieval-Augmented Generation (RAG) contexts for task-specific data.

* **Vector Database Integration**
  * RAG and memory are powered by a vector database for efficient storage and retrieval.

* **Framework Agnosticism**
  * HiveBase is designed to be framework-agnostic, enabling users to experiment with different agentic frameworks and configurations seamlessly.

## Creating a New Agent from the Base Agent

HiveBase provides a streamlined process for creating new agents using the base agent template. Follow these steps:

### 1. Run the `add-agent.sh` Script
Navigate to the `scripts` directory and run the following command, replacing `<agent-name>` with your desired agent name:

```bash
./scripts/add-agent.sh <agent-name>
```

This will create a new directory under `agents/` with the necessary scaffold for your new agent.

### 2. Customize the Agent Code
Edit the generated `agent_code/<agent-name>_main.py` file to define your agent’s specific functionality. Use the provided base-agent utilities (e.g., `MemoryManager`) as needed.

### 3. Build the Agent Docker Image
Build the Docker image for your new agent:

```bash
docker build -t hivebase/<agent-name>:latest ./agents/<agent-name>
```

### 4. Test the New Agent
Run the newly built agent locally to ensure it works as expected:

```bash
docker run -p 8000:8000 hivebase/<agent-name>:latest
curl http://localhost:8000/health
```

### 5. Add the Agent to the Helm Chart
Integrate your new agent into the Helm chart for deployment. Update the necessary YAML files to include the agent in your Kubernetes deployment.

### Example Directory Structure After Adding a New Agent

```plaintext
HiveBase/
├── agents/
│   ├── base-agent/
│   │   ├── agent_code/
│   │   │   ├── main.py
│   │   │   ├── memory.py
│   │   │   └── utils.py
│   │   ├── Dockerfile
│   │   ├── __init__.py
│   │   └── requirements.txt
│   ├── math-solver/
│   │   ├── agent_code/
│   │   │   └── math-solver_main.py
│   │   └── Dockerfile
│   ├── <new-agent>/
│   │   ├── agent_code/
│   │   │   └── <new-agent>_main.py
│   │   └── Dockerfile
└── templates/
    ├── agent_code/
    │   └── main.py
    └── Dockerfile
```

This ensures consistency across all agents while allowing flexibility for customization.


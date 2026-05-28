🚀 Local AI Code Reviewer (n8n + Llama 3.1)
An autonomous, privacy-first AI agent that intercepts binary file uploads, decodes them in-memory, and executes intelligent code reviews entirely on your local machine.

🧠 Overview
This project orchestrates a completely local LLM (Llama 3.1) using n8n. By utilizing n8n's Advanced AI framework and native JavaScript buffers, the agent dynamically parses uploaded code files (e.g., Python, JavaScript) straight from the chat UI without relying on external APIs, fragile HTTP parameter parsing, or rigid disk-path validations.

It is designed to be a secure, offline alternative for analyzing proprietary code or sensitive scripts (such as threat-detection microservices).

✨ Key Features
100% Local & Private: Runs entirely on local Docker containers. Zero data leaves your machine.

Direct File Ingestion: Drag-and-drop code files directly into the n8n chat interface.

In-Memory Decoding: Bypasses standard filesystem restrictions by natively decoding base64 binary streams within n8n's Custom Code execution environment.

Zero-Parameter LLM Abstraction: Eliminates 422 Unprocessable Entity formatting bugs common with smaller open-source models by strictly structuring the input schema.

🏗️ Architecture
Orchestrator: n8n (Self-Hosted via Docker)

LLM Engine: Ollama (Llama 3.1 8B)

Integration: n8n AI Agent Node -> Custom Code Tool (JavaScript)

Data Flow: Chat Trigger (Binary File) -> Buffer Stream -> UTF-8 String Extraction -> LLM Context Window -> Markdown Response

⚙️ Prerequisites
Docker and Docker Compose

Basic familiarity with n8n interfaces

🚀 Setup & Installation
1. Clone the repository:

Bash
git clone https://github.com/MuhammadSahal/n8n-local-ai-agent.git
cd n8n-local-ai-agent
2. Spin up the infrastructure:
Ensure your Docker daemon is running, then launch the stack:

Bash
docker compose up -d
3. Pull the Local Model:
Once the containers are up, download the Llama 3.1 weights into the Ollama container:

Bash
docker exec -it ollama ollama run llama3.1
4. Import the Agent Workflow:

Open http://localhost:5678 in your browser.

Navigate to Workflows -> Add Workflow -> Import from File.

Select the local-ai-code-reviewer.json file included in this repository.

Ensure the Ollama Chat Model node is authenticated with the base URL: http://ollama:11434.

💻 Usage
Open the imported workflow and click Open Chat in the bottom right corner.

Click the Paperclip Icon to upload a code file (e.g., server.py).

Send a prompt, such as: "Review this code for performance optimizations."

The AI will instantly decode the file and stream back a comprehensive, markdown-formatted code review.

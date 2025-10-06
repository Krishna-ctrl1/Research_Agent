Autonomous AI Research Agent
An autonomous AI agent built with LangChain, LangGraph, and Ollama. This project receives a research topic, autonomously creates a plan, searches the web, and writes a comprehensive report. The entire agent is served via a production-ready FastAPI backend, containerized with Docker, and configured for automated deployment to AWS.

🚀 Key Features
Autonomous Multi-Step Research: The agent can plan, search, critique, and write without human intervention.

Stateful Agentic Workflow: Built using LangGraph to enable complex, cyclical workflows for tasks like self-correction and planning.

Powered by Local LLMs: Natively integrated with Ollama to run powerful open-source models like Llama 3 directly on your machine.

Production-Ready API: A robust and scalable API built with FastAPI, including automatic interactive documentation.

Containerized & Portable: Comes with a Dockerfile to ensure a consistent and reproducible environment anywhere.

MLOps Ready: Includes a CI/CD pipeline definition using GitHub Actions for automated building and deployment to AWS App Runner.

🛠️ Tech Stack
AI Frameworks: LangChain, LangGraph

LLM Backend: Ollama (Llama 3)

API Framework: FastAPI

Tools: DuckDuckGo Search

Containerization: Docker

CI/CD & Deployment: GitHub Actions, AWS ECR, AWS App Runner

🏗️ Project Architecture
This project uses a decoupled architecture where the agent logic is served via an API.

+----------------+      +---------------------+      +---------------------+      +----------------------+
| User / Client  |----->|   FastAPI Backend   |----->|  LangGraph Agent    |----->|  DuckDuckGo Search   |
| (e.g., Browser)|      | (api.py)            |      |  (agent.py)         |      |  (Tool)              |
+----------------+      +---------------------+      +----------+----------+      +----------------------+
                                                                 |
                                                                 |
                                                       +---------v---------+
                                                       | Ollama (Llama 3)  |
                                                       | (Local LLM)       |
                                                       +-------------------+

⚙️ Local Setup and Installation
Follow these steps to get the project running on your local machine.

1. Prerequisites
Python 3.11+

Git

Ollama

Docker Desktop (for containerization)

2. Clone the Repository
git clone [https://github.com/Krishna-ctrl1/Research_Agent.git](https://github.com/Krishna-ctrl1/Research_Agent.git)
cd Research_Agent

3. Set Up Ollama
Once Ollama is installed and running, pull the Llama 3 model.

ollama pull llama3

4. Configure Environment Variables
Create a file named .env in the project root and add your LangSmith API key for tracing.

# .env file

# Get these from your LangSmith account settings
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="PASTE_YOUR_LANGSMITH_API_KEY_HERE"

5. Install Dependencies
Install all the required Python packages.

python -m pip install -r requirements.txt

▶️ Running the Application
Local Development Server
This is the easiest way to run the application for development.

python main.py

The API server will be available at http://127.0.0.1:8000.

Testing the API
Once the server is running, you can test the agent by navigating to the interactive documentation in your browser:

URL: http://127.0.0.1:8000/docs

Expand the POST /research endpoint.

Click "Try it out", enter your topic in the request body, and click "Execute".

🐳 Docker Usage
You can also build and run the entire application as a Docker container.

Build the Docker Image
docker build -t research-agent-api .

Run the Docker Container
docker run -p 8000:8000 --env-file .env research-agent-api

The API will be accessible at the same address: http://127.0.0.1:8000.

🚀 MLOps and Deployment
This project is configured with a CI/CD pipeline for automated deployments to AWS App Runner.

The workflow is defined in .github/workflows/deploy.yml and performs the following steps on every push to the main branch:

Configure AWS Credentials: Securely logs into AWS using secrets stored in GitHub.

Login to ECR: Authenticates Docker with Amazon Elastic Container Registry.

Build & Push Image: Builds a new Docker image and pushes it to the ECR repository.

Automatic Deployment: AWS App Runner is configured to automatically detect the new image in ECR and deploy the update to the live service.

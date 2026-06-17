# 🤖 Autonomous AI Research Agent

An **autonomous AI research assistant** built with **LangChain**, **LangGraph**, and **Ollama**.  
This project takes a research topic, autonomously **creates a plan**, **searches the web**, and **writes a comprehensive report**.  
The entire system is served via a **production-ready FastAPI backend**, **containerized with Docker**, and configured for **automated deployment to AWS**.

---

## 🚀 Key Features

- **🧠 Autonomous Multi-Step Research:**  
  The agent plans, searches, critiques, and writes — fully autonomously.

- **🔁 Stateful Agentic Workflow:**  
  Built using **LangGraph** for complex, cyclical task workflows (planning, self-correction, evaluation).

- **⚡ Powered by Local LLMs:**  
  Natively integrates with **Ollama** to run open-source models like **Llama 3** directly on your local machine.

- **🧩 Production-Ready API:**  
  Robust and scalable backend built using **FastAPI**, with automatic interactive documentation.

- **🐳 Containerized & Portable:**  
  Pre-configured **Dockerfile** ensures consistent and reproducible environments.

- **🚢 MLOps Ready:**  
  Includes **GitHub Actions CI/CD pipeline** for automated build and deployment to **AWS App Runner**.

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **AI Frameworks** | LangChain, LangGraph |
| **LLM Backend** | Ollama (Llama 3) |
| **API Framework** | FastAPI |
| **Search Tool** | DuckDuckGo Search |
| **Containerization** | Docker |
| **CI/CD & Deployment** | GitHub Actions, AWS ECR, AWS App Runner |

---

## 🏗️ Project Architecture

```text
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
```

## ⚙️ Local Setup and Installation

### 1️⃣ Prerequisites
Make sure you have the following installed:

- **Python 3.11+**  
- **Git**  
- **Ollama**  
- **Docker Desktop**

---

### 2️⃣ Clone the Repository
```bash
git clone https://github.com/Krishna-ctrl1/Research_Agent.git
cd Research_Agent
```

### 3️⃣ Set Up Ollama

Once Ollama is installed and running, pull the **Llama 3** model:

```bash
ollama pull llama3
```

### 4️⃣ Configure Environment Variables

Create a .env file in the project root:
```bash
# .env file

# Get these from your LangSmith account settings
LANGCHAIN_TRACING_V2="true"
LANGCHAIN_API_KEY="PASTE_YOUR_LANGSMITH_API_KEY_HERE"
```

### 5️⃣ Install Dependencies
```bash
python -m pip install -r requirements.txt
```

## ▶️ Running the Application

### 🧩 Local Development Server

Run the application locally using the following command:

```bash
python main.py
```
**Once started, the API will be available at:**
**👉 http://127.0.0.1:8000**


## 🧪 Test the API

Visit the interactive documentation:  
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

### Steps:
1. Expand the **POST /research** endpoint  
2. Click **“Try it out”**  
3. Enter your research topic  
4. Click **“Execute”**  

## 🐳 Docker Usage

### Build the Docker Image
Build the Docker image using the following command:  
`docker build -t research-agent-api .`

### Run the Docker Container
Run the container with:  
`docker run -p 8000:8000 --env-file .env research-agent-api`

The API will be available at:  
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 🚀 MLOps & Deployment (AWS)

This project includes a **CI/CD pipeline** configured for automated deployments using **GitHub Actions** and **AWS App Runner**.

The workflow file is located at:  
`.github/workflows/deploy.yml`

### 🔄 CI/CD Workflow Steps

1. **Configure AWS Credentials:**  
   Authenticates using GitHub Secrets.

2. **Login to ECR:**  
   Authenticates Docker with Amazon Elastic Container Registry (ECR).

3. **Build & Push Image:**  
   Builds and pushes the new Docker image to AWS ECR.

4. **Automatic Deployment:**  
   AWS App Runner automatically detects the new image and deploys it to the live environment.

---

## 🧠 Future Enhancements

- Add support for **multi-agent collaboration**  
- Integrate **vector databases** (e.g., Chroma, FAISS) for memory  
- Extend **report export formats** (PDF, DOCX)  
- Introduce a **voice interaction module**

---

## 📜 License

This project is licensed under the **MIT License** — feel free to use and modify it.

---

# 🏥 Medical Chatbot

An intelligent medical chatbot powered by **LLMs** and **LangChain**, enhanced with vector embeddings via **Pinecone** and deployed using **Flask** and **AWS**.

---

## 📋 Table of Contents

- [Features](#-features)
- [Tech Stack](#-tech-stack)
- [Prerequisites](#-prerequisites)
- [Installation](#-installation)
- [Configuration](#-configuration)
- [Running Locally](#-running-locally)
- [AWS Deployment](#-aws-deployment)
- [Project Structure](#-project-structure)
- [API Documentation](#-api-documentation)
- [Contributing](#-contributing)
- [License](#-license)

---

## ✨ Features

- 🤖 AI-powered medical consultation chatbot
- 🔍 Vector-based semantic search with Pinecone
- 🚀 Fast inference with LLM integration
- 🌐 Flask web interface
- 🐳 Docker containerization
- ☁️ AWS deployment with CI/CD (GitHub Actions)
- 📊 Scalable architecture with EC2 & ECR

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| **LLM** | GPT (OpenAI) |
| **RAG Framework** | LangChain |
| **Vector Database** | Pinecone |
| **Web Framework** | Flask |
| **Language** | Python 3.10 |
| **Containerization** | Docker |
| **Cloud Provider** | AWS (EC2, ECR) |
| **CI/CD** | GitHub Actions |

---

## 📦 Prerequisites

Before you begin, ensure you have the following installed:

- **Python 3.10** or higher
- **Conda** (recommended) or **pip**
- **Git**
- **Docker** (for containerization)

### Required API Keys

- [OpenAI API Key](https://platform.openai.com/api-keys)
- [Pinecone API Key](https://www.pinecone.io/)

---

## 🚀 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/kirankarakalli/Medical-Chatbot.git
cd Medical-Chatbot
```

### 2. Create a Virtual Environment

Using Conda (recommended):

```bash
conda create -n medibot python=3.10 -y
conda activate medibot
```

Or using venv:

```bash
python -m venv medibot
source medibot/bin/activate  # On Windows: medibot\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 🔑 Configuration

### 1. Create a `.env` File

In the root directory, create a `.env` file with your API credentials:

```ini
PINECONE_API_KEY=your_pinecone_api_key_here
OPENAI_API_KEY=your_openai_api_key_here
```

**Tip:** Copy and modify the `.env.example` file:

```bash
cp .env.example .env
```

---

## 💻 Running Locally

### 1. Initialize Vector Store

Store your medical document embeddings in Pinecone:

```bash
python store_index.py
```

This script:
- Loads medical documents from `data/medical_documents/`
- Generates embeddings using OpenAI
- Stores them in your Pinecone index

### 2. Start the Flask Application

```bash
python app.py
```

### 3. Access the Chatbot

Open your browser and navigate to:

```
http://localhost:5000
```

---

## ☁️ AWS Deployment

### Step 1: AWS Console Setup

1. Log in to your AWS console
2. Create an **IAM user** for deployment with these permissions:
   - **EC2 Access** (manage virtual machines)
   - **ECR Full Access** (manage container registry)

### Step 2: Create Required AWS Resources

#### Create ECR Repository

```bash
# Store this URI for later use
# Example: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot
```

#### Launch EC2 Instance

1. Create an **Ubuntu EC2 instance**
2. Allocate sufficient resources (t2.medium or higher recommended)

### Step 3: Install Docker on EC2

SSH into your EC2 instance and run:

```bash
# Update system packages
sudo apt-get update -y
sudo apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

# Add ubuntu user to docker group
sudo usermod -aG docker ubuntu
newgrp docker
```

### Step 4: Configure GitHub Actions Runner

1. Go to **Repository Settings → Actions → Runners**
2. Click **New self-hosted runner**
3. Select your OS (Linux)
4. Execute the provided commands on your EC2 instance

### Step 5: Add GitHub Secrets

In **Repository Settings → Secrets and Variables → Actions**, add:

| Secret Name | Value |
|------------|-------|
| `AWS_ACCESS_KEY_ID` | Your IAM access key |
| `AWS_SECRET_ACCESS_KEY` | Your IAM secret key |
| `AWS_DEFAULT_REGION` | e.g., `us-east-1` |
| `ECR_REPO` | Your ECR repository URI |
| `PINECONE_API_KEY` | Your Pinecone API key |
| `OPENAI_API_KEY` | Your OpenAI API key |

### Step 6: Deploy

Push to your repository. GitHub Actions will automatically:

1. ✅ Build Docker image
2. ✅ Push to ECR
3. ✅ Deploy to EC2
4. ✅ Launch container

---

## 📁 Project Structure

```
Medical-Chatbot/
├── .github/
│   └── workflows/
│       ├── ci.yml                    # CI/CD pipeline
│       └── deploy.yml                # Deployment workflow
│
├── src/
│   ├── config/
│   │   ├── settings.py               # Configuration management
│   │   └── logging_config.py         # Logging setup
│   ├── core/
│   │   ├── embeddings.py             # Embedding generation
│   │   ├── vector_store.py           # Vector DB operations
│   │   └── chain.py                  # RAG chain setup
│   ├── api/
│   │   ├── routes.py                 # API endpoints
│   │   ├── middleware.py             # Rate limiting, auth
│   │   └── schemas.py                # Pydantic models
│   ├── services/
│   │   ├── chatbot_service.py        # Business logic
│   │   ├── cache_service.py          # Redis caching
│   │   └── monitoring_service.py     # Metrics tracking
│   ├── utils/
│   │   ├── validators.py             # Input validation
│   │   ├── exceptions.py             # Custom exceptions
│   │   └── decorators.py             # Reusable decorators
│   ├── helper.py                     # Helper utilities
│   └── prompt.py                     # Prompt templates
│
├── tests/
│   ├── unit/
│   │   ├── test_embeddings.py
│   │   ├── test_chain.py
│   │   └── test_api.py
│   ├── integration/
│   │   └── test_chatbot_flow.py
│   └── conftest.py
│
├── templates/
│   ├── chat.html                     # Chat interface
│   ├── base.html                     # Base template
│   └── admin.html                    # Admin dashboard
│
├── static/
│   ├── css/style.css
│   ├── js/chat.js
│   └── images/
│
├── data/
│   └── medical_documents/            # PDF storage
│
├── deployment/
│   ├── docker-compose.yml
│   ├── kubernetes/
│   │   ├── deployment.yaml
│   │   └── service.yaml
│   └── terraform/                    # IaC for AWS
│
├── docs/
│   ├── API.md                        # API documentation
│   ├── ARCHITECTURE.md               # System design
│   ├── DEPLOYMENT.md                 # Deployment guide
│   └── CONTRIBUTING.md               # Contributing guidelines
│
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt
├── .env.example
├── .gitignore
├── README.md
└── LICENSE
```

---

## 📚 API Documentation

See [docs/API.md](docs/API.md) for detailed API endpoints and usage examples.

### Example Request

```bash
curl -X POST http://localhost:5000/api/chat \
  -H "Content-Type: application/json" \
  -d '{
    "query": "What are the symptoms of diabetes?"
  }'
```

---

## 🐳 Docker Deployment

Build and run with Docker:

```bash
# Build image
docker build -t medical-chatbot:latest .

# Run container
docker run -p 5000:5000 \
  -e OPENAI_API_KEY=your_key \
  -e PINECONE_API_KEY=your_key \
  medical-chatbot:latest
```

Or use Docker Compose:

```bash
docker-compose up -d
```

---

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](docs/CONTRIBUTING.md) for guidelines.

### Quick Start for Contributors

```bash
# Install dev dependencies
pip install -r requirements-dev.txt

# Run tests
pytest

# Format code
black .
flake8 .
```

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 Support

For issues, questions, or suggestions:
- Open an [Issue](https://github.com/kirankarakalli/Medical-Chatbot/issues)
- Check existing [Discussions](https://github.com/kirankarakalli/Medical-Chatbot/discussions)

---

## 🙋 Author

**Kiran Karakalli**

---

**⭐ If you found this helpful, please star the repository!**

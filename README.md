# Build-a-Complete-Medical-Chatbot-with-LLMs-LangChain-Pinecone-Flask-AWS

# How to run?
### STEPS:

Clone the repository

```bash
https://github.com/kirankarakalli/Medical-Chatbot.git
```
### STEP 01- Create a conda environment after opening the repository

```bash
conda create -n medibot python=3.10 -y
```

```bash
conda activate medibot
```


### STEP 02- install the requirements
```bash
pip install -r requirements.txt
```


### Create a `.env` file in the root directory and add your Pinecone & openai credentials as follows:

```ini
PINECONE_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
OPENAI_API_KEY = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```


```bash
# run the following command to store embeddings to pinecone
python store_index.py
```

```bash
# Finally run the following command
python app.py
```

Now,
```bash
open up localhost:
```


### Techstack Used:

- Python
- LangChain
- Flask
- GPT
- Pinecone



# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment

	#with specific access

	1. EC2 access : It is virtual machine

	2. ECR: Elastic Container registry to save your docker image in aws


	#Description: About the deployment

	1. Build docker image of the source code

	2. Push your docker image to ECR

	3. Launch Your EC2 

	4. Pull Your image from ECR in EC2

	5. Lauch your docker image in EC2

	#Policy:

	1. AmazonEC2ContainerRegistryFullAccess

	2. AmazonEC2FullAccess

	
## 3. Create ECR repo to store/save docker image
    - Save the URI: 315865595366.dkr.ecr.us-east-1.amazonaws.com/medicalbot

	
## 4. Create EC2 machine (Ubuntu) 

## 5. Open EC2 and Install docker in EC2 Machine:
	
	
	#optinal

	sudo apt-get update -y

	sudo apt-get upgrade
	
	#required

	curl -fsSL https://get.docker.com -o get-docker.sh

	sudo sh get-docker.sh

	sudo usermod -aG docker ubuntu

	newgrp docker
	
# 6. Configure EC2 as self-hosted runner:
    setting>actions>runner>new self hosted runner> choose os> then run command one by one


# 7. Setup github secrets:

   - AWS_ACCESS_KEY_ID
   - AWS_SECRET_ACCESS_KEY
   - AWS_DEFAULT_REGION
   - ECR_REPO
   - PINECONE_API_KEY
   - OPENAI_API_KEY






Medical-Chatbot/
│
├── .github/
│   └── workflows/
│       ├── ci.yml                    # CI/CD pipeline
│       └── deploy.yml                # Deployment workflow
│
├── src/
│   ├── __init__.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py               # Configuration management
│   │   └── logging_config.py         # Logging setup
│   │
│   ├── core/
│   │   ├── __init__.py
│   │   ├── embeddings.py             # Embedding generation
│   │   ├── vector_store.py           # Vector DB operations
│   │   └── chain.py                  # RAG chain setup
│   │
│   ├── api/
│   │   ├── __init__.py
│   │   ├── routes.py                 # API endpoints
│   │   ├── middleware.py             # Rate limiting, auth
│   │   └── schemas.py                # Pydantic models
│   │
│   ├── services/
│   │   ├── __init__.py
│   │   ├── chatbot_service.py        # Business logic
│   │   ├── cache_service.py          # Redis caching
│   │   └── monitoring_service.py     # Metrics tracking
│   │
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── validators.py             # Input validation
│   │   ├── exceptions.py             # Custom exceptions
│   │   └── decorators.py             # Reusable decorators
│   │
│   ├── helper.py                     # Keep existing helper
│   └── prompt.py                     # Keep existing prompt
│
├── tests/
│   ├── __init__.py
│   ├── unit/
│   │   ├── test_embeddings.py
│   │   ├── test_chain.py
│   │   └── test_api.py
│   ├── integration/
│   │   └── test_chatbot_flow.py
│   └── conftest.py                   # Pytest fixtures
│
├── templates/
│   ├── chat.html                     # Enhanced UI
│   ├── base.html                     # Base template
│   └── admin.html                    # Admin dashboard
│
├── static/
│   ├── css/
│   │   └── style.css
│   ├── js/
│   │   └── chat.js                   # Frontend logic
│   └── images/
│
├── data/
│   └── medical_documents/            # PDF storage
│
├── logs/                             # Application logs
│
├── notebooks/
│   ├── data_exploration.ipynb
│   └── model_evaluation.ipynb
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
│   └── CONTRIBUTING.md               # Contribution guidelines
│
├── .env.example                      # Environment template
├── .gitignore
├── .dockerignore
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── requirements-dev.txt              # Dev dependencies
├── setup.py
├── pytest.ini                        # Pytest configuration
├── Makefile                          # Common commands
├── README.md
└── LICENSE
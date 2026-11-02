# Customer Support Agent

An AI-powered customer support API built with FastAPI, LangChain, and LangGraph. The agent handles customer inquiries, retrieves relevant e-commerce information from the Olist dataset, and validates whether queries are within its customer support scope.

## Key Features

- **AI-Powered Customer Support:** Handles customer inquiries using an LLM.
- **Agentic Workflow:** Uses LangGraph to orchestrate the agent and tool execution cycle.
- **Customer & Order Information Retrieval:** Retrieves customer, order, product, and shipping-related information from the Olist dataset.
- **Scope Validation:** Identifies and rejects queries outside the supported customer service scope.
- **Conversation Context:** Supports follow-up questions using conversation state.
- **API Integration:** Exposes the agent through a FastAPI backend.
- **LLM Observability:** Integrates LangSmith for tracing and monitoring agent execution.
- **Containerization:** Uses Docker and Docker Compose to simplify application deployment.

## Tech Stack

**Programming Language**
- Python 3.11.2

**AI & LLM**
- LangChain
- LangGraph
- OpenRouter
- GPT-4o-mini

**Backend**
- FastAPI
- Uvicorn
- Pydantic

**Data Processing**
- Pandas

**Monitoring & Observability**
- LangSmith

**Containerization**
- Docker
- Docker Compose

## Datasets

### Olist Brazilian E-Commerce Dataset

The main dataset used for customer, order, product, and shipping-related information retrieval.

Source: [Kaggle — Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Files used:

- `olist_customers_dataset.csv`
- `olist_orders_dataset.csv`
- `olist_order_items_dataset.csv`
- `olist_products_dataset.csv`
- `product_category_name_translation.csv`

### Bitext Customer Support Dataset

Used as a reference for customer support intents and instructions.

Source: [GitHub — Bitext Customer Support Dataset](https://github.com/bitext/customer-support-llm-chatbot-training-dataset)

File used:

- `Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv`

## Project Structure

```text
customer-support-agent/
├── app/
│   ├── api/
│   │   └── routes.py
│   ├── prompts/
│   ├── services/
│   │   └── chat_service.py
│   ├── data.py
│   ├── graph.py
│   ├── llm.py
│   ├── main.py
│   ├── nodes.py
│   ├── scope.py
│   ├── state.py
│   ├── tools.py
│   └── validation.py
├── data/
│   ├── olist/
│   └── bitext/
├── notebook/
├── .dockerignore
├── .env.example
├── compose.yaml
├── Dockerfile
└── requirements.txt
```

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/naufalsutrisna/customer-support-agent.git
cd customer-support-agent
```

### 2. Create a Virtual Environment

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root based on `.env.example`.

```env
OPENROUTER_API_KEY=your_openrouter_api_key

LANGSMITH_TRACING=true
LANGSMITH_API_KEY=your_langsmith_api_key
LANGSMITH_PROJECT=customer-support-agent
```

Add your API keys before running the application.

## Run Locally

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

Access the interactive API documentation at:

```text
http://127.0.0.1:8000/docs
```

## Run with Docker Compose

Make sure Docker Desktop is running and the `.env` file is configured.

Build and start the application:

```bash
docker compose up -d --build
```

Check the container status:

```bash
docker compose ps
```

View application logs:

```bash
docker compose logs -f api
```

Stop the application:

```bash
docker compose down
```

The API documentation will be available at:

```text
http://localhost:8000/docs
```

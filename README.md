# Customer Support Agent

An AI-powered customer support API built with FastAPI, LangChain, and LangGraph.

## Tech Stack

* Python 3.11.2
* FastAPI
* LangChain
* LangGraph
* Pandas
* OpenRouter

## Datasets

### Olist Brazilian E-Commerce Dataset

Main dataset for customer, order, product, and shipping-related information.

Source: [Kaggle — Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce)

Files used:

* `olist_customers_dataset.csv`
* `olist_orders_dataset.csv`
* `olist_order_items_dataset.csv`
* `olist_products_dataset.csv`
* `product_category_name_translation.csv`

### Bitext Customer Support Dataset

Used as a reference for customer support intents and instructions.

Source: [GitHub — Bitext Customer Support Dataset](https://github.com/bitext/customer-support-llm-chatbot-training-dataset)

File used:

* `Bitext_Sample_Customer_Support_Training_Dataset_27K_responses-v11.csv`

## Setup

Clone the repository:

```bash
git clone https://github.com/your-username/customer-support-agent.git
cd customer-support-agent
```

Create and activate a virtual environment:

```bash
python3.11 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file and add the required environment variables.

## Run

Start the FastAPI application:

```bash
uvicorn app.main:app --reload
```

The API will be available at:

```text
http://127.0.0.1:8000
```

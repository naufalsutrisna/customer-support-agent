import os

from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

from app.tools import (
    customer_orders,
    order_details,
    product_details,
)


load_dotenv()


llm = ChatOpenAI(
    model="openai/gpt-4o-mini",
    temperature=0,
    api_key=os.getenv("OPENROUTER_API_KEY"),
    base_url="https://openrouter.ai/api/v1",
)


tools = [
    customer_orders,
    order_details,
    product_details,
]

llm_with_tools = llm.bind_tools(tools)

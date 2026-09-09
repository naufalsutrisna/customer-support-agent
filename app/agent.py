from langchain.agents import create_agent

from app.llm import llm
from app.tools import (
    customer_orders,
    order_details,
    product_details,
)


tools = [
    customer_orders,
    order_details,
    product_details,
]


agent = create_agent(
    model=llm,
    tools=tools,
)

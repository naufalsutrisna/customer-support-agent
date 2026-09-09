from langgraph.prebuilt import ToolNode

from app.llm import llm_with_tools
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


def agent_node(state):
    response = llm_with_tools.invoke(state["messages"])

    return {
        "messages": [response]
    }


tool_node = ToolNode(tools)


def should_continue(state):
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"

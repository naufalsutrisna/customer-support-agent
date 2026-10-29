from langgraph.prebuilt import ToolNode
from langchain_core.messages import SystemMessage

from app.prompts.system import SYSTEM_PROMPT
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
    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"],
    ]

    response = llm_with_tools.invoke(messages)
    
    return {
        "messages": [response]
    }


tool_node = ToolNode(tools)


def should_continue(state):
    last_message = state["messages"][-1]

    if last_message.tool_calls:
        return "tools"

    return "end"

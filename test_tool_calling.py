from app.llm import llm_with_tools, llm
from app.tools import customer_orders
from langchain_core.messages import HumanMessage, ToolMessage


customer_unique_id = "861eff4711a542e4b93843c6dd7febb0"

messages = [
    HumanMessage(
        content=f"Show me all orders for customer {customer_unique_id}"
    )
]

response = llm_with_tools.invoke(messages)

print("Tool calls:")
print(response.tool_calls)


for tool_call in response.tool_calls:
    if tool_call["name"] == "customer_orders":
        result = customer_orders.invoke(tool_call["args"])

        messages.append(response)
        messages.append(
            ToolMessage(
                content=str(result),
                tool_call_id=tool_call["id"],
            )
        )


print("\nMessages:")
for message in messages:
    print(type(message).__name__)
    print(message.content)
    
final_response = llm.invoke(messages)

print("\nFinal response:")
print(final_response.content)

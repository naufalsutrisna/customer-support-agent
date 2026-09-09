from app.graph import graph


print(graph.get_graph().draw_mermaid())


customer_unique_id = "861eff4711a542e4b93843c6dd7febb0"

result = graph.invoke({
    "messages": [
        {
            "role": "user",
            "content": (
                f"Show me all orders for customer "
                f"{customer_unique_id}"
            ),
        }
    ]
})

print(result["messages"][-1].content)

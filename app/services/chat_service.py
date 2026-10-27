from app.graph import graph


def process_message(message: str) -> str:
    result = graph.invoke(
        {
            "messages": [
                {"role": "user", "content": message}
            ]
        }
    )

    return result["messages"][-1].content

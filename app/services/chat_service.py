
from uuid import uuid4

from app.graph import graph


# Temporary in-memory conversation storage
_conversations: dict[str, list] = {}


def process_message(message: str, conversation_id: str | None = None,) -> dict[str, str]:
    if conversation_id is None:
        conversation_id = str(uuid4())

    history = _conversations.get(conversation_id, [])

    result = graph.invoke(
        {
            "messages": [
                *history,
                {"role": "user", "content": message},
            ]
        }
    )

    messages = result["messages"]
    answer = messages[-1].content

    _conversations[conversation_id] = messages

    return {
        "conversation_id": conversation_id,
        "answer": answer,
    }

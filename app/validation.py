from langchain_core.messages import AIMessage

from app.scope import validate_scope


def scope_validation_node(state):
    user_message = state["messages"][-1].content
    result = validate_scope(user_message)

    if result.classification == "out_of_scope":
        return {
            "messages": [
                AIMessage(
                    content=(
                        "I'm sorry, but I can only help with "
                        "e-commerce customer support, such as orders "
                        "and product information."
                    )
                )
            ],
            "is_in_scope": False,
        }

    return {"is_in_scope": True}

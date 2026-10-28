from typing import NotRequired

from langgraph.graph import MessagesState


class AgentState(MessagesState):
    is_in_scope: NotRequired[bool]

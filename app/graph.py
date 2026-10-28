from langgraph.graph import StateGraph, START, END

from app.state import AgentState
from app.nodes import agent_node, tool_node, should_continue
from app.validation import scope_validation_node


graph_builder = StateGraph(AgentState)

graph_builder.add_node("validate_scope", scope_validation_node)
graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "validate_scope")


def route_scope(state):
    if state["is_in_scope"]:
        return "agent"

    return "end"


graph_builder.add_conditional_edges(
    "validate_scope",
    route_scope,
    {
        "agent": "agent",
        "end": END,
    },
)

graph_builder.add_conditional_edges(
    "agent",
    should_continue,
    {
        "tools": "tools",
        "end": END,
    },
)

graph_builder.add_edge("tools", "agent")

graph = graph_builder.compile()

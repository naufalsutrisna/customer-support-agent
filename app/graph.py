from langgraph.graph import StateGraph, START, END

from app.state import AgentState
from app.nodes import agent_node, tool_node, should_continue


graph_builder = StateGraph(AgentState)

graph_builder.add_node("agent", agent_node)
graph_builder.add_node("tools", tool_node)

graph_builder.add_edge(START, "agent")

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
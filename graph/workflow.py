from langgraph.graph import StateGraph, END, START

from graph.state import AgentState

from agents.supervisor import supervisor_agent
from agents.sql_agent import sql_agent
from agents.analytics_agent import analytics_agent
from agents.report_agent import report_agent
from langchain_core.messages import HumanMessage





def supervisor_node(state:AgentState):

    response = supervisor_agent.invoke(
        {
            "messages": [
                HumanMessage(content=state["question"])
            ]
        }
    )

    print(response)

    return {
        "next_agent": "sql"
    }


def sql_node(state:AgentState):

    response  = sql_agent.invoke(state)

    return {
        "sql_result" : response,
        "next_agent" : "supervisor"
    }

def analytics_node(state:AgentState):

    response = analytics_agent.invoke(state)

    return {

        "analytics_result" : response,
        "next_agent" : "supervisor"

    }

def report_node(state:AgentState):

    response = report_agent.invoke(state)

    return{
        "report_result" : response,
        "next_agent" : "supervisor"

    }



builder  = StateGraph(AgentState)


builder.add_node("supervisor",supervisor_node)
builder.add_node("sql",sql_node)
builder.add_node("analytics", analytics_node)
builder.add_node("report", report_node)


builder.add_edge(START, "supervisor")

builder.add_conditional_edges(
    "supervisor",
    lambda state: state["next_agent"],
    {
        "sql": "sql",
        "analytics": "analytics",
        "report": "report",
        "end": END,
    },
)


builder.add_edge("sql", "supervisor")
builder.add_edge("analytics", "supervisor")
builder.add_edge("report", "supervisor")


graph = builder.compile()


result = graph.invoke(
    {
        "question": "Which department generated the highest revenue?",
        "sql_result": None,
        "analytics_result": None,
        "report_result": None,
        "next_agent": "",
    }
)

print(result)
from typing import TypedDict, Any


class AgentState(TypedDict):

    question: str

    sql_result: Any

    analytics_result: Any

    report_result: Any

    next_agent: str
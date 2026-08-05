from typing import TypedDict


class AgentState(TypedDict):

    user_question: str

    next_agent: str

    answer: str
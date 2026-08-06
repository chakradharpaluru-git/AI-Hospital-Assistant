from typing import TypedDict, Optional, Any


class AgentState(TypedDict):

    user_question: str

    next_agent: str

    answer: Optional[Any]
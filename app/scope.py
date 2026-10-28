from typing import Literal

from pydantic import BaseModel
from langchain_core.messages import SystemMessage, HumanMessage

from app.llm import llm
from app.prompts.scope import SCOPE_VALIDATION_PROMPT


class ScopeResult(BaseModel):
    classification: Literal["in_scope", "out_of_scope"]


scope_llm = llm.with_structured_output(ScopeResult)


def validate_scope(message: str) -> ScopeResult:
    return scope_llm.invoke(
        [
            SystemMessage(content=SCOPE_VALIDATION_PROMPT),
            HumanMessage(content=message),
        ]
    )

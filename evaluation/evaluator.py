
from langchain_core.prompts import ChatPromptTemplate
from pydantic import BaseModel, Field

from app.llm import llm
from evaluation.prompt import EVALUATION_PROMPT


class EvaluationResult(BaseModel):
    correctness_score: int = Field(
        ge=1,
        le=5,
        description="Score from 1 to 5 for factual correctness.",
    )
    correctness_reason: str = Field(
        description="Explanation for the correctness score.",
    )

    groundedness_score: int = Field(
        ge=1,
        le=5,
        description="Score from 1 to 5 for groundedness.",
    )
    groundedness_reason: str = Field(
        description="Explanation for the groundedness score.",
    )


evaluation_prompt = ChatPromptTemplate.from_messages([
    ("system", EVALUATION_PROMPT),
    (
        "human",
        """
        User Input:
        {user_input}

        Expected Behavior:
        {expected_behavior}

        Expected Facts:
        {expected_facts}

        Agent Response:
        {actual_output}

        Retrieved Context:
        {retrieved_context}
        """,
    ),
])

judge_llm = llm.with_structured_output(EvaluationResult)

evaluator = evaluation_prompt | judge_llm

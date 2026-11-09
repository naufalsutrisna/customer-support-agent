import json
import os

from app.graph import graph
from evaluation.evaluator import evaluator


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATASET_PATH = os.path.join(BASE_DIR, "evaluation", "dataset.json")


def load_dataset():
    with open(DATASET_PATH, "r", encoding="utf-8") as file:
        return json.load(file)


def run_evaluation():
    dataset = load_dataset()

    for test_case in dataset:
        result = graph.invoke({
            "messages": [
                {
                    "role": "user",
                    "content": test_case["input"],
                }
            ]
        })
        
        for message in result["messages"]:
            if message.type == "ai":
                for tool_call in message.tool_calls:
                    print("\nTool Call:")
                    print(f"Name: {tool_call['name']}")
                    print(f"Arguments: {tool_call['args']}")

            elif message.type == "tool":
                print("\nTool Result:")
                print(message.content)

        messages = result["messages"]
        actual_output = messages[-1].content

        tool_outputs = [
            message.content
            for message in messages
            if message.type == "tool"
        ]

        print(f"\nTest Case: {test_case['id']}")
        print(f"Category: {test_case['category']}")
        print(f"Actual Output:\n{actual_output}")

        if test_case["category"] == "out_of_scope":
            expected_output = (
                "I'm sorry, but I can only help with "
                "e-commerce customer support, such as orders "
                "and product information."
            )

            status = (
                "PASS"
                if actual_output == expected_output
                else "FAIL"
            )

            print(f"Rule-based Evaluation: {status}")
            continue

        evaluation_result = evaluator.invoke({
            "user_input": test_case["input"],
            "expected_behavior": test_case["expected_behavior"],
            "expected_facts": str(test_case.get("expected_facts", {})),
            "actual_output": actual_output,
            "retrieved_context": str(tool_outputs),
        })

        print("\nLLM-as-a-Judge Results:")
        print(f"Correctness: {evaluation_result.correctness_score}/5")
        print(f"Reason: {evaluation_result.correctness_reason}")
        print(f"Groundedness: {evaluation_result.groundedness_score}/5")
        print(f"Reason: {evaluation_result.groundedness_reason}")


if __name__ == "__main__":
    run_evaluation()
    
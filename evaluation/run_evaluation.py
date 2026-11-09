import json
import os

from app.graph import graph


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

        if tool_outputs:
            print(f"Retrieved Context:\n{tool_outputs}")


if __name__ == "__main__":
    run_evaluation()
    
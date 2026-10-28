from app.scope import validate_scope


def main():
    test_messages = [
        "Where is my order?",
        "What products did I order?",
        "Write a Python script to sort a list.",
        "Who will win the next election?",
    ]

    for message in test_messages:
        result = validate_scope(message)
        print(f"Message: {message}")
        print(f"Classification: {result.classification}")
        print()


if __name__ == "__main__":
    main()

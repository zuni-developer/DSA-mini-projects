from PostfixEvaluator import PostfixEvaluator
def run_tests():
    evaluator=PostfixEvaluator()
    test_cases=[
        ("3 4 +", 7),
        ("10 5 /", 2),
        ("2 3 4 * +", 14),
        ("5 1 2 + 4 * + 3 -", 14), 
        ("2 3 ^", 8),
        ("6 2 / 3 - 4 2 * +", 8),
        ("100 200 + 2 / 5 * 7 +", 757),
    ]
    for i, (expression, expected) in enumerate(test_cases, 1):
        try:
            result = evaluator.evaluate(expression)
            assert result == expected, f"❌ Test {i} failed: expected {expected}, got {result}"
            print(f"✅ Test {i} passed.")
        except Exception as e:
            print(f"❌ Test {i} raised an error: {e}")

if __name__ == "__main__":
    run_tests()
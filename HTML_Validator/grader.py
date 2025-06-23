import unittest
from test_html_validator import TestHtmlValidator

def run_grader():
    loader = unittest.TestLoader()
    suite = loader.loadTestsFromTestCase(TestHtmlValidator)
    runner = unittest.TextTestRunner(verbosity=0, resultclass=unittest.TextTestResult)
    result = runner.run(suite)

    total = result.testsRun
    failed = len(result.failures) + len(result.errors)
    passed = total - failed

    print(f"{passed} test{'s' if passed != 1 else ''} passed.")
    print(f"{failed} test{'s' if failed != 1 else ''} failed.")

    if failed == 0:
        print("Great job! Your score for this assignment would be 100%")
    else:
        score = int((passed / total) * 100)
        for i, failure in enumerate(result.failures + result.errors, 1):
            test_case, err = failure
            print(f"#{i}. {test_case.id().split('.')[-1]} failed:\n{err.strip().splitlines()[-1]}")
        print(f"Your score for this assignment would be {score}%\n")

if __name__ == '__main__':
    run_grader()

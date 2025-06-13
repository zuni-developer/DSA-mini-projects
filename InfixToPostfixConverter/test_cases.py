from InfixToPostfixConverter import InfixToPostfix  

def test_case(expr, expected):
    converter = InfixToPostfix()
    converter.convert(expr)
    result = converter.get_postfix()
    print(f"Infix: {expr} ➜ Postfix: {result}")
    assert result == expected, f"Expected: {expected}, Got: {result}"

def run_tests():
    test_case("A+B", "AB+")
    test_case("A+B*C", "ABC*+")
    test_case("(A+B)*C", "AB+C*")
    test_case("A+B*C-(D/E+F)*G", "ABC*+DE/F+G*-")
    test_case("A*(B+C*D)+E", "ABCD*+*E+")
    test_case("((A+B)*C-(D-E))*(F+G)", "AB+C*DE--FG+*")
    test_case("4+9/7", "497/+")
    test_case("10+20*30", "102030*+")
    test_case("100*(2+12)/14", "100212+*14/")

if __name__ == "__main__":
    run_tests()
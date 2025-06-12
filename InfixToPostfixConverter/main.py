from InfixToPostfixConverter import InfixToPostfix

def main():
    converter=InfixToPostfix()
    print("Infix to Postfix Converter")

    while True:
        print("\nMenu:")
        print("1. Convert infix expression")
        print("2. Exit")
        choice=input("Enter choice (1 or 2): ")
        match choice:
            case '1':
                expr=input("Enter an infix expression: ")
                converter.convert(expr)
                postfix=converter.get_postfix()
                print(f"Postfix expression: {postfix}")
            case '2':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter 1 or 2.")

main()
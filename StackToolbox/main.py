from stack_operations import Stack  

stack=Stack()
condition=True
while condition:
    condition = False
    print("\nChoose an operation:")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Size")
    print("6. Is Empty?")
    print("7. Clear")
    print("8. Search")
    print("9. Reverse")
    print("10. Copy")
    print("11. Multi-Pop")
    print("12. Peek-N")
    print("13. Exit")
    choice=int(input("Enter your choice (1-13): "))
    match choice:
        case 1:
            item=input("Enter value to push: ")
            stack.push(item)
        case 2:
            print("Popped:", stack.pop())
        case 3:
            print("Top element:", stack.peek())
        case 4:
            stack.display()
        case 5:
            print("Size of stack:", stack.size())
        case 6:
            print("Stack is empty?", stack.is_empty())
        case 7:
            stack.clear()
            print("Stack cleared!")
        case 8:
            value=input("Enter value to search: ")
            print("Position from top:", stack.search(value))
        case 9:
            stack.reverse()
            print("Stack reversed!")
        case 10:
            copied=stack.copy()
            print("Copied stack:", copied)
        case 11:
            n=int(input("Enter number of elements to pop: "))
            result=stack.multi_pop(n)
            if result:
                print(result)
        case 12:
            n=int(input("Enter n to peek nth element from top: "))
            print("Peek-N:", stack.peek_n(n))
        case 13:
            print("Exiting program...")
            break
        case _:
            print("Invalid choice! Try again!")
            break

    print("To continue press 1 else press 0")
    condition=int(input())
    while condition!=1 and condition!=0:
        print("Invalid input! Please enter 1 to continue or 0 to exit: ")
        condition = int(input())
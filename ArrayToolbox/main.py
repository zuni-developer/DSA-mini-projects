from fixed_array_template import  FixedSizeArray

print("Enter the size of the array: ")
size=int(input())
array=FixedSizeArray(size)
condition=True
while condition:
    condition=False
    print("\nChoose an operation:")
    print("1. Insert")
    print("2. Delete")
    print("3. Update")
    print("4. Get")
    print("5. Display")
    print("6. Print")
    print("7. Search")
    print("8. Is Full?")
    print("9. Is Empty?")
    print("10. Clear")
    print("11. Bubble sort")
    print("12. Binary search")
    print("13. Exit")
    choice = int(input("Enter your choice (1-11): "))
    match choice:
        case 1:
            index = int(input("Enter index to insert: "))
            value = int(input("Enter value to insert: "))
            array.insert(index, value)
        case 2:
            index = int(input("Enter index to delete: "))
            array.delete(index)
        case 3:
            index = int(input("Enter index to update: "))
            value = input("Enter new value: ")
            array.update(index, value)
        case 4:
            index = int(input("Enter index to get value: "))
            val = array.get(index)
            if val is not None:
                print("Value at index", index, ":", val)
        case 5:
            array.display()
        case 6:
            array.print()
        case 7:
            value = int(input("Enter the value you want to search: "))
            array.search(value)
        case 8:
            print("Array is full?", array.is_full())
        case 9:
            print("Array is empty?", array.is_empty())
        case 10:
            array.clear()
            print("Array is cleared!")
        case 11:
            array.bubble_sort()
            print("Array is sorted!")
        case 12:
            array.bubble_sort()
            key=int(input("Enter the value to find: "))
            print(key, "found at: ",array.binary_search(key))
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
        condition=int(input())
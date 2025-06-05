from CircularQueueToolbox import CircularQueue

def main():
    print("Circular Queue Toolbox")
    size=int(input("Enter capacity of the circular queue: "))
    queue=CircularQueue(size)
    while True:
        print("\nMenu:")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Check if empty")
        print("5. Check if full")
        print("6. Size")
        print("7. Clear")
        print("8. Exit")
        choice=input("Enter your choice (1-8): ")
        match choice:
            case '1':
                item=input("Enter item to enqueue: ")
                result=queue.enqueue(item)
                if result=="Queue is full!":
                    print(result)
                else:
                    print("Item enqueued.")
            case '2':
                item=queue.dequeue()
                if item is None:
                    print("Queue is empty!")
                else:
                    print(f"Dequeued item: {item}")
            case '3':
                if queue.is_empty():
                    print("Queue is empty!")
                else:
                    print(f"Front item: {queue.peek()}")
            case '4':
                print("Queue is empty." if queue.is_empty() else "Queue is not empty.")
            case '5':
                print("Queue is full." if queue.is_full() else "Queue is not full.")
            case '6':
                print(f"Size of queue: {queue.size()}")
            case '7':
                queue.clear()
                print("Queue cleared.")
            case '8':
                print("Goodbye!")
                break
            case _:
                print("Invalid choice. Please enter a number from 1 to 8.")

main()
from queue_class import Queue 

def main():
    q=Queue()
    while True:
        print("\n--- Queue Operations ---")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Peek")
        print("4. Is Empty")
        print("5. Size")
        print("6. Clear")
        print("7. Contains")
        print("8. Exit")
        choice=input("Enter your choice: ")
        match choice:
            case "1":
                item=input("Enter item to enqueue: ")
                q.enqueue(item)
                print(f"Enqueued: {item}")
            case "2":
                removed=q.dequeue()
                print("Dequeued:", removed if removed is not None else "Queue is empty")
            case "3":
                front=q.peek()
                print("Front item:", front if front is not None else "Queue is empty")
            case "4":
                print("Queue is empty:", q.is_empty())
            case "5":
                print("Queue size:", q.size())
            case "6":
                q.clear()
                print("Queue cleared.")
            case "7":
                item=input("Enter item to check: ")
                print("Found in queue:" if q.contains(item) else "Not found in queue.")
            case "8":
                print("Exiting.")
                break
            case _:
                print("Invalid choice. Try again.")
            
main()
from DoubleEndedLinkedlist import LinkedList

def test_linked_list_pass_fail():
    print("📦 Starting linked list tests...\n")
    ll = LinkedList()

    # Test insert()
    ll.insert(5)
    ll.insert(2)
    ll.insert(8)
    expected = [5, 2, 8]
    actual = get_list_as_array(ll)
    print_result("insert()", actual == expected)

    # Test insertAtFront()
    ll.insertAtFront(1)
    expected = [1, 5, 2, 8]
    actual = get_list_as_array(ll)
    print_result("insertAtFront()", actual == expected)

    # Test insertAtEnd()
    ll.insertAtEnd(10)
    expected = [1, 5, 2, 8, 10]
    actual = get_list_as_array(ll)
    print_result("insertAtEnd()", actual == expected)

    # Test remove() existing element
    ll.remove(2)
    expected = [1, 5, 8, 10]
    actual = get_list_as_array(ll)
    print_result("remove() existing element", actual == expected)

    # Test remove() non-existing element (list should stay same)
    ll.remove(99)
    expected = [1, 5, 8, 10]
    actual = get_list_as_array(ll)
    print_result("remove() non-existing element", actual == expected)

    # Test removeFromFront()
    ll.removeFromFront()
    expected = [5, 8, 10]
    actual = get_list_as_array(ll)
    print_result("removeFromFront()", actual == expected)

    # Test removeFromBack()
    ll.removeFromBack()
    expected = [5, 8]
    actual = get_list_as_array(ll)
    print_result("removeFromBack()", actual == expected)

    # Test find() existing element
    found = ll.find(8)
    print_result("find() existing element", found == True)

    # Test find() non-existing element
    found = ll.find(100)
    print_result("find() non-existing element", found == False)

    # Test getElementAt() valid index
    value = ll.getElementAt(1)
    print_result("getElementAt() valid index", value == 8)

    # Test getElementAt() out of range
    value = ll.getElementAt(5)
    print_result("getElementAt() out of range", value == "Index out of range" or value == "Index out of bond")  # accept both

    # Test selection_sort()
    ll.insert(3)
    ll.insertAtFront(7)
    # Current list: [7,5,8,3]
    ll.selection_sort()
    expected = sorted([7,5,8,3])  # [3,5,7,8]
    actual = get_list_as_array(ll)
    print_result("selection_sort()", actual == expected)

    print("\n✅ All tests done!")

def get_list_as_array(linked_list):
    """Helper: returns list elements as array"""
    result = []
    current = linked_list.head
    while current:
        result.append(current.data)
        current = current.next
    return result

def print_result(test_name, passed):
    if passed:
        print(f"✅ PASS: {test_name}")
    else:
        print(f"❌ FAIL: {test_name}")

# Import your class first
if __name__ == "__main__":
    from DoubleEndedLinkedlist.DoubleEndedLinkedlist import LinkedList 
    test_linked_list_pass_fail()

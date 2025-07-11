from special_list import SpecialList 

# Structured and additional simple test cases
if __name__ == "__main__":
    def test_case(description, expected, actual):
        if expected == actual:
            print(f"PASSED: {description}")
        else:
            print(f"FAILED: {description} -> Expected: {expected}, Got: {actual}")

    L = SpecialList()
    L.insert(2)
    L.insert(5)
    L.insert(7)
    test_case("Initial insert", [2, 5, 7], L._list.copy())

    L.insert(6)
    test_case("After insert(6)", [2, 5, 7, 6], L._list.copy())

    L.delete(5)
    test_case("After delete(5)", [2, 7, 6], L._list.copy())

    L.undo()  # undo delete(5)
    test_case("After undo delete(5)", [2, 7, 6, 5], L._list.copy())

    L.undo()  # undo insert(6)
    test_case("After undo insert(6)", [2, 7, 5], L._list.copy())

    L.redo()  # redo insert(6)
    test_case("After redo insert(6)", [2, 7, 5, 6], L._list.copy())

    L.insert(4)
    test_case("After insert(4)", [2, 7, 5, 6, 4], L._list.copy())

    L.redo()  # redo has nothing to redo
    test_case("After redo with nothing to redo", [2, 7, 5, 6, 4], L._list.copy())

    L.delete(3)  # deleting non-existing
    test_case("After delete(3) non-existing", [2, 7, 5, 6, 4], L._list.copy())

    L.undo()  # undo delete(3)
    test_case("After undo delete(3) non-existing", [2, 7, 5, 6, 4], L._list.copy())

    L.undo()  # undo insert(4)
    test_case("After undo insert(4)", [2, 7, 5, 6], L._list.copy())

    L.undo()  # undo insert(6)
    test_case("After undo insert(6)", [2, 7, 5], L._list.copy())

    L.redo()  # redo insert(6)
    test_case("After redo insert(6)", [2, 7, 5, 6], L._list.copy())

    L.redo()  # redo insert(4)
    test_case("After redo insert(4)", [2, 7, 5, 6, 4], L._list.copy())

    # Additional simple cases
    sl_simple = SpecialList()
    sl_simple.insert(1)
    sl_simple.insert(2)
    sl_simple.insert(2)
    sl_simple.insert(3)
    sl_simple.delete(2)
    sl_simple.undo()  # undo delete(2)
    test_case("Simple: undo delete(2)", [1, 3, 2], sl_simple._list.copy())

    sl_simple.undo()  # undo insert(3)
    test_case("Simple: undo insert(3)", [1, 2], sl_simple._list.copy())

    sl_simple.redo()  # redo insert(3)
    test_case("Simple: redo insert(3)", [1, 2, 3], sl_simple._list.copy())

    sl_simple.redo()  # redo delete(2)
    test_case("Simple: redo delete(2)", [1, 3], sl_simple._list.copy())

    print("\nAll structured and simple cases executed.")
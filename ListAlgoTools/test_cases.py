from ListUtils import ListUtils

def test_insert_sorted():
    lst = [1, 3, 5, 7]
    ListUtils.insert_sorted(lst, 4)
    assert lst == [1, 3, 4, 5, 7], f"Test failed: got {lst}"

    lst = [2, 4, 6]
    ListUtils.insert_sorted(lst, 1)
    assert lst == [1, 2, 4, 6]

    lst = [2, 4, 6]
    ListUtils.insert_sorted(lst, 7)
    assert lst == [2, 4, 6, 7]

    lst = []
    ListUtils.insert_sorted(lst, 5)
    assert lst == [5]

    ListUtils.insert_sorted(None, 5)  # Should handle None safely


def test_remove_maximum_values():
    # Null list should not throw an error
    lst = None
    ListUtils.remove_maximum_values(lst, 2)  # Should do nothing

    # Test: N is 0 → list remains unchanged
    lst = ["a", "b", "c", "d"]
    ListUtils.remove_maximum_values(lst, 0)
    assert lst == ["a", "b", "c", "d"], f"Test failed: got {lst}"

    # Test: N > list size → list becomes empty
    lst = ["doge"]
    ListUtils.remove_maximum_values(lst, 2)
    assert lst == [], f"Test failed: got {lst}"

    # Test: N = list size → list becomes empty
    lst = ["doge"]
    ListUtils.remove_maximum_values(lst, 1)
    assert lst == [], f"Test failed: got {lst}"

    # Test: each max appears once (remove top 2 max: "koala", "kangaroo")
    lst = ["doge", "cat", "kangaroo", "koala", "bear"]
    ListUtils.remove_maximum_values(lst, 2)
    assert lst == ["doge", "cat", "bear"], f"Test failed: got {lst}"

    # Test: max values appear more than once (remove all "koala" and "kangaroo")
    lst = ["doge", "kangaroo", "cat", "kangaroo", "koala", "bear", "doge", "koala", "kangaroo"]
    ListUtils.remove_maximum_values(lst, 2)
    assert lst == ["doge", "cat", "bear", "doge"], f"Test failed: got {lst}"


def test_contains_subsequence():
    assert ListUtils.contains_subsequence([1, 2, 3, 4, 5], [3, 4]) == True
    assert ListUtils.contains_subsequence([1, 2, 3, 4, 5], [4, 3]) == False
    assert ListUtils.contains_subsequence([1, 2, 3], [1, 2, 3]) == True
    assert ListUtils.contains_subsequence([1, 2, 3], [1, 3]) == False
    assert ListUtils.contains_subsequence([], [1]) == False
    assert ListUtils.contains_subsequence([1, 2], []) == False
    assert ListUtils.contains_subsequence(None, [1]) == False
    assert ListUtils.contains_subsequence([1, 2], None) == False




if __name__ == "__main__":
    test_insert_sorted()
    test_remove_maximum_values()
    test_contains_subsequence()
    print("All tests passed.")

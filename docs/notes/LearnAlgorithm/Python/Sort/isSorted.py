import random


def is_sorted(arr: list) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


def is_sorted_disp(arr: list) -> bool:
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            print("Given input is not sorted.")
            return False
    print("Given input is sorted.")
    return True


def sorted_test(test_times: int, test_len: int, sort_function) -> bool:
    for i in range(test_times):
        array = []
        for j in range(test_len):
            array.append(random.randint(0, test_len))
        arr_cpy = array[:]
        sort_function(array)
        if not is_sorted(array):
            print("Test Failed")
            print("Failed Case:", arr_cpy)
            arr_cpy.sort()
            print("Expected:", arr_cpy)
            print("Get:", array)
            return False
    print("Test Passed", test_times, "tests with arrays of length", test_len)
    return True

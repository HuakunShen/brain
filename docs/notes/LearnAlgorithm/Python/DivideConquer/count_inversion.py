import random
import matplotlib.pyplot as plt
import time


def count_inversion_brute_force(lst: list) -> int:
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] > lst[j]:
                count += 1
    return count


def count_inversion_divide_conquer_wrapper(lst: list) -> int:
    return count_inversion_divide_conquer(lst)[1]


def count_inversion_divide_conquer(lst: list):
    # divide
    mid = len(lst) // 2
    left = lst[:mid]
    right = lst[mid:]

    # recursive call
    left_count = right_count = 0
    if len(lst) > 1:
        left, left_count = count_inversion_divide_conquer(left)
        right, right_count = count_inversion_divide_conquer(right)

    # merge
    cross_count = i = j = 0
    merged = []
    while i != len(left) and j != len(right):
        if left[i] > right[j]:
            cross_count += len(left) - i
            merged.append(right[j])
            j += 1
        elif left[i] <= right[j]:
            merged.append(left[i])
            i += 1
    if i != len(left):
        merged.extend(left[i:])
    elif j != len(right):
        merged.extend(right[j:])

    return merged, left_count + right_count + cross_count


def test_fixed(test_function):
    lst = [3, 4, 1, 2, 4]  # there are 5 inversions in total
    # print(test_function(lst))

    assert test_function(lst) == 4, "error from test_fixed()"


def test(test_times: int, lst_length: int):
    for i in range(test_times):
        lst = []
        for j in range(lst_length):
            lst.append(random.randint(1, lst_length))
        real_num_inversion = count_inversion_brute_force(lst)
        assert real_num_inversion == count_inversion_divide_conquer_wrapper(
            lst), "Test Failed from test()"
    print("Testing {0} times with random lists of length {1} has passed.".format(
        test_times, lst_length))


def get_random_list(n: int):
    lst = []
    for i in range(n):
        lst.append(random.randint(0, n))
    return lst


def time_test():
    length = []
    runtime = []
    for l in range(0, 10000, 100):
        lst = get_random_list(l)
        start_time = time.time()
        count_inversion_brute_force(lst)
        # count_inversion_divide_conquer_wrapper(lst)
        length.append(l)
        runtime.append(time.time() - start_time)
        print(l)

    fig, ax = plt.subplots()
    ax.grid()

    ax.plot(length, runtime)
    plt.show()


if __name__ == "__main__":
    test_fixed(count_inversion_brute_force)
    test_fixed(count_inversion_divide_conquer_wrapper)
    test(100, 100)

    time_test()

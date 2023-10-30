import matplotlib.pyplot as plt
import time


def fib_brute_force(n: int):
    if n < 0:
        return -1
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib_brute_force(n - 2) + fib_brute_force(n - 1)


def fib_memoization(n: int):
    memo = [-1] * (n + 1)
    memo[0] = 0
    if n >= 1:
        memo[1] = 1
    return fib_memo_helper(n, memo)


def fib_memo_helper(n, memo):
    if memo[n] != -1:
        return memo[n]
    else:
        memo[n] = fib_memo_helper(n - 2, memo) + fib_memo_helper(n - 1, memo)
        return memo[n]


def fib_dynamic_programming(n: int):
    memo = [-1] * (n + 1)
    memo[0] = 0
    if n >= 1:
        memo[1] = 1
    for i in range(2, n + 1):
        memo[i] = memo[i - 2] + memo[i - 1]
    return memo[n]


fib_list = [fib_brute_force, fib_memoization, fib_dynamic_programming]
plot_list = [[[], []], [[], []], [[], []]]
for i in range(40):
    for j in range(3):
        plot_holder = plot_list[j]
        algo = fib_list[j]
        start = time.time()
        algo(i)
        end = time.time()
        plot_holder[0].append(i)
        plot_holder[1].append(end - start)
for i in range(3):
    plt.plot(plot_list[i][0], plot_list[i][1])
plt.legend(["Brute Force", "Memoization", "DP"])
plt.show()

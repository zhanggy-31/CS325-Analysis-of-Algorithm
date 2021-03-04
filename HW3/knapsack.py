import random
import time


def main():
    ##n = int(input(" N is ?"))
    n = 30
    capacity = int(input(" W is ?"))
    value = [random.randint(0, 100) for __ in range(int(n))]
    weight = [random.randint(0, 100) for __ in range(int(n))]

    rec_start = time.time()
    recursion(capacity, weight, value, n)
    rec_end = time.time()

    dp_start = time.time()
    dp(capacity, weight, value, n)
    dp_end = time.time()

    print("N = ", n, "W = ", capacity, "Rec time = %f" % (rec_end - rec_start), "DP time = %f" % (dp_end - dp_start), "max Rec = ", recursion(capacity, weight, value, n), "max Dp = ", dp(capacity, weight, value, n))
    main()


def recursion(capacity, weight, value, n):

    if n == 0 or capacity == 0:
        return 0

    if weight[n - 1] > capacity:
        return recursion(capacity, weight, value, n-1)

    else:
        return max(value[n-1] + recursion(capacity - weight[n-1], weight, value, n-1),
                   recursion(capacity, weight, value, n-1))


def dp(capacity, weight, value, n):
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]

    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][capacity]


main()
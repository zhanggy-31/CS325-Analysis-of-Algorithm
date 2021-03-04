

def main():

    f = open("shopping.txt")
    cases = int(f.readline().strip())
    result = open("results.txt", "w+")
    for x in range(cases):
        items = int(f.readline().strip())
        value = []
        weight = []
        for i in range(items):
            v, w = map(int, f.readline().strip().split())
            value.append(v)
            weight.append(w)

        capacity = []
        members = int(f.readline().strip())
        for i in range(members):
            capacity.append(int(f.readline().strip()))


        total = 0
        plan = []
        for i in range(len(capacity)):
            t, p = dp(capacity[i], weight, value, items)
            total += t
            plan.append(p)

        result.write("Test Case %d" % (x + 1) + "\n")
        result.write("Total Price %d" % total + "\n")
        for i in range(len(plan)):
            result.write("%s: %s" % (i + 1, " ".join(str(i) for i in plan[i])) + "\n")

        result.write("\n")



    f.close()
    result.close()


def dp(capacity, weight, value, n):
    choice = []
    K = [[0 for x in range(capacity + 1)] for x in range(n + 1)]
    for i in range(n + 1):
        for w in range(capacity + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif weight[i - 1] <= w:
                K[i][w] = max(value[i - 1] + K[i - 1][w - weight[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    i = n
    k = capacity

    while i != 0:
        if K[i][k] != K[i - 1][k]:
            choice.append(i)
            i -= 1
            k -= weight[i]
        else:
            i -= 1
    plan = sorted(choice)

    return K[n][capacity], plan


main()
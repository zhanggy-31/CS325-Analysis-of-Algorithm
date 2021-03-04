def main():
    f = open("act.txt")
    cases = int(input("how many cases you want to process from txt file?")) # for making the program shorter
    for x in range(cases):
        activity = int(f.readline().strip())        # get the activity number
        arr = []
        for i in range(activity):
            o, s, e = map(int, f.readline().strip().split())    # put order, start, end into a list
            arr.append([o, s, e])                               # 2d list for all activities

        arr.sort(key=lambda x: (x[1], x[2]), reverse=True)      # sort by end time and reverse the order

        L2S = []
        i = 0
        L2S.append(arr[i])                                      # start from the latest one
        for j in range(len(arr)):
            if arr[i][1] >= arr[j][2]:
                L2S.append(arr[j])
                i = j

        L2S.sort(key=lambda x:x[0])                             # sort by orders
        print("case:",x+1, L2S)


main()

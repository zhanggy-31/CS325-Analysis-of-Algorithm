import time
import random


def main():
    n = input("how many numbers: \n")
    data = [random.randint(0, 10000) for __ in range(int(n))]
    i = input("1 for merge3, 2 for exit:\n")
    if i == '1':
        merge_sort3_data = data
        print("array size: ", len(merge_sort3_data))
        #   output array size
        start = time.time()
        merge_sort3(merge_sort3_data)
        end = time.time()
        #   count time
        print(merge_sort3_data)
        #   print results
        print(end - start, "sec\n")
        print("-------------------------")
        #   count the running time
        main()
        #   repeat main()
    elif i == '2':
        exit()
    else:
        exit()

def merge_sort3(data):
    if len(data) > 1:
        #   check the length of separating data
        n = int(len(data) // 3)
        #   get the mid point of current data
        arr = data[:n]
        brr = data[n:2*n+1]
        crr = data[2*n+1:]

        merge_sort3(arr)
        merge_sort3(brr)
        merge_sort3(crr)

        i, j, k, z = 0, 0, 0, 0
        while i < len(arr) and j < len(brr) and k < len(crr):
            if arr[i] < brr[j]:
                #   min in arr and brr
                if arr[i] < crr[k]:
                    #   min in arr, brr, and crr
                    data[z] = arr[i]
                    i = i + 1
                else:
                    data[z] = crr[k]
                    k = k + 1
            else:
                if brr[j] < crr[k]:
                    data[z] = brr[j]
                    j = j + 1
                else:
                    data[z] = crr[k]
                    k = k + 1
            z = z + 1

        while i < len(arr) and j < len(brr):
            #   compare the rest number
            if arr[i] < brr[j]:
                data[z] = arr[i]
                i = i + 1
                z = z + 1
            else:
                data[z] = brr[j]
                j = j + 1
                z = z + 1
        while j < len(brr) and k < len(crr):
            if brr[j] < crr[k]:
                data[z] = brr[j]
                j = j + 1
                z = z + 1
            else:
                data[z] = crr[k]
                k = k + 1
                z = z + 1
        while j < len(brr) and k < len(crr):
            if arr[i] < crr[k]:
                data[z] = arr[i]
                i = i + 1
                z = z + 1
            else:
                data[z] = crr[k]
                k = k + 1
                z = z + 1
        while i < len(arr):
            data[z] = arr[i]
            i = i + 1
            z = z + 1
        while j < len(brr):
            data[z] = brr[j]
            j = j + 1
            z = z + 1
        while k < len(crr):
            data[z] = crr[k]
            k = k + 1
            z = z + 1


main()


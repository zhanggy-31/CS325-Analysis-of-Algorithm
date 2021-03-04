import time
import random


def main():
    n = input("how many numbers: \n")
    data = [random.randint(0, 10000) for __ in range(int(n))]
    i = input("1 for insertion, 2 for merge, 3 for exit:\n")
    if i == '1':
        insertionsort_data = data
        print("array size: ", len(insertionsort_data))
        #   output array size
        start = time.time()
        insertion_sort(insertionsort_data)
        end = time.time()
        #   count time
        print(insertionsort_data)
        #   print results
        print(end - start, "sec\n")
        print("-------------------------")
        #   count the running time
        main()
        #   repeat main()
    elif i == '2':
        mergesort_data = data
        print("array size: ", len(mergesort_data))
        #   output array size
        start = time.time()
        merge_sort(mergesort_data)
        end = time.time()
        #   count time
        print(mergesort_data)
        #   print results
        print(end - start, "sec\n")
        print("-------------------------")
        #   count the running time
        main()
        #   repeat main()
    elif i == '3':
        exit()


def insertion_sort(data):
    for i in range(1, len(data)):
        #   start sorting at first data
        value = data[i]
        j = i - 1
        while j >= 0 and value < data[j]:
            data[j + 1] = data[j]
            j = j - 1
            data[j + 1] = value


def merge_sort(data):
    if len(data) > 1:
        #   check the length of separating data
        n = len(data) // 2
        #   get the mid point of current data
        arr = data[:n]
        brr = data[n:]

        merge_sort(arr)
        merge_sort(brr)

        i, j, k = 0, 0, 0
        while i < len(arr) and j < len(brr):
            #   compare the smallest numbers in two arrays
            if arr[i] < brr[j]:
                data[k] = arr[i]
                i = i + 1
            else:
                data[k] = brr[j]
                j = j + 1
            k = k + 1
        while i < len(arr):
            #   place the rest numbers of arr
            data[k] = arr[i]
            i = i + 1
            k = k + 1
        while j < len(brr):
            #   place the rest numbers of brr
            data[k] = brr[j]
            j = j + 1
            k = k + 1


#   run main
main()


def main(file):
    output_insertionsort = ''
    output_mergesort = ''
    for line in open(file):
        array = line.split()
        #   split numbers by space

        insertionsort_data = [int(i) for i in array[1:]]
        mergesort_data = [int(i) for i in array[1:]]
        #   get the numbers except the first one

        insertion_sort(insertionsort_data)
        merge_sort(mergesort_data)
        #   sort each line of the data

        insertionsort_data = [str(i) for i in insertionsort_data]
        mergesort_data = [str(i) for i in mergesort_data]
        #   change types

        output_insertionsort += ' '.join(insertionsort_data) + '\n'
        output_mergesort += ' '.join(mergesort_data) + '\n'
        #   collect outputs

    p = open('insert.txt', 'w+')
    p.write(output_insertionsort)

    q = open('merge.txt', 'w+')
    q.write(output_mergesort)
    #   write outputs

    p.close()
    q.close()
    #   close files


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


#   run data.txt in main
main('data.txt')

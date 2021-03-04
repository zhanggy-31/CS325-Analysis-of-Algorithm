
def main(file):
    output_mergesort3 = ''
    for line in open(file):
        array = line.split()
        #   split numbers by space

        mergesort3_data = [int(i) for i in array[1:]]
        #   get the numbers except the first one

        merge_sort3(mergesort3_data)
        #   sort each line of the data

        mergesort3_data = [str(i) for i in mergesort3_data]
        #   change types

        output_mergesort3 += ' '.join(mergesort3_data) + '\n'
        #   collect outputs

    f = open('merge3.txt', 'w+')
    f.write(output_mergesort3)
    f.close()


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

#   run data.txt in main
main('data.txt')

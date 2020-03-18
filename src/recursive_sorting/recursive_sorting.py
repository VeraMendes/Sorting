# TO-DO: complete the helper function below to merge 2 sorted arrays
def merge(arrA, arrB):
    # elements = len(arrA) + len(arrB)
    # merged_arr = [0] * elements
    # new array ready to receive merged elements
    merged_arr = []

    # if both arrays are empty, final array is empty
    if len(arrA) == 0 and len(arrB) == 0:
        merged_arr = []
    # if arrA is empty, final array is equal to arrB
    elif len(arrA) == 0:
        merged_arr = arrB
    # if arrB is empty, final array is equal to arrA
    elif len(arrB) == 0:
        merged_arr = arrA

    # index for both arrays starting point, defining as variables
    i = 0
    j = 0

    # considering both indexes are equal or smaller than max len of arrays
    while i <= len(arrA) and j <= len(arrB):

        # if index of A go over len of array, then only append the rest of the
        # array B into the final array
        if i == len(arrA):
            # print('a')
            # print(i)
            for value in arrB[j:]:
                merged_arr.append(value)
            break

        # if index of B go over len of array, then only append the rest of the
        # array A into the final array
        elif j == len(arrB):
            # print('b')
            for value in arrA[i:]:
                merged_arr.append(value)
            break

        else:
            # print(i)
            # print(j)

            # append to final array the smallest value found from the
            # comparation of both arrays
       
            if arrA[i] < arrB[j]:
                merged_arr.append(arrA[i])
                i += 1
            else:
                merged_arr.append(arrB[j])
                j += 1

        # if len(merged_arr) == len(arrA) + len(arrB):
        #     break

    return merged_arr


# implement the Merge Sort function below USING RECURSION
def merge_sort(arr):

    # check if array has more than one element, 
    # otherwise array is sorted
    if len(arr) > 1:

        # divide the array in two new arrays
        halfpoint = len(arr)//2
        arrC = arr[:halfpoint]
        arrD = arr[halfpoint:]
        # apply merge_sort in each of them
        merge_sort(arrC)
        merge_sort(arrD)

        # indexes for all arrays
        # i for arr, j for arrC, l for arrD
        i = 0
        j = 0
        m = 0

        # considering that both indexes are smaller than length of arrays
        while j < len(arrC) and m < len(arrD):

                # if index in arrC has smallest value than value in arrD, this
                # value enters the final array
            if arrC[j] < arrD[m]:
                arr[i] = arrC[j]
                # increase index for arrC
                j += 1
            else:
                # if index in arrD has smallest value than value in arrC, this
                # value enters the final array
                arr[i] = arrD[m]
                # increase index for arrD
                m += 1

            # increase index of final array
            i += 1

        # run only while index j is smaller than max len
        while j < len(arrC):
            arr[i] = arrC[j]
            j += 1
            i += 1

        # run only while index m is smaller than max len
        while m < len(arrD):
            arr[i] = arrD[m]
            m += 1
            i += 1

    return arr


# example from test_case = [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# STRETCH: implement an in-place merge sort algorithm
def merge_in_place(arr, start, mid, end):
    # TO-DO

    return arr

def merge_sort_in_place(arr, l, r):
    l = 1
    while l <= len(arr):
        r = 0
        for r in range(0,len(arr), l * 2):
            left, right = r, min(len(arr), r + 2 * l)
            mid = r + l
            p, q = left, mid
            while p < mid and q < right:
                if arr[p] < arr[q]:  # already sorted...
                    p += 1 # ... skip to next pair
                else: # need to swap...
                    temp = arr[q]  # store temp value...
                    arr[p + 1: q + 1] = arr[p:q]  # ... shift to the right...
                    arr[p] = temp # update value
                    p, mid, q = p + 1, mid + 1, q + 1  # ... go to next pair
        l *= 2
    return arr


# STRETCH: implement the Timsort function below
# hint: check out https://github.com/python/cpython/blob/master/Objects/listsort.txt
def timsort(arr):

    return arr

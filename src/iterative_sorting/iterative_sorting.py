# Complete the selection_sort() function below
def selection_sort(arr):

    # loop through n-1 elements
    for i in range(0, len(arr) - 1):
        # curr_index = i
        # smallest_index = curr_index
        smallest_index = i
        # find next smallest element
        for j in range(i+1, len(arr)):
            if arr[j] < arr[smallest_index]:
                smallest_index = j

            # (hint, can do in 3 loc)

        # swap
        if smallest_index != i:
            # print(f'{i} {smallest_index} {arr[i]} {arr[smallest_index]}')
            temp = arr[i]
            arr[i] = arr[smallest_index]
            arr[smallest_index] = temp

    return arr

# [1, 5, 8, 4, 2, 9, 6, 0, 3, 7]


# Implement the Bubble Sort function below
def bubble_sort(arr):

    for i in range(len(arr)):

        for j in range(0, (len(arr)-i-1)):

            if arr[j] > arr[j+1]:
                # print(f'{j} {j+1} {arr[j]} {arr[j+1]}')
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp            
    return arr


# STRETCH: implement the Count Sort function below
def count_sort(arr, maximum=-1):

    return arr

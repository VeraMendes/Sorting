def my_recursion(n):
    print(n)
    if n == 3:
        return

    my_recursion(n+1)
    my_recursion(n+1)


my_recursion(1)

# Fibonacci

# 0,1 - Base - if we solve recursively move towards it

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55


# 10th Fib number?

# print nth Fib number
def recursive_fib(n):
    # base case
    # test for negatives (TODO)
    # if n is 0
    # return 0
    if n == 0:
        return 0
    # if n is 1
    # return 1
    if n == 1:
        return 1

    # if we're not in the base case
    # recursion of n-1 and n-2
    return recursive_fib(n-1) + recursive_fib(n-2)


print(recursive_fib(10))


# Quick sort

[5 9 3 7 2 8 1 6]

# pick first number

# append all smaller to new array left
# append all bigger to new array right

[3 2 1] [5] [9 7 8 6]

# recurse left

[2 1] [3] []   [5]  [9 7  8  6]

# recurse left

[1] [2] [] [3] []   [5]  [9 7  8  6]

# recurse left

# recurse left
#  1 is sorted, base case

# recurse right
# empty array base case

# recruse right
# empty array, base case

# recurse right
[1][2][][3]     [5]   [9 7 8 6]

[1][2][][3][]    [5]   [7 8 6][9][]

# recurse left
​
[1][2][][3][]     [5] [6][7][8][ ][9][]
​
[1, 2] [3]
[1, 2,  3]
​
# plan
def quicksort(data):
# base case:  if array length 0 or 1
    if len(data) < 2:
# return array
        return data
# else:
    else:
# pick pivot might as well pick first because its unsorted, none are better
    pivot = data[0]
    left = []
    right = []  
# put anything smaller into left array
# put anything bigger into right array
    for value in data[1:]:
        if value <= pivot:
            left.append(value)
        else: right.append(value)
# return quicksort(left) + quicksort(right)
    return quicksort(left) + [pivot] + quicksort(right)

# quick sort
[ 5  9  3  7  2  8  1  6]
​
# pick first mumber
​
# append all smaller to new array left
# append all bigger to new array right
​
[3 2 1]  [5]  [9 7 8 6]
​
# recurse left
​
[2 1 ][3][]     [5]  [9 7 8 6]
​
#recurse left
​
[1][2][][3][]     [5]  [9 7 8 6]
​
#recurse left
# 1 is sorted,  base case
​
#recurse right
# empty array base case
​
#recurse right
# empty array, base case
​
#recurse right
[1][2][][3][]     [5]  [9 7 8 6]
​
[1][2][][3][]     [5] [7 8 6][9][]
​
#recurse left 
​
[1][2][][3][]     [5] [6][7][8][  ][9][]
​
[1, 2] [3]
[1, 2,  3]
​

def rec_factorial(n):
    print(n)
    # base case
    if n <= 1:
        return 1
​
    # what step can we do recursively?
    prev = rec_factorial(n-1)
    return n * prev
​
​
print(rec_factorial(9))

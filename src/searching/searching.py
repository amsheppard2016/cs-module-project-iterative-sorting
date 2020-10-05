def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):
        if arr[i] == target:
            return i      


    return -1   # not found


#Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    first = 0
    last =(len(arr)-1)

    while first <= last:
        middle = (first + last) // 2
        middle_value = arr[middle]

        if middle_value == target:
            return middle
            
        elif target < middle_value:
                last = middle - 1
        else:
                first = middle + 1
    return -1


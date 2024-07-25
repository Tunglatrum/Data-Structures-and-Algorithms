def binarySearch(arr, targetVal):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == targetVal:
            return mid
        
        if arr[mid] < targetVal:
            left = mid + 1
        else:
            right = mid - 1

    return -1

with open(r'C:\Users\Tung\Data Structures and Algorithms\Data-Structures-and-Algorithms\Arrays\test_case_arrays\random_numbers_exp.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]
print(int_list)

targetNum = 3
result = binarySearch(int_list, targetNum)

if result != -1:
    print("Value",targetNum,"found at index", result)
else:
    print("Target not found in array.")
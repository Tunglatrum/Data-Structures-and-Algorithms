def bubbleSort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                
def radixSortWithBubbleSort(arr):
    max_val = max(arr)
    exp = 1
    
    while max_val // exp > 0:
        radixArray = [[],[],[],[],[],[],[],[],[],[]]
        
        for num in arr:
            radixIndex = (num // exp) % 10
            radixArray[radixIndex].append(num)
        
        for bucket in radixArray:
            bubbleSort(bucket)
        
        i = 0
        for bucket in radixArray:
            for num in bucket:
                arr[i] = num
                i += 1
        
        exp *= 10


with open(r'C:\Users\Tung\Data Structures and Algorithms\Data-Structures-and-Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_100000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]
print(int_list)
radixSortWithBubbleSort(int_list)
print(int_list)
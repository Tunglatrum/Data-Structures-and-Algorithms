def partition(array, low , high):
    pivot = array[high]
    i = low - 1

    for j in range(low,high):
        if array[j] <= pivot:
            i+=1
            array[i],array[j]=array[j],array[i]
    array[i + 1], array[high] = array[high], array[i + 1]
    return i+1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        quickSort(array, low, pi - 1)
        quickSort(array, pi + 1, high)



with open(r'C:\Users\Tung\Data Structures and Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_125000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]

print(int_list)
n = len(int_list)

quickSort(int_list,0,n-1)
print(int_list)
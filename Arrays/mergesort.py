def merge(left, right):
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

def mergesort(array):
    step = 1  
    length = len(array)
    
    while step < length:
        for i in range(0, length, 2 * step):
            left = array[i:i + step]
            right = array[i + step:i + 2 * step]
            merged = merge(left, right)
            for j, val in enumerate(merged):
                array[i + j] = val
                
        step *= 2  
        
    return array


with open(r'C:\Users\Tung\Data Structures and Algorithms\Data-Structures-and-Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_125000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]
print(int_list)
mergesort(int_list)
print(int_list)
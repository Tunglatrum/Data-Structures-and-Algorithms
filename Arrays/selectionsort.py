with open(r'C:\Users\Tung\Data Structures and Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_125000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]

print(int_list)

n = len(int_list)
for i in range(n-1):
    min_index = i
    for j in range(i+1,n):
        if int_list[j] < int_list[min_index]:
            min_index = j
    min_value = int_list.pop(min_index)
    int_list.insert(i,min_value)

print(int_list)
    
    
        
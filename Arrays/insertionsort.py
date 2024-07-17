with open(r'C:\Users\Tung\Data Structures and Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_1000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]

print(int_list)
n = len(int_list)
for i in range(1,n):
    target_index = i
    target_value = int_list[i]
    for j in range(i-1,-1,-1):
        if int_list[j] > target_value:
            int_list[j+1] = int_list[j]
            target_index = j
        else:
            break
    int_list[target_index] = target_value

print(int_list)
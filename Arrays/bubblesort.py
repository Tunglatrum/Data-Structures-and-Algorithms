with open(r'C:\Users\Tung\Data Structures and Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_150000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]
print(int_list)

n = len(int_list)
for i in range(n-1):
    swapped = False
    for j in range(n-i-1):
        if int_list[j] > int_list[j+1]:
            int_list[j],int_list[j+1] = int_list[j+1],int_list[j]
        swapped = True
    if not swapped:
        break    
print(int_list)
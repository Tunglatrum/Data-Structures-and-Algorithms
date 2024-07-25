def linearSearch(array, targetNum):
    for i in range(len(array)):
        if array[i] == targetNum:
            return i
    return -1


with open(r'C:\Users\Tung\Data Structures and Algorithms\Data-Structures-and-Algorithms\Arrays\test_case_arrays\random_numbers_exp.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]
print(int_list)

targetNum = 11
result = linearSearch(int_list, targetNum)


if result != -1:
    print("Value",targetNum,"found at index",result)
else:
    print("Value",targetNum,"not found")
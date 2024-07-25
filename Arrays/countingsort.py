
def countingSort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)

    while len(array) > 0:
        num = array.pop(0)
        count[num] += 1

    for i in range(len(count)):
        while count[i] > 0:
            array.append(i)
            count[i] -= 1

    return array

with open(r'C:\Users\Tung\Data Structures and Algorithms\Data-Structures-and-Algorithms\Arrays\test_case_arrays\unique_random_numbers_multiline_10000.txt', 'r') as file:
    arrays = file.readlines()
    int_list = [int(item) for item in arrays]
print(int_list)

countingSort(int_list)
print(int_list)
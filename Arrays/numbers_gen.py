import random

unique_random_numbers = random.sample(range(100000000), 150000)

with open("Arrays/unique_random_numbers_multiline_150000.txt", 'w') as file:
    for number in unique_random_numbers:
        file.write(f"{number}\n")

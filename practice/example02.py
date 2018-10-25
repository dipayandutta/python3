dict_of_numbers = dict()


def dict_maked(number):
    for i in range(1, number+1):
        dict_of_numbers[i] = i*i


print(dict_maked(5))
print(dict_of_numbers)

for numbers in dict_of_numbers.keys():
    print(numbers)

max_numbers = input("Enter max numbers")
number = []
print(max_numbers)

for i in range(0, int(max_numbers)):
    numbers = input("Enter {} number".format(i))
    number.append(str(numbers).split(','))

print(number)
result_tuple = tuple(number)


print(result_tuple)

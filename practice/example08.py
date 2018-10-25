def alpha_num_calc(msg_string):
    counter_string = 0
    counter_digit = 0
    for message in msg_string.split(" "):
        if message.isalpha():
            counter_string += 1
            print(message)
        elif message.isdigit():
            counter_digit += 1
            print(message)
        else:
            break
    print("Total number of characters are {0} ".format(counter_string))
    print("Total number of digits are {0}".format(counter_digit))


alpha_num_calc("Hello World 123")

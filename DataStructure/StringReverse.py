def reverse(string):

    if string == "":
        return string
    else:
        return string[-1]+reverse(string[:-1])

def main():
    
    str_input = input("Please enter the string revese")
    reverse_output = reverse(str_input)
    print(reverse_output)

if __name__ == '__main__':
    main()

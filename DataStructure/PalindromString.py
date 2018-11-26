def ifPalindrom(string_ip):
    
    if string_ip == '':
        return True
    else:
        return (string_ip[0] == string_ip[-1] and ifPalindrom(string_ip[1:-1]))


def main():
    string_ip = input('Please enter a string')
    if (ifPalindrom(string_ip)):
        print ("PALINDROM")
    else:
        print("NOT PALINDROM!")


if __name__ == '__main__':
    main()
    

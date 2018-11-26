'''
    Recursion Example 
'''
def factorial(number):

    fact = 1
    assert number >= 0

    for i in range(1,number+1):
        fact = fact*i

    return fact

def rec_factorial(number):

    assert number>=0
    if number == 0 or number ==1:
        return 1
    else:
        return number*rec_factorial(number-1)

def main():

    number = int(input("Enter number to find the factorial of the number"))
    fact = factorial(number)
    print("factorial of {0} is {1}".format(number,fact))
    fact_rec = rec_factorial(number)
    print("Using Recursion")
    print("++++++++++++++++++")
    print("factorial of {0} is {1}".format(number,fact_rec))

if __name__ == '__main__':
    main()

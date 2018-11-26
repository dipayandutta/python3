def flatten(lst1 , lst2=[]):
    for element in lst1:
        if type(element) != list:
            lst2.append(element)
        else:
            flatten(element,lst2)

    return lst2


def main():
    lst1 = eval(input("Enter the list to flatten"))
    result = flatten(lst1)
    print('Flattened list :',result)


if __name__ == '__main__':
    main()

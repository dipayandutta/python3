
def sorted_list():
    items = [x for x in input("Enter String-> ").split(',')]
    items.sort()
    print(','.join(items))


if __name__ == '__main__':
    sorted_list()

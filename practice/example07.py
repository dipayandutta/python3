'''
s = input()
words = [word for word in s.split(" ")]
print("".join(sorted(list(set(words)))))
'''


def remove_split():
    words_upper = []
    string = input()
    words = [word for word in string.split(" ")]
    words_upper = [word.upper() for word in words]
    print("".join(sorted(list(set(words_upper)))))


if __name__ == '__main__':
    remove_split()

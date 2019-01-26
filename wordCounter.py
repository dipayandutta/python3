def wordCounter(str):
    counts = dict()

    words = str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1

    return counts 

print (wordCounter('The quick brown fox jumps over The lazy dog '))

fileName = input("Enter file name: ")
fh = open(fileName)
lst = list()
for line in fh:
    words = line.split()
    for word in words:
        if word in lst:
            continue
        else:
            lst.append(word)
            lst.sort()
print(lst)

try:
    d1 = dict()
    fp =open("demo.txt")
    for line in fp:
        words = line.split()
        for word in words:
            d1[word] = d1.get(word,0) +1
    print(d1)
except:
    print("file not found")

str = input("Enter String:")
d1 = dict()
for word in str:
    d1[word] = d1.get(word,0) +1
print(d1)

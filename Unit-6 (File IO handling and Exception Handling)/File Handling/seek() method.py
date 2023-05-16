fp = open("demo.txt","r")
print("First line")
fp.seek(0,0)
print(fp.readline())
fp = open("demo.txt","r")
fp.seek(0,0)
fp.readline()
print("current position of file pointer :",fp.tell());
fp.close()
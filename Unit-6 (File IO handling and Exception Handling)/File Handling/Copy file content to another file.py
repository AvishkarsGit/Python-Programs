fp = open("demo.txt","r")
string = fp.read()
print(string)
fp = open("pqr.txt","w")
fp.write(string)
fp.close()
print("File copied successfully.")
fp = open("demo.txt","a")
name = input("Enter your name:")
string = name+"\n"
fp.write(string)
print("Data written successfully..")
fp.seek(0,0)
fp.close()
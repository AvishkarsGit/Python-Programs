#write data into file
fp = open("demo.txt","w")
fp.write("Hi\n")
fp.write("Hello\n")
fp.write("How are you\n")
print("File written successfully..")
fp.close()
print("**** Exception  Handling *****")
print("Statement 1:",15/3)
try:
    print("Statement 2:",15/0)
except ZeroDivisionError:
    print("Division by zero exception error")

print("End of Program")
tuple1 = tuple(input("Enter 1st Tuple element (seperated by ',')").split(","))
tuple2 = tuple(input("Enter 2nd Tuple element (seperated by ',')").split(","))

print("Before interchanging  tuple variables: tuple1=",tuple1,"tuple2 =",tuple2)

tuple1,tuple2 = tuple2,tuple1

print("After interchanging  tuple variables: tuple1=",tuple1,"tuple2 =",tuple2)
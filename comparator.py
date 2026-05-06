value_a = float(input("Type the first value: "))
value_b = float(input("Type the second value: "))
value_c = float(input("Type the third value: ")) 

if value_a > value_b and value_a > value_c:
    print("First value is bigger")
elif value_b > value_a and value_b > value_c:
    print("Second value is bigger") 
elif value_c > value_a and value_c > value_b:
    print("Third value is bigger") 
else: 
    print("All values are equal")
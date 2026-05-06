# User start inputs

value_a = float(input("Type the first value: "))
value_b = float(input("Type the second value: "))
value_c = float(input("Type the third value: ")) 

# If all numbers are the same

if value_a == value_b and value_b == value_c:
    print ("All values are the same") 

# Two values tied (Both bigger than the third value)

elif value_a == value_b and value_a > value_c:
    print (f"Both {value_a} and {value_b} are bigger than {value_c}") 
elif value_a == value_c and value_a > value_b:
    print (f"Both {value_a} and {value_c} are bigger than {value_b}") 
elif value_b == value_c and value_b > value_a:
    print (f"Both {value_b} and {value_c} are bigger than {value_a}")

# Only one value is bigger

elif value_a > value_b and value_a > value_c:
    print(f"{value_a} is bigger")
elif value_b > value_a and value_b > value_c:
    print(f"{value_b} is bigger") 
else:
    print(f"{value_c} is bigger") 

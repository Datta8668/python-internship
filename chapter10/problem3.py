class Demo:
    a = 5

b = Demo()
print(b.a) # Prints the class attribute because instance attribute is not present
b.a = 1 # Instance attribute is set
print(b.a) # Prints the instance attribute because instance attribute is present
print(Demo.a) #Prints the class attribute
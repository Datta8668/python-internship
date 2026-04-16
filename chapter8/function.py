# function defination
# def avg():

#     a = int(input("Enter number: "))
#     b = int(input("Enter number: "))
#     c = int(input("Enter number: "))
#     d = int(input("Enter number: "))
#     average = (a + b + c + d) / 4
#     print("The average is: ", average)

# # function call
# avg()
# avg()



# function with no parameters
# def greet():
#     print("Good day datta")

# greet()


print()
# function with parameters
def greet(name , end):
    print("Good day,", name)
    print(end)

greet("datta", "Have a nice day..!")

print()
# function with return type
def add(a, b):
    return a + b
result = add(10, 20)
print("The sum is: ", result)

print()
# default parameter value
def GoodDay(name, end = "Have a nice day..!"):
    print(f"Good day, {name}")
    print(end)

GoodDay("datta")
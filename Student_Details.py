print ("=======Student Registration Form=======")

full_name = input("Enter your full name: ")
age = int(input("Enter your age: "))
city = input("Enter your city: ")

name_lower = full_name.lower()
first_name = name_lower.split()[0]

username = first_name + str(age)

student_id = age +len(full_name)

password = first_name[:3] + city[-2:] + str(age)

print ("\n=======Generated Student Details=======")
print ("Name: ", full_name)
print("city: ", city)
print("Age: ", age)
print("Username: ", username)
print("Student Id: ", student_id)
print("Password: ", password)

marks1 = int(input("Enter marks 1:"))
marks2 = int(input("Enter marks 2:"))
marks3 = int(input("Enter marks 3:"))
marks4 = int(input("Enter marks 4:"))

# check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3 + marks4)) / 400

if (total_percentage >= 40 and marks1 >= 35 and marks2 >= 35 and marks3 >= 35 and marks4 >= 35):
    print("congratulations..! You are pass!: ",total_percentage)

else:
    print("You are failed, try again next year!: ",total_percentage)


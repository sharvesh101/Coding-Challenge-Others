grade = int(input("Enter Your Grade: "))

if grade >= 90 and grade <= 100:
    print("Your grade is A")
elif grade >= 80 and grade <= 89:
    print("Your grade is B")
elif grade >= 70 and grade <= 79:
    print("Your grade is C")
elif grade >= 60 and grade <= 69:
    print("Your grade is D")
elif grade < 60:
    print("Your grade is F")
else:
    print("Enter Proper Grade")
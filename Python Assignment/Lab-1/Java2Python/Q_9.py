# Write a Java program for following grading system.
# Note: 
# Percentage>=90% : Grade A
# Percentage>=80% : Grade B
# Percentage>=70% : Grade C
# Percentage>=60% : Grade D
# Percentage>=40% : Grade E
# Percentage<40% : Grade F

marks = float(input("Enter your marks: "))

if marks >= 90:
    print("Grade A")
elif marks >= 80:
    print("Grade B")
elif marks >= 70:
    print("Grade C")
elif marks >= 60:
    print("Grade D")
elif marks >= 40:
    print("Grade E")
else:
    print("Grade F")
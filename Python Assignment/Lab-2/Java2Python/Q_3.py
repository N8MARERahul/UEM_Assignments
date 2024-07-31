# Admission to a professional course is subject to the following conditions:
# (a) marks in Mathematics >= 60
# (b) marks in Physics >= 50
# (c) marks in Chemistry >= 40
# (d) Total in all 3 subjects >= 200
# (Or) Total in Maths & Physics >=150
# Given the marks in the 3 subjects of n (user input) students, write a program to process the applications to list the eligible candidates.

math = int(input("Enter the marks for Mathematics: "))
physics = int(input("Enter the marks for Physics: "))
chemistry = int(input("Enter the marks for Chemistry: "))

if math >= 60 and physics >= 50 and chemistry >= 40 and (math + physics + chemistry >= 200 or math + physics >= 150):
    print("Eligible")
else:
    print("Not Eligible")
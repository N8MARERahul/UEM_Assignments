# Write a Java program to check whether a number is Buzz or not.

def isBuzz(num):
    return num % 7 == 0 or num % 10 == 7

num = int(input("Enter a number: "))

print(f"{num} is {'' if isBuzz(num) else 'not '}a Buzz Number")
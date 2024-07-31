# Write a Java program to check whether a number is prime or not.

def isPrime(number):
    for i in range(2, number // 2):
        if number % i == 0:
            return False
    return True

num = int(input("Enter a Number: "))

print(f"{num} is a {'Prime' if isPrime(num) else 'Composite'} Number")
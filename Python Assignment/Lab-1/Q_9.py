# WAP to check whether a)is a perfect number b)is an Armstrong number

def isPerfectNumber(num):
    sum = 0
    for i in range(1, num):
        if num % i == 0:
            sum += i
    
    return sum == num

def isArmstrongNumber(num):
    count = 0
    n = num
    while n != 0:
        count += 1
        n //= 10

    sum = 0
    n = num

    while n != 0:
        digit = n % 10
        sum += pow(digit, count)
        n //= 10

    return sum == num

num = int(input("Enter a number: "))

print(f"{num} is{'' if isPerfectNumber(num) else ' not'} a perfect number")

print(f"{num} is{'' if isArmstrongNumber(num) else ' not'} a Armstrong number")


# WAP to check whether a number is a palindrome or not

def palindrome(num):
    if num < 0:
        return False
    rev = 0

    n = num
    while n != 0:
        digit = n % 10
        rev = 10 * rev + digit
        n = n//10
    
    return rev == num

num = int(input("Enter a number: "))
if palindrome(num):
    print(f"{num} is a Palindrome Number")
else: 
    print(f"{num} is not a Palindrome Number")
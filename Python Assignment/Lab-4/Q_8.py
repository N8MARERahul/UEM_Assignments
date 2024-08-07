# Please write a program which count and print the numbers of each character in a string input by console.
# Example:
# If the following string is given as input to the program:
# abcdefgabc
# Then, the output of the program should be:
# a,2
# c,2
# b,2
# e,1
# d,1
# g,1
# f,1

string = input("Enter the String: ")

count = dict()

for char in string:
    if char in count:
        count[char] += 1
    else:
        count[char] = 1

for key, value in count.items():
    print(f"{key},{value}")
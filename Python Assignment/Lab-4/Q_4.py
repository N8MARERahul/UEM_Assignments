# Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words and sorting them alphanumerically.
# Suppose the following input is supplied to the program:
# hello world and practice makes perfect and hello world again
# Then, the output should be:
# again and hello makes perfect practice world

string = input("Enter the String: ")

words = string.split()

removed_duplicate = set(words)

list = list(removed_duplicate)
list.sort()

print("Removed duplicate and Sorted ->")
print(' '.join(list))

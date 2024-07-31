# WAP to reverse a given string.

str = input("Enter a string: ")

revStr = ""
for ch in str:
    revStr = ch + revStr

print(f"Reversed string = {revStr}")
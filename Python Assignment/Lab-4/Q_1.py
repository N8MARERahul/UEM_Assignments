# Write a program to enter a string. Calculate the length of the string. Find the substring country.
# Count the occurences of each word in the given sentence.
# If the String as input is India is my motherland. I love my country. Capital of India is New Delhi.

string = input("Enter the String: ")

# length of the string
print(f"Length of the String is: {len(string)}")

# Find the word "country"
wordLoaction = string.find("country")
if wordLoaction == -1:
    print(f"The Word 'country' is not Present!")
else:
    print(f"The Word 'country' is Present in the location - {wordLoaction}")

#Count the frequency of each word
count = dict()
words = string.split()
for word in words:
    if word in count:
        count[word] += 1
    else:
        count[word] = 1

print("Frequency of Each word is ->")
for key, value in count.items():
    print(f"{key} : {value}")
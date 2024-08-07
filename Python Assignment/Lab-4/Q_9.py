# Write a program that accepts a string
# I. 1.reverses it.
# II. 2.checks whether it is a palindrome.
# III. 3.checks whether it ends with a specific substring.
# IV. 4.capitalize the first letter of each word in a string
# V. 5.check if a string is anagram of another string
# VI. 6.remove vowels from string
# VII. 7.find length of the longest word in a sentence

string = input("Enter the String: ")

while True:
    print("\n\n1.Reverse")
    print("2.Check Palindrome")
    print("3.Check ending with specific substring")
    print("4.Capitalize the first letter of each word")
    print("5.Check Anagram of other string")
    print("6.Remove Vowels")
    print("7.Find length of the longest word")
    print("8.Exit")
    choice = int(input("Enter Your Choice: "))

    match choice:
        case 1:
            print(string[::-1])

        case 2:
            if string == string[::-1]:
                print("\nString is Palindrome")
            else:
                print("\nString is not Palindrome")

        case 3:
            substring = input("\nEnter the ending Substring: ")
            if string.endswith(substring):
                print(f"{string} is ending with {substring}")
            else:
                print(f"{string} is not ending with {substring}")

        case 4:
            # capitalized_string = string.title()
            capitalized_string = ' '.join(word.capitalize() for word in string.split())
            print(capitalized_string)

        case 5:
            second_str = input("\nEnter the other String: ")
            str_1 = string.replace(" ", "").lower()
            str_2 = second_str.replace(" ", "").lower()

            if (sorted(str_1) == sorted(str_2)):
                print(f"{second_str} is a Anagram of {string}")
            else:
                print(f"{second_str} is not a Anagram of {string}")

        case 6:
            vowels = "aeiou"
            removed_vowel = ''.join([char for char in string if char.lower() not in vowels])
            print(f"\nString after removing the vowels is -> {removed_vowel}")

        case 7:
            longest_word_length = 0
            longest_word = ''
            for word in string.split():
                if len(word) > longest_word_length:
                    longest_word_length = len(word)
                    longest_word = word
            print(f"Longest Word -> {longest_word}")

        case 8:
            print("\nExiting...")
            exit()

        case default:
            print("\nInvalid Input!")
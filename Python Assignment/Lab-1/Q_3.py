# Leapyear

year = int(input("Enter the Year: "))

if year % 100 == 0:
    if year % 400 == 0:
        print(f"{year} is a Leap Year")
        exit()
else:
    if year % 4 == 0:
        print(f"{year} is a Leap Year")
        exit()
print(f"{year} is not a Leap Year")

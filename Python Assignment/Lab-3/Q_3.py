# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(list):
    for item in list:
        print(item)

print("Enter data for the List(Type '0' to exit): ")
my_list = []
while True:
    data = input()
    if data == '0':
        break
    my_list.append(data)

print("\nPrinting the List:")
print_list(my_list)
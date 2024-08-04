# Write a Java program to generate all combination of 1, 2, or 3 using loop

def generate_combinations():
    numbers = [1, 2, 3]

    # Generate all combinations of length 1
    print("Combinations of length 1:")
    for i in range(len(numbers)):
        print(numbers[i])

    # Generate all combinations of length 2
    print("\nCombinations of length 2:")
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            print(numbers[i], numbers[j])

    # Generate all combinations of length 3
    print("\nCombinations of length 3:")
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            for k in range(len(numbers)):
                print(numbers[i], numbers[j], numbers[k])

generate_combinations()

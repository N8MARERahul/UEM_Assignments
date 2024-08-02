# Print the pattern upto N lines:
#   1 2        1 2 3        1 2 3 4
#   4 3        8 9 4        12 13 14 5
#              7 6 5        11 16 15 6
#                           10 9 8 7
#  N = 2        N = 3          N = 4

def print_spiral_pattern(N):
    # Create an N x N matrix filled with zeros
    matrix = [[0] * N for _ in range(N)]

    # Define directions for spiral movement: right, down, left, up
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    current_direction = 0  # Start moving right

    # Initialize starting position
    row, col = 0, 0

    # Fill the matrix with numbers 1 to N*N
    for num in range(1, N*N + 1):
        matrix[row][col] = num  # Place the current number in the matrix

        # Calculate next position
        next_row = row + directions[current_direction][0]
        next_col = col + directions[current_direction][1]

        # Check if the next position is within bounds and not already filled
        if 0 <= next_row < N and 0 <= next_col < N and matrix[next_row][next_col] == 0:
            # Move to the next position
            row, col = next_row, next_col
        else:
            # Change direction (turn right)
            current_direction = (current_direction + 1) % 4
            row += directions[current_direction][0]
            col += directions[current_direction][1]

    # Print the matrix in the desired format
    for line in matrix:
        print(" ".join(map(str, line)))

def main():
    N = int(input("Enter the number of lines (N): "))
    if N <= 0:
        print("N must be a positive integer.")
        exit()
    print_spiral_pattern(N)

if __name__ == "__main__":
    main()

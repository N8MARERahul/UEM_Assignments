# Print a number as a 8 segment display N Lines:

#   _     _     
#   _|    _|    |_|
#  |_     _|      |
# 

# N=2    N=3    N=4


def print_pattern(str):
    print(" --") if str[0] == '1' else print("   ")
    print("|", end="  ") if str[5] == '1' else print("   ", end="")
    print("|") if str[1] == '1' else print(" ")
    print(" --") if str[6] == '1' else print("   ")
    print("|", end="  ") if str[4] == '1' else print("   ", end="")
    print("|") if str[2] == '1' else print(" ")
    print(" --") if str[3] == '1' else print("   ")

num = input("Enter the digit: ")

#      a
#       -
# f   |  | b
# g    -
# e  |   | c
#      -
#     d

segment = {
    '0' : '1111110',
    '1' : '0110000',
    '2' : '1101101',
    '3' : '1111001',
    '4' : '0110011',
    '5' : '1011011',
    '6' : '1011111',
    '7' : '1110000',
    '8' : '1111111',
    '9' : '1111011'
}
print_pattern(segment.get(num))
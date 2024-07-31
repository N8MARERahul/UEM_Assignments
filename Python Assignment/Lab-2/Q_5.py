# Compute a)sin of 60 degree b)cos of pi c)sin(0.8660254037844386) d)tan of 90 degree

import math

# a) Sin of 60 degrees
sin_60 = math.sin(math.radians(60))
print(f"Sin of 60 degrees is: {sin_60}")

# b) Cos of pi
cos_pi = math.cos(math.pi)
print(f"Cos of pi is: {cos_pi}")

# c) Sin of 0.8660254037844386
sin_value = math.sin(0.8660254037844386)
print(f"Sin of 0.8660254037844386 is: {sin_value}")

# d) Tan of 90 degrees
try:
    tan_90 = math.tan(math.radians(90))
    print(f"Tan of 90 degrees is: {tan_90}")
except ValueError:
    print("Tan of 90 degrees is undefined.")

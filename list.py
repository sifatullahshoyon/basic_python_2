# List, array, Collection is same(simple terms)

# index:  0    1    2  3   4   5
numbers = [24, 56, 54, 81, 36, 91]
# r index: -6  -5  -4  -3  -2   -1   Reverse Index

print(numbers[3], numbers[-4])

# list(start : end) Start from the start index and stops before the end index
print(numbers[1:5])

# List(start : end : step)
print(numbers[1 : 5: 1])
print(numbers[1 : 5: 2])
print(numbers[1 : 5: -1])
print(numbers[5 : 1: -1])
print(numbers[5 : 1: -2])
print(numbers[2:]) # End ar idx na bolle ekdom ses porjonto cole jabe
print(numbers[:4]) # first ar idx na bolle ekdom first porjonto cole jabe
print(numbers[:]) # kisu na boole ekbare sob print kore felbe. Shortcut to copy a list
print(numbers[: : -1]) # Full array Reverse. Shortcut to reverse a list
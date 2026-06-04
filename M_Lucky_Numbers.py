a, b = input().split()

A = int(a)
B = int(b)

found = False

for i in range(A, B + 1):
    num_str = str(i)

    lucky_number = True

    for digit in num_str:
        if digit != '4' and digit != '7':
            lucky_number = False
            break

    if lucky_number:
        print(i, end=" ")
        found = True

if not found:
    print(-1)
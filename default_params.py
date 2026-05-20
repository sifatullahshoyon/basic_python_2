def sum(num1, num2, num3 = 0, num4 = 0, num5 = 0):
    return num1 + num2 + num3 + num4 + num5

total = sum(82, 52, 154, 6)
# print("Total :", total)

# Args
def sum_all_numbers(num1 = 0, num2 = 0, *args): # args এর বদলে যে কোন নামই ব্যবহার করা যাবে। যেমনঃ numbers
    print(args)
    sum = 0
    for num in args:
        print("num :", num)
        sum += num
    return sum

output = sum_all_numbers(66, 74, 54, 21, 91, 22)
print("All Sum :", output)
def full_name(first, last):
    name = f'Full Name Is: {first} {last}'
    return name

# take paramaters in order(serial wise)
# name = full_name('kodom', 'ali')

# take paramaters in unorder 
name = full_name(last= 'johir', first='kodom')

# print(name)

# def famous(**kargs)
def famous_name(first, last, **addition):
    name = f'Full Name: {first} {last}'
    # print(addition['title'])
    for key, value in addition.items():
        print(key, value)
    return name

popular_name = famous_name(first='Tahar', title='khajay aga', last='Ali', addition="morside mokammel")

print(popular_name)

# def function_name(num1, num2, *args, **kargs):

# return multiple things from an array
def a_lot(num1, num2):
    sum = num1 + num2
    mul = num2 * num1
    remain = num1 - num2
    # return [sum, mul, remain]
    return sum, mul, remain

everything = a_lot(55, 21)
print(everything)
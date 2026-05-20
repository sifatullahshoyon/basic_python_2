# Global Variable
blance = 3000

def buy_things(item = 0, price = 0):
    # local Variable
    global blance
    print("Before Global. Blance inside the func: ", blance)
    sunglasses = blance - price
    print(sunglasses)
    blance = sunglasses
    print("After Global. Blance inside the func: ", blance)

result = buy_things(price= 1000)
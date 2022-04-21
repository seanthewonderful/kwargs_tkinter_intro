def add(*args):
    list = []
    for n in args:
        list.append(n)
    return sum(list)
    # # Or
    # sum = 0
    # for n in args:
    #     sum += n
    # return sum

# print(add(1,2,3,4,5))


def calculate(n, **kwargs):
    # print(kwargs)
    # for key, value in kwargs.items():
    #     print(key)
    #     print(value)
    # print(kwargs["add"])
    n += kwargs["add"]
    n *= kwargs["multiply"]
    print(n)
    
# calculate(2, add=3, multiply=5)


class Car:
    
    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.power = kw.get("power")
    
my_car = Car(make="Tesla", model="3", color="red")
print(my_car.power)
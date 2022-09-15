from .CarSprite import CarSprite

class Car1(CarSprite):
    def __init__(self, name):
        self.name = name
        self.max_speed = 1
        self.angle = 0
        self.speed = 0
        self.turn_speed = 1

    def __str__(self):
        return "Car1: " + self.name

class Car2(CarSprite):
    def __init__(self, name):
        self.name = name
        self.max_speed = 2
        self.angle = 0
        self.speed = 0
        self.turn_speed = 2

    def __str__(self):
        return "Car2: " + self.name

# continue until 72 cars

class Car3(CarSprite):
    def __init__(self, name):
        self.name = name
        self.max_speed = 3
        self.angle = 0
        self.speed = 0
        self.turn_speed = 3

    def __str__(self):
        return "Car3: " + self.name

class Car4(CarSprite):
    def __init__(self, name):
        self.name = name
        self.max_speed = 4
        self.angle = 0
        self.speed = 0
        self.turn_speed = 4

    def __str__(self):
        return "Car4: " + self.name

class Car5(CarSprite):
    def __init__(self, name):
        self.name = name
        self.max_speed = 5
        self.angle = 0
        self.speed = 0
        self.turn_speed = 5

    def __str__(self):
        return "Car5: " + self.name

class Car6(CarSprite):
    def __init__(self, name):
        self.name = name
        self.max_speed = 6
        self.angle = 0
        self.speed = 0
        self.turn_speed = 6

    def __str__(self):
        return "Car6: " + self.name

def number_to_class(number):
    return {
        1: Car1,
        2: Car2,
        3: Car3,
        4: Car4,
        5: Car5,
        6: Car6,
    }[number]

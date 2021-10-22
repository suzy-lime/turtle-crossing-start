import turtle
from turtle import Turtle
from random import choice, randint

COLORS = [(231, 206, 83), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19), (232, 221, 226),
          (30, 110, 159), (235, 81, 44), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144),
          (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98), (83, 17, 24),
          (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68),
          (227, 171, 162), (73, 135, 188), (172, 204, 174)]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        turtle.colormode(255)
        self.start_speed = 5
        self.COLORS = [(231, 206, 83), (229, 147, 85), (217, 227, 219), (119, 166, 186), (160, 13, 19), (232, 221, 226),
                       (30, 110, 159), (235, 81, 44), (5, 99, 37), (176, 19, 14), (187, 187, 25), (121, 177, 144),
                       (207, 62, 22), (23, 132, 41), (245, 201, 4), (10, 42, 77), (13, 64, 41), (137, 83, 98),
                       (83, 17, 24),
                       (46, 168, 74), (3, 66, 140), (173, 133, 149), (36, 25, 21), (45, 151, 198), (220, 63, 68),
                       (227, 171, 162), (73, 135, 188), (172, 204, 174)]

    def create_car(self):
        random_change = randint(1, 6)
        if random_change == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(choice(self.COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3, outline=0)
            random_y = randint(-240, 250)
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.start_speed)

    def increase_speed(self):
        self.start_speed += 3
        random_change = randint(1, 20)
        if random_change == 1:
            new_car = Turtle()
            new_car.penup()
            new_car.color(choice(self.COLORS))
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=3, outline=0)
            random_y = randint(-240, 250)
            new_car.goto(310, random_y)
            self.all_cars.append(new_car)

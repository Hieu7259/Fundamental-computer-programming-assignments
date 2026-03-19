class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0
    def get_description(self):
        return f"{self.registration_number} {self.maximum_speed} {self.current_speed} {self.travelled_distance}"

    def accelerate(self, speed_increase):
        self.current_speed += speed_increase
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed

    def brake(self, speed_decrease):
        self.current_speed -= speed_decrease
        if self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

import random
racing_cars = [Car(f"ABC-{i+1}", random.randint(150, 200)) for i in range(10)]
while not any(c.travelled_distance >= 10000 for c in racing_cars):
    for c in racing_cars:
        c.accelerate(random.randint(-10, 15))
        c.drive(1)
for car in racing_cars:
    print(f"{car.registration_number:<10} {car.maximum_speed:<10} {car.travelled_distance:<10}")
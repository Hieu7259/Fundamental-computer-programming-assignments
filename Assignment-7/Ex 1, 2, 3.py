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

new_car = Car("ABC-123", 142)
print(new_car.get_description())
new_car.accelerate(30)
new_car.accelerate(70)
new_car.accelerate(50)
print("The car's current speed is:", new_car.current_speed)
new_car.drive(2)
print("The car's travelled distance is:", new_car.travelled_distance)
new_car.brake(200)
print("The car's current speed after braking is:", new_car.current_speed)

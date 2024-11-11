class Car:
  def __init__(self, model, speed, color):
    self.model = model
    self.speed = speed
    self.color = color


car_1 = Car("Toyota", 267, "black")
car_2 = Car("M7", 342, "red")
car_3 = Car("Frary", 563, "blue")

print(f"The first car's model is {car_1.model}")
print(f"The second car's speed is {car_2.speed}")
print(f"The third car's color is {car_3.color}")


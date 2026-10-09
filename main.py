class Robot:
    def __init__(self, name, battery, speed):
        self.name = name
        self.battery = battery
        self.speed = speed

    def show_info(self):
        print(f"Robot: {self.name}")
        print(f"Battery: {self.battery}%")
        print(f"Speed: {self.speed} m/s")

    def move(self):
        print(f"{self.name} is moving...")

    def charge(self):
        self.battery = 100
        print(f"Battery charged: {self.battery}%")


robot = Robot("Sufi", 80 , 5)
robot.show_info()
robot.move()
robot.charge()




### Mellim necedi?

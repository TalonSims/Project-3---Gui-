import random

class Car:
    def __init__(self):
        self.odometer_val = random.randint(0, 999999)
        self.fuel_efficiency = random.uniform(5, 10) # [:3]
        self.max_gas = random.randint(10, 16)
        self.current_gas = random.uniform((self.max_gas-5),self.max_gas) # [:3]
        self.speed = 0
    
    def set_speed(self, speed):
        self.speed = speed
        print(type(speed).__name__)
        return self.speed
       

    def increment_odo(self, duration, current_speed):
        self.speed = current_speed
        # print(type(current_speed).__name__)
        # print(type(duration).__name__)
        miles = current_speed * duration / 60 #  miles = (current_speed)(1/60)(duration)
        self.odometer_val += miles 
        return self.odometer_val

    def refuel_gas (self, refuel_amount):


        self.current_gas += abs(refuel_amount)
        if self.current_gas > self.max_gas:
            self.current_gas = self.max_gas

def set_duration():
    duration = int(input("How long would you like to travel at this speed? "))
    return duration      

my_car = Car()
x = my_car.increment_odo(set_duration(), my_car.set_speed(int(input("How fast would you like to travel?"))))


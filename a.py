class Vehicle:
  def __init__(self, make, color, max_speed, current_speed, current_gear):
    self.__make = make
    self.__color = color
    self.__max_speed = max_speed
    self.__current_speed = current_speed
    self.__current_gear = current_gear
    self.__max_gear = 4
  def get_make(self):
    return self.__make
  def get_color(self):
    return self.__color
  def get_max_speed(self):
    return self.__max_speed    
  def get_current_speed(self):
    return self.__current_speed
  def get_current_gear(self):
    return self.__current_gear
  def get_max_gear(self):
    return self.__max_gear
  def set_make(self, make):
    self.__make = make
  def set_color(self, color):
    self.__color = color
  def set_max_speed(self, max_speed):
    self.__max_speed = max_speed
  def set_current_speed(self, current_speed):
    self.__current_speed = current_speed
  def set_current_gear(self, current_gear):
    self.__current_gear = current_gear
  def show_details(self):
    print(self.__dict__)
  def accelerate(self, raised_speed):
    self.__current_speed += raised_speed
    if raised_speed <= 0:
      print("In order to accelerate you need a higher speed than 0.")
    elif self.__current_speed <= self.__max_speed:
      print(f"Current speed: {self.__current_speed}km/h. You are within the speed limit (Speed limit: {self.__max_speed}km/h).")
    else:
      print(f"Current speed: {self.__current_speed}km/h. You cannot exceed the speed limit ({self.__max_speed}km/h)!")
  def decelerate(self, lowered_speed):
    if lowered_speed <= self.current_speed:
      self.current_speed -= lowered_speed
      print(f"Current speed: {self.current_speed}km/h.")
    else:
      print("Error! Invalid input!")
  def up_shift(self):
    self.current_gear += 1
    if self.current_gear <= self.max_gear:
      print(f"Current gear: {self.current_gear}.")
    else:
      print("You cannot exceed the gear limit!")
  def down_shift(self, gear = None):
    if gear == None:
      self.current_gear -= 1
      if self.current_gear > 0:
        print(f"Current gear: {self.current_gear}.")
      else:
        print("No lower gear!")
    else:
      if gear == 0:
        print("Current gear: Neutral.")
      elif gear == -1:
        print("Current gear: Reverse.")
      else:
        print("Error! Invalid input!")

class Motorcycle(Vehicle):
  def __init__(self, make, color, max_speed, current_speed, current_gear):
    Vehicle.__init__(self, make, color, max_speed, current_speed, current_gear)
    self.__max_gear = 6
    self.__nr_of_wheels = 2
  def accelerate(self, raised_speed):
    self.current_speed += raised_speed
    if raised_speed <= 0:
      print("In order to accelerate you need a higher speed than 0.")
    elif self.current_speed <= self.max_speed:
      print(f"Current speed of motorcycle: {self.current_speed}km/h. You are within the speed limit (Speed limit: {self.max_speed}km/h).")
    else:
      print(f"Current speed of motorcycle: {self.current_speed}km/h. You cannot exceed the speed limit ({self.max_speed}km/h)!")
  def decelerate(self, lowered_speed):
    if lowered_speed <= self.current_speed:
      self.current_speed -= lowered_speed
      print(f"Current speed of motorcycle: {self.current_speed}km/h.")
    else:
      print("Error! Invalid input!")
  def up_shift(self):
    self.current_gear += 1
    if self.current_gear <= self.max_gear:
      print(f"Current gear of motorcycle: {self.current_gear}.")
    else:
      print("You cannot exceed the gear limit!")
  def down_shift(self, gear = None):
    if gear == None:
      self.current_gear -= 1
      if self.current_gear > 0:
        print(f"Current gear of motorcycle: {self.current_gear}.")
      else:
        print("No lower gear!")
    else:
      if gear == 0:
        print("Current gear of motorcycle: Neutral.")
      elif gear == -1:
        print("Current gear of motorcycle: Reverse.")
      else:
        print("Error! Invalid input!")

class Car(Vehicle):
  def __init__(self, make, color, max_speed, current_speed, current_gear):
    Vehicle.__init__(self, make, color, max_speed, current_speed, current_gear)
    self.max_gear = 7
    self.nr_of_wheels = 4
  def accelerate(self, raised_speed):
    self.current_speed += raised_speed
    if raised_speed <= 0:
      print("In order to accelerate you need a higher speed than 0.")
    elif self.current_speed <= self.max_speed:
      print(f"Current speed of car: {self.current_speed}km/h. You are within the speed limit (Speed limit: {self.max_speed}km/h).")
    else:
      print(f"Current speed of car: {self.current_speed}km/h. You cannot exceed the speed limit ({self.max_speed}km/h)!")
  def decelerate(self, lowered_speed):
    if lowered_speed <= self.current_speed:
      self.current_speed -= lowered_speed
      print(f"Current speed of car: {self.current_speed}km/h.")
    else:
      print("Error! Invalid input!")
  def up_shift(self):
    self.current_gear += 1
    if self.current_gear <= self.max_gear:
      print(f"Current gear of car: {self.current_gear}.")
    else:
      print("You cannot exceed the gear limit!")
  def down_shift(self, gear = None):
    if gear == None:
      self.current_gear -= 1
      if self.current_gear > 0:
        print(f"Current gear of car: {self.current_gear}.")
      else:
        print("No lower gear!")
    else:
      if gear == 0:
        print("Current gear of car: Neutral.")
      elif gear == -1:
        print("Current gear of car: Reverse.")
      else:
        print("Error! Invalid input!")
"""
HINT the for loop should look like this:
for vehicle in [my_vehicle, my_motorbike, my_car]:
#call the functions using the variable “vehicle” to test polymorphism
vehicle.accelerate(50)"""

vehicle = Vehicle("IVECO", "blue", 180, 40, 2)
vehicle.accelerate(100)
# motorcycle = Motorcycle("BMW", "black", 450, 200, 3)
# car = Car("Ferrari", "red", 480, 300, 5)

# for vehicle in [vehicle]:
#   vehicle.accelerate(100)
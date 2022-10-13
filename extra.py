
# 1a) Create a class Vehicle with the following attributes:name, max_speed,mileage. Define attribute color to be “White” for all the vehicles.
#  Create two instances to confirm it works.
# b) Create a method that congratulates the owner  for buying that kind of a car. Include the car’s name, color,max_speed,mileage.
# c)Create a method that returns the car name and its capacity.
class Vehicle:
  color="White"
  def __init__(self,name,max_speed,mileage):
      self.name= name
      self.max_speed = max_speed
      self.mileage = mileage

  def car(self):
      return f"Lona your car is {self.name} with {self.mileage} mileage and its max speed {self.max_speed}"

  def congratulate(self):
     
      return f"Congratulations upon purchasing a {self.color} {self.name} with {self.mileage} milage and max speed of {self.max_speed}"

  def capacity(self,capacity):
     
     return f"Your {self.name} capacity is {capacity}"


# Write a function for checking the speed of drivers. This function should have one parameter: speed.
# If speed is less than 70, it should print “Ok”.
# Otherwise, for every 5km above the speed limit (70), it should give the driver one demerit point and print the total number of demerit points. For example, if the speed is 80, it should print: “Points: 2”.
# If the driver gets more than 12 points, the function should print: “License suspended”



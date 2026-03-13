class Vehicle:

    def __init__ (self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

modelx = Vehicle(560,20)
modely = Vehicle(600,22)

print ("Maximum Speed of Model~X is:",modelx.max_speed)
print ("Mileage of Model~X is:",modelx.mileage)

print ("Maximum Speed of Model~Y is:",modely.max_speed)
print ("Mileage of Model~Y is:",modely.mileage)
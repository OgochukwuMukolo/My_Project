from random import randint

fuel = randint(10, 25)

miles = randint(200, 400)

# calculate MPG assuming car manufacturers over estimate
print("The car can travel " + str(miles // fuel) + " miles per gallon.")

# displays the number of gallons of fuel that the car's fuel tank can hold
print("The car's fuel tank can hold " + str(fuel) + " gallons.")

# displays the number of miles that the car can travel on a full tank
print("The car can travel " + str(miles) + " miles on a full tank.")
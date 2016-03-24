# Converts Richter Scale measurement into energy in Joules
# 1.0, 5.0, 9.1 (Indonesia), 9.2 (Alaska), 9.5 (Chile)
# Then program prompts for user input to enter a Richter Scale measurement
# accepts floating point value
# converts it into energy in Joules, and in tons of exploded TNT

import cmath

quakes = [1.0, 5.0, 9.1, 9.2, 9.5]

for scale in quakes:
	convert = (1.5 * scale) + 4.8
	energy = pow(10, convert)
	print ("For an earthquake on the Richter scale of {0} the energy produced is: {1} Joules".format(scale, energy))

print ("Now, let's convert your Richter Scale measurement to energy in Joules & tons of exploded TNT!")

user_scale = float(input("Enter a Richter Scale value: "))

if user_scale < 10:
	convert = (1.5 * user_scale) + 4.8
	energy = pow(10, convert)
	tons = energy / (4.184 * pow(10,9))
	print ("Your Richter Scale value of {0} yields {1}J of energy and {2} tons of exploded TNT!".format(user_scale, energy, tons))
else:
	print("Error. Richter Scale values tend to range from 0 to 9 (although no real upper limit exists)")
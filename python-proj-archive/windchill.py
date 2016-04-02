# Calculation of Wind Chill Temperature Index

def calculate_wcti(air_temp, wind_speed):
	wct_index = 35.74 + 0.6215 * air_temp \
				- 35.75 * wind_speed**0.16 \
				+ 0.4275 * air_temp * wind_speed**0.16
	return wct_index

print("For air temp 10.0 degrees Fahrenheit and 15 MPH wind speed,\
	wind chill temperature index is: {0}".format(calculate_wcti(10.0, 15)))

print("For air temp 0.0 degrees Fahrenheit and 25 MPH wind speed,\
	wind chill temperature index is: {0}".format(calculate_wcti(0.0, 25)))

print("For air temp -10 degrees Fahrenheit and 35 MPH wind speed,\
	wind chill temperature index is: {0}".format(calculate_wcti(-10.0, 35)))

print("\nNow let's do some measurements with you.\n")

user_air_temp = float(input("Enter an air temp measurement: "))
user_wind_speed = float(input("Enter a wind speed measurement: "))

print("Your Wind Chill Temperature Index is: {0}".format(calculate_wcti(user_air_temp, user_wind_speed)))

# Calculation of Wind Chill Temperature Index

def calculate_wcti(air_temp, wind_speed):
	wct_index = 35.74 + 0.6215 * air_temp \
				- 35.75 * wind_speed**0.16 \
				+ 0.4275 * air_temp * wind_speed**0.16
	return wct_index

# Assignment Values
print("\nTemperature (degrees F): 10.0")
print("Wind speed (MPH): 15.0")
print("Wind Chill Temperature Index: {0}".format(calculate_wcti(10.0, 15)))

print("\nTemperature (degrees F): 10.0")
print("Wind speed (MPH): 15.0")
print("Wind Chill Temperature Index: {0}".format(calculate_wcti(0.0, 25)))

print("\nTemperature (degrees F): 10.0")
print("Wind speed (MPH): 15.0")
print("Wind Chill Temperature Index: {0}".format(calculate_wcti(-10.0, 35)))

# User input Values
user_air_temp = float(input("\nPlease enter the Temperature (degrees F): "))
user_wind_speed = float(input("\nPlease enter the Wind Speed (MPH): "))

print("\nTemperature (degrees F): {0}".format(user_air_temp))
print("Wind Speed (MPH): {0}".format(user_wind_speed))
print("Wind Chill Temperature Index: {0}".format(calculate_wcti(user_air_temp, user_wind_speed)))

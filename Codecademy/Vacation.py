def hotel_costs(nights):
	return 140*nights

def plane_ride_cost(city):
	if city == 'Charlotte':
		return 183
	elif city == 'Tampa':
		return 220
	elif city == 'Pittsburgh'
		return 222
	elif city == 'Los Angeles'
		return 475

def rental_car_cost(days):
	total = 40*days

	if days >= 7:
		total = total - 50
	elif days >= 3:
		total = total - 20
	return total

def trip_cost(city, days, spending_money):
	sum = hotel_costs(days) + plane_ride_cost(city) + rental_car_cost(days) + spending_money

print trip_cost('Los Angeles', 5, 600)
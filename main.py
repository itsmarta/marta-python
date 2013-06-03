from getVehicles import getBuses, getTrains

def main():

	# Input function to obtain route number from user
	route = input('\n\n*******Get Buses*******\n\nPlease enter a route number (leave blank for all routes):\n\n')
	
	# Call getBuses function with user-defined route number
	getBuses(route)
	
	# Input function to obtain route number from user
	station = input('\n\n*******Get Trains*******\n\nPlease enter a station (leave blank for all trains):\n\n')
	
	# Call getBuses function with user-defined route number
	getTrains(station)

def usage():
	print("\n\n--help\n\nThis is how you use it.\n\n")

if __name__ == '__main__':
	main()
import json
from getVehicles import getBuses, getTrains
def main():
	
	route = ""
	
	# Input function to obtain route number from user
	route = getInput("route")
	
	# Call getBuses function with user-defined route number
	getBuses(route)
	
	station = ""
	
	# Input function to obtain route number from user
	station = getInput("station")
	
	# Call getBuses function with user-defined route number
	getTrains(station)

def usage():
	print("\n\n--help\n\nThis is how you use it.\n\n")

def getInput(type):
	vehicle = ""
	if (type == "route"):
		vehicle = "Buses"
	else:
		vehicle = "Trains"
	message = '\n\n*******Get' + vehicle + '*******\n\nPlease enter a route number\n\n(leave blank for all routes)\n\n(type \'?\' for a list of ' + type + 's)\n\n'
	
	userInput = input(message)

	if (userInput == "?"):
		showJSON(type)
		userInput = getInput(type)

	return userInput
	
def showJSON(type):
	json_data = open('json')

	data = json.load(json_data)
	print("\n\nList of " + type + "s:\n")
	for i in data[type]:
		print(i)
	json_data.close()

if __name__ == '__main__':
	main()
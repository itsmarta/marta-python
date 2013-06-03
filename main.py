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

def getInput(mode):
	vehicle = ""
	if (mode == "route"):
		vehicle = "Buses"
	else:
		vehicle = "Trains"
	message = '\n\n*******Get' + vehicle + '*******\n\nPlease enter a route number\n\n(leave blank for all routes)\n\n(type \'?\' for a list of ' + mode + 's)\n\n'
	
	userInput = input(message)

	if (userInput == "?"):
		showJSON(mode)
		userInput = getInput(mode)

	return userInput
	
def showJSON(mode):
	json_data = open('json')

	data = json.load(json_data)
	print("\n\nList of " + mode + "s:\n")
	for i in data[mode]:
		print(i)
	json_data.close()

if __name__ == '__main__':
	main()
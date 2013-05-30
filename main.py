from getBuses import getBuses

def main():
	
	# Input function to obtain route number from user
	route = input('\n\nPlease enter a route number (leave blank for all routes):\n\n')
	
	# Call getBuses function with user-defined route number
	getBuses(route)

if __name__ == '__main__':
	main()
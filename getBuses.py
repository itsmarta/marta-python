#!/usr/bin/env python

#import urllib2
import urllib.request
import json
import datetime
import sys

# By default, function searches for all MARTA routes.
def getBuses(route=''):
	
	#Base URL for MARTA API
	base = 'http://developer.itsmarta.com/BRDRestService/BRDRestService.svc/'
	
	# If user does not input a value for route number, use 'GetAllBus' API call
	if route == '':
		query = 'GetAllBus'
	
	# Else, use 'GetBusByRoute' API call with user-defined route number
	else:
		query = 'GetBusByRoute/' + route
	
	# Formulate URL request and format response as json object
	response = urllib.request.urlopen(base + query, timeout=30)
	str_response = response.readall().decode('utf-8')
	buses = json.loads(str_response)
	
	# Prints entirety of json response
	#print(buses)
	
	# For each bus in response, print a few pieces of data.
	for bus in buses:
		print(bus['ROUTE'] + '  LAT:' + bus['LATITUDE'] + '  LON:' + bus['LONGITUDE'] + '  ADHER:' + bus['ADHERENCE'] + '  VEHICLE:' + bus['VEHICLE'] + '\n')

def getTrains(station=''):
	
	#Base URL for MARTA API
	base = 'http://gispd/RTTService/RTTService.svc/'
	
	# If user does not input a value for route number, use 'GetAllBus' API call
	if station == '':
		query = 'GetAllTrains'
	
	# Else, use 'GetBusByRoute' API call with user-defined route number
	else:
		query = 'GetTrainByStation/' + station
	
	# Formulate URL request and format response as json object
	response = urllib.request.urlopen(base + query, timeout=30)
	str_response = response.readall().decode('utf-8')
	trains = json.loads(str_response)
	
	# Prints entirety of json response
	#print(buses)
	
	# For each bus in response, print a few pieces of data.
	for train in trains:
		print(train['Direction'] + '  LAT:' + train['Latitude'] + '  LON:' + train['Longitude'] + '  LOCATION:' + train['Location'] + '  TRACK:' + train['Track'] + '\n' + '  ID:' + train['Train_ID'] + '\n')

	
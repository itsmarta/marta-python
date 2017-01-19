import requests
from json import loads
from os import getenv
from pprint import pprint

from vehicles import Bus, Train

API_KEY = getenv('MARTA_API_KEY', None)
BASE_URL = 'http://developer.itsmarta.com/'
TRAIN_PATH = '/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals'
BUS_PATH = '/BRDRestService/RestBusRealTimeService/GetAllBus'


def get_all_trains():
    response = requests.get('{}{}?apikey={}'.format(BASE_URL, TRAIN_PATH, API_KEY))
    data = loads(response.text)
    return [Train(t) for t in data]


def get_all_buses():
    response = requests.get('{}{}?apikey={}'.format(BASE_URL, BUS_PATH, API_KEY))
    data = loads(response.text)
    return [Bus(b) for b in data]


if __name__ == '__main__':
    buses = get_all_buses()
    pprint(buses[0].__dict__)


import requests
from json import loads
from os import getenv
from pprint import pprint

from .vehicles import Bus, Train

API_KEY = getenv('MARTA_API_KEY', None)
BASE_URL = 'http://developer.itsmarta.com/'
TRAIN_PATH = '/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals'
BUS_PATH = '/BRDRestService/RestBusRealTimeService/GetAllBus'
BUS_ROUTE_PATH = '/BRDRestService/RestBusRealTimeService/GetBusByRoute/'


def get_trains(line=None, station=None, destination=None):
    response = requests.get('{}{}?apikey={}'.format(BASE_URL, TRAIN_PATH, API_KEY))
    data = loads(response.text)
    trains = [Train(t) for t in data]

    if line is not None:
        trains = [t for t in trains if t.line == line]

    if station is not None:
        trains = [t for t in trains if t.station == station]

    if destination is not None:
        trains = [t for t in trains if t.destination == destination]

    return trains


def get_buses(route=None):
    if route is not None:
        url = '{}{}/{}?apikey={}'.format(BASE_URL, BUS_ROUTE_PATH, str(route), API_KEY)
    else:
        url = '{}{}?apikey={}'.format(BASE_URL, BUS_PATH, API_KEY)

    response = requests.get(url)
    data = loads(response.text)
    return [Bus(b) for b in data]


def main():
    trains = get_trains()
    pprint(trains[0].__dict__)


if __name__ == '__main__':
    main()

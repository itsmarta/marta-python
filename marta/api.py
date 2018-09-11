import requests
import requests_cache
from json import loads, JSONDecodeError
from os import getenv
from functools import wraps

from .exceptions import APIKeyError
from .vehicles import Bus, Train

_API_KEY = getenv('MARTA_API_KEY')
_CACHE_EXPIRE = int(getenv('MARTA_CACHE_EXPIRE', 30))
_BASE_URL = 'http://developer.itsmarta.com'
_TRAIN_PATH = '/RealtimeTrain/RestServiceNextTrain/GetRealtimeArrivals'
_BUS_PATH = '/BRDRestService/RestBusRealTimeService/GetAllBus'
_BUS_ROUTE_PATH = '/BRDRestService/RestBusRealTimeService/GetBusByRoute/'

requests_cache.install_cache('marta_api_cache', backend='sqlite', expire_after=_CACHE_EXPIRE)


def require_api_key(func):
    """
    Decorator to ensure an API key is present
    """
    @wraps(func)
    def with_key(*args, **kwargs):
        api_key = kwargs.get('api_key')
        if not api_key and not _API_KEY:
            raise APIKeyError()
        kwargs['api_key'] = api_key if api_key else _API_KEY
        return func(*args, **kwargs)
    return with_key


@require_api_key
def get_trains(line=None, station=None, destination=None, api_key=None):
    """
    Query API for train information
    :param line (str): train line identifier filter (red, gold, green, or blue)
    :param station (str): train station filter
    :param destination (str): destination filter
    :param api_key (str): API key to override environment variable
    :return: list of Train objects
    """
    endpoint = '{}{}?apikey={}'.format(_BASE_URL, _TRAIN_PATH, api_key)
    response = requests.get(endpoint)

    if response.status_code == 401 or response.status_code == 403:
        raise APIKeyError('Your API key seems to be invalid. Try visiting {}.'.format(endpoint))

    data = loads(response.text)
    trains = [Train(t) for t in data]

    trains = [t for t in trains if
              (t.line.lower() == line.lower() if line is not None else True) and
              (t.station.lower() == station.lower() if station is not None else True) and
              (t.destination.lower() == destination.lower() if destination is not None else True)]

    return trains


@require_api_key
def get_buses(route=None, api_key=None):
    """
    Query API for bus information
    :param route (int): route number
    :param api_key (str): API key to override environment variable
    :return: list of Bus objects
    """
    if route is not None:
        url = '{}{}/{}?apikey={}'.format(_BASE_URL, _BUS_ROUTE_PATH, str(route), api_key)
    else:
        url = '{}{}?apikey={}'.format(_BASE_URL, _BUS_PATH, _API_KEY)

    response = requests.get(url)
    data = loads(response.text)
    return [Bus(b) for b in data]

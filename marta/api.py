from typing import List, Union

import requests
import requests_cache
import json
from os import getenv
from functools import wraps

from .exceptions import APIKeyError, InvalidDirectionError
from .vehicles import Bus, Train

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
    def with_key(self, *args, **kwargs):
        if not kwargs.get('api_key'):
            if not self._api_key:
                raise APIKeyError()
            kwargs['api_key'] = self._api_key
        return func(self, *args, **kwargs)

    return with_key

def _convert_direction(user_direction: str, vehicle_type: str = 'bus') -> Union[str, None]:
    if not user_direction:
        return None
    if vehicle_type == 'bus':
        if user_direction.lower().startswith('n'):
            return 'Northbound'
        elif user_direction.lower().startswith('s'):
            return 'Southbound'
        elif user_direction.lower().startswith('e'):
            return 'Eastbound'
        elif user_direction.lower().startswith('w'):
            return 'Westbound'
        else:
            raise InvalidDirectionError(direction_provided=user_direction)
    elif vehicle_type == 'train':
        if user_direction.lower().startswith('n'):
            return 'N'
        elif user_direction.lower().startswith('s'):
            return 'S'
        elif user_direction.lower().startswith('e'):
            return 'E'
        elif user_direction.lower().startswith('w'):
            return 'W'
        else:
            raise InvalidDirectionError(direction_provided=user_direction)
    else:
        return user_direction


def _get_data(endpoint: str, api_key: str) -> dict:
    url = f'{_BASE_URL}{endpoint}?apikey={api_key}'
    response = requests.get(url)
    if response.status_code == 401 or response.status_code == 403:
        raise APIKeyError(f'Your API key seems to be invalid. Try visiting {url}.')
    return json.loads(response.text)

def _filter_response(response: dict, filters: dict) -> List[dict]:
    valid_items = []
    for item in response:
        valid = True
        for filter_key, filter_value in filters.items():
            if filter_value: # ignore if the filter value doesn't exist
                if not item.get(filter_key): # don't penalize if item doesn't have a filter_key
                    pass
                elif str(item[filter_key]).lower() != str(filter_value).lower():
                    # lower all values to avoid case issues
                    valid = False
        if valid:
            valid_items.append(item)
    return valid_items

class MARTA:
    def __init__(self, api_key: str = None):
        self._api_key = api_key
        if not api_key:
            self._api_key = getenv('MARTA_API_KEY')

    @require_api_key
    def get_trains(self,
                   line: str = None,
                   station: str = None,
                   destination: str = None,
                   direction: str = None,
                   api_key: str = None) -> List[Train]:
        """
        Query API for train information

        :param line: Train line identifier filter (red, gold, green, or blue)
        :type line: str, optional
        :param station: train station filter
        :type station: str, optional
        :param destination: destination filter
        :type destination: str, optional
        :param direction: Direction train is heading (N, S, E, or W)
        :param api_key: API key to override environment variable
        :type api_key: str, optional
        :return: list of Train objects
        :rtype: List[Train]
        """
        data = _get_data(endpoint=_TRAIN_PATH, api_key=api_key)
        filters = {
            'LINE': line,
            'DIRECTION': _convert_direction(user_direction=direction, vehicle_type='train'),
            'STATION': station,
            'DESTINATION': destination
        }
        matching_data = _filter_response(response=data, filters=filters)
        return [Train(t) for t in matching_data]

    @require_api_key
    def get_buses(self,
                  route: int = None,
                  stop_id: int = None,
                  vehicle_id: int = None,
                  time_point: str = None,
                  direction: str = None,
                  api_key: str = None) -> List[Bus]:
        """
        Query API for bus information
        :param route: route number
        :type route: int, optional
        :param stop_id: Bus stop ID
        :type stop_id: int, optional
        :param vehicle_id: Bus ID
        :type vehicle_id: int, optional
        :param time_point:
        :type time_point: str, optional
        :param direction: Bus direction (Northbound, Southbound, Westbound or Eastbound)
        :type direction: str, optional
        :param api_key: API key to override environment variable
        :type api_key: str, optional
        :return: list of Bus objects
        """

        if route:
            endpoint = f'{_BUS_ROUTE_PATH}/{route}'
        else:
            endpoint = f'{_BUS_PATH}'


        data = _get_data(endpoint=endpoint, api_key=api_key)
        filters = {
            'STOPID': stop_id,
            'VEHICLE': vehicle_id,
            'TIMEPOINT': time_point,
            'ROUTE': route,
            'DIRECTION': _convert_direction(user_direction=direction, vehicle_type='bus')
        }
        matching_data = _filter_response(response=data, filters=filters)
        return [Bus(b) for b in matching_data]

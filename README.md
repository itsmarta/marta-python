# marta-python

Python library for accessing MARTA real-time API

## Testing

```
# Install tox
pip install tox
# Run tests
tox
```

## Installing

```
python setup.py install
```

## Using

The MARTA Python library expects your API key to be stored in the `MARTA_API_KEY` environment variable:

On Windows:

```
set MARTA_API_KEY=<your_api_key_here>
```

On Mac/Linux:

```
export MARTA_API_KEY=<your_api_key_here>
```

Optionally, you can also set the cache timeout (default 30 seconds):

Windows:

```
set MARTA_CACHE_EXPIRE=15
```

Mac/Linux:

```
export MARTA_CACHE_EXPIRE=15
```

There are two primary API wrapper functions, `get_buses()` and `get_trains()`. Each method takes keyword arguments to filter results.

```
from marta.api import get_buses, get_trains

# Get all buses
buses = get_buses()

# Get buses by route
buses = get_buses(route=1)

# Get all trains
trains = get_trains()

# Get trains by line
trains = get_trains(line='red')

# Get trains by station
trains = get_trains(station='Midtown Station')

# Get trains by destination
trains = get_trains(destination='Doraville')

# Get trains by line, station, and destination
trains = get_trains(line='blue', station='Five Points Station', destination='Indian Creek')
```

## Results

The library includes very basic objects to represent Trains and Buses. Below are dictionary representations of each.

The `get_buses()` and `get_trains()` functions return lists of `Bus` and `Train` objects, respectively.

### Bus Objects

```
{'adherence': '-3',
 'block_abbr': '3-3',
 'block_id': '346',
 'direction': 'Westbound',
 'last_updated': datetime.datetime(2017, 1, 26, 8, 10, 24),
 'latitude': '33.7545535',
 'longitude': '-84.4686002',
 'route': 3,
 'stop_id': '903320',
 'timepoint': 'Hamilton E. Holmes Station',
 'trip_id': '5408210',
 'vehicle': '2417'}
```

### Train Objects

```
{'destination': 'Indian Creek',
 'direction': 'E',
 'last_updated': datetime.datetime(2017, 1, 26, 8, 37, 35),
 'line': 'BLUE',
 'next_arrival': datetime.time(8, 37, 45),
 'station': 'GEORGIA STATE STATION',
 'train_id': '102026',
 'waiting_seconds': '-43',
 'waiting_time': 'Boarding'}
```

from datetime import datetime


class Vehicle():
    """Generic Vehicle object that exists to print vehicles as dicts"""
    def __str__(self):
        return str(self.__dict__)


class Bus(Vehicle):
    def __init__(self, record):
        self.adherence = record.get('ADHERENCE')
        self.block_id = record.get('BLOCKID')
        self.block_abbr = record.get('BLOCK_ABBR')
        self.direction = record.get('DIRECTION')
        self.latitude = record.get('LATITUDE')
        self.longitude = record.get('LONGITUDE')
        self.last_updated = datetime.strptime(record.get('MSGTIME'), '%m/%d/%Y %H:%M:%S %p')
        self.route = int(record.get('ROUTE'))
        self.stop_id = record.get('STOPID')
        self.timepoint = record.get('TIMEPOINT')
        self.trip_id = record.get('TRIPID')
        self.vehicle = record.get('VEHICLE')



class Train(Vehicle):
    def __init__(self, record):
        self.destination = record.get('DESTINATION')
        self.direction = record.get('DIRECTION')
        self.last_updated = datetime.strptime(record.get('EVENT_TIME'), '%m/%d/%Y %H:%M:%S %p')
        self.line = record.get('LINE')
        self.next_arrival = datetime.strptime(record.get('NEXT_ARR'), '%H:%M:%S %p').time()
        self.station = record.get('STATION')
        self.train_id = record.get('TRAIN_ID')
        self.waiting_seconds = record.get('WAITING_SECONDS')
        self.waiting_time = record.get('WAITING_TIME')

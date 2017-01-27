import datetime

from marta.vehicles import Bus, Train


def test_bus(bus_record):
    bus = Bus(bus_record)
    assert bus.adherence == "0"
    assert bus.block_id == "7"
    assert bus.block_abbr == "1-7"
    assert bus.direction == "Southbound"
    assert bus.latitude == "33.771677"
    assert bus.longitude == "-84.3867937"
    assert isinstance(bus.last_updated, datetime.datetime)
    assert bus.route == 1
    assert bus.stop_id == "907473"
    assert bus.timepoint == "North Ave Station"
    assert bus.trip_id == "5391405"
    assert bus.vehicle == "1469"


def test_train(train_record):
    train = Train(train_record)
    assert train.destination == "Doraville"
    assert train.direction == "N"
    assert isinstance(train.last_updated, datetime.datetime)
    assert train.line == "GOLD"
    assert isinstance(train.next_arrival, datetime.time)
    assert train.station == "CHAMBLEE STATION"
    assert train.train_id == "305326"
    assert train.waiting_seconds == "-40"
    assert train.waiting_time == "Boarding"

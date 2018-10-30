import pytest
import requests_mock

import marta
from marta.api import get_buses, get_trains
from marta.exceptions import APIKeyError
from marta.vehicles import Bus, Train


def test_get_trains(train_response):
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, text=train_response)
        trains = get_trains()
    for t in trains:
        assert isinstance(t, Train)


def test_get_trains_by_line(train_response):
    line = "BLUE"
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, text=train_response)
        trains = get_trains(line=line)

    assert len(trains) > 0
    for t in trains:
        assert isinstance(t, Train)
        assert t.line == line


def test_get_trains_by_station(train_response):
    station = "INDIAN CREEK STATION"
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, text=train_response)
        trains = get_trains(station=station)

    assert len(trains) > 0
    for t in trains:
        assert isinstance(t, Train)
        assert t.station == station


def test_get_trains_by_line_and_station(train_response):
    station = "INDIAN CREEK STATION"
    line = "BLUE"
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, text=train_response)
        trains = get_trains(line=line, station=station)

    assert len(trains) > 0
    for t in trains:
        assert isinstance(t, Train)
        assert t.station == station
        assert t.line == line


def test_get_buses(bus_all_response):
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, text=bus_all_response)
        buses = get_buses()

    assert len(buses) > 0

    for b in buses:
        assert isinstance(b, Bus)


def test_get_buses_by_route(bus_route_response):
    with requests_mock.mock() as m:
        m.get(requests_mock.ANY, text=bus_route_response)
        buses = get_buses(route=1)

    assert len(buses) > 0

    for b in buses:
        assert isinstance(b, Bus)
        assert b.route == 1


def test_missing_api_key():
    marta.api._API_KEY = None
    with pytest.raises(APIKeyError):
        buses = get_buses()

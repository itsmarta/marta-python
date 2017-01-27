import pytest

from marta.api import get_buses, get_trains
from marta.vehicles import Bus, Train


def test_get_trains():
    trains = get_trains()
    for t in trains:
        assert isinstance(t, Train)


def test_get_trains_by_line():
    line = "BLUE"
    trains = get_trains(line=line)

    assert len(trains) > 0
    for t in trains:
        assert isinstance(t, Train)
        assert t.line == line


def test_get_trains_by_station():
    station = "FIVE POINTS STATION"
    trains = get_trains(station=station)

    assert len(trains) > 0
    for t in trains:
        assert isinstance(t, Train)
        assert t.station == station


def test_get_trains_by_line_and_station():
    station = "FIVE POINTS STATION"
    line = "BLUE"
    trains = get_trains(line=line, station=station)

    assert len(trains) > 0
    for t in trains:
        assert isinstance(t, Train)
        assert t.station == station
        assert t.line == line


def test_get_buses():
    buses = get_buses()
    assert len(buses) > 0

    for b in buses:
        assert isinstance(b, Bus)


def test_get_buses_by_route():
    buses = get_buses(route=1)
    assert len(buses) > 0

    for b in buses:
        assert isinstance(b, Bus)
        assert b.route == 1

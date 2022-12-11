#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from car import Car

class ElectricCar:

    def __init__(self, battery_size, battery_range_km):

        if type(battery_size) != float or type(battery_range_km) != float or battery_size < 0 or battery_range_km < 0:
            raise Warning("Invalid Input")

        self.__battery_size = battery_size
        self.__battery_range_km = battery_range_km
        self.__charge_left = battery_size

    def charge(self, kwh):
        self.__charge_left += kwh
        if self.__charge_left > self.__battery_size:
            raise Warning("Battery overcharge")

    def get_battery_status(self):
        battery_status = self.__charge_left
        battery_size = self.__battery_size
        return battery_status, battery_size

    def get_remaining_range(self):
        range_left = self.__charge_left / self.__battery_size * self.__battery_range_km
        return range_left

    def drive(self, dist):
        if type(dist) != float or dist < 0:
            raise Warning("Invalid input type")

        if self.get_remaining_range() < dist:
            self.__charge_left = 0
            raise Warning("Battery empty")
        else:
            self.__charge_left -= dist / self.__battery_range_km * self.__battery_size

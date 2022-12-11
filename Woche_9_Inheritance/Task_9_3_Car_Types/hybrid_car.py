#!/usr/bin/env python3

# Implement this class. Stick to the naming that is introduced in the
# UML diagram. Do not change the class name or the method signatures
# or the automated grading won't work.

from combustion_car import CombustionCar
from electric_car import ElectricCar


class HybridCar(ElectricCar, CombustionCar):

    def __init__(self, gas_capacity, gas_per_100km, battery_size, battery_range_km):

        self.__COMBUSTION = 0
        self.__ELECTRIC = 1
        CombustionCar.__init__(self, gas_capacity, gas_per_100km)
        ElectricCar.__init__(self, battery_size, battery_range_km)
        self.__mode: int = self.__ELECTRIC

    def switch_to_combustion(self):
        self.__mode = self.__COMBUSTION

    def switch_to_electric(self):
        self.__mode = self.__ELECTRIC

    def get_remaining_range(self):
        return ElectricCar.get_remaining_range(self) + CombustionCar.get_remaining_range(self)

    def drive(self, dist: float) -> None:
        current_remaining = self.__get_mode_remaining_range()
        try:
            if self.__mode == self.__COMBUSTION:
                CombustionCar.drive(self, dist)
            else:
                ElectricCar.drive(self, dist)
        except Warning:
            if self.__mode == self.__COMBUSTION:
                self.switch_to_electric()
                ElectricCar.drive(self, dist - current_remaining)
            else:
                self.switch_to_combustion()
                CombustionCar.drive(self, dist - current_remaining)

    def __get_mode_remaining_range(self) -> float:
        if self.__mode == self.__COMBUSTION:
            return CombustionCar.get_remaining_range(self)
        else:
            return ElectricCar.get_remaining_range(self)

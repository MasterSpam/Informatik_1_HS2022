#!/usr/bin/env python3

# Implement this class. Extend Character and adopt the combat
# mechanics that are defined in the description. Do not change the
# class name and stick to the method signatures of Character
# or the automated grading won't work.

from character import Character


class Knight(Character):
    def _take_physical_damage(self, amount):
        amount = round(amount * 0.75)
        super()._take_physical_damage(amount)

    def _get_caused_dmg(self, other):
        return max(1, round((self._lvl * 11 - other._lvl) * 0.8))


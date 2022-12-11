#!/usr/bin/env python3

import random


class GameRunner(object):

    def __init__(self):
        self.rows = 17
        self.columns = 2

    def generate_hex_codes(self):
        HEX_BASE = "0123456789ABCDEF"
        result = []
        for i in range(self.rows * self.columns):
            temp = ""
            for j in range (4):
                temp += random.choice(HEX_BASE)
            result.append("0x" + temp)
        return result


d = GameRunner()
print(d.generate_hex_codes())

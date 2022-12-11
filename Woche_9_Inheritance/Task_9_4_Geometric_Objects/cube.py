from geometric_object import GeometricObject


class Cube(GeometricObject):
    def __init__(self, side_length, color, filled):
        self.__side_length = side_length
        super().__init__(color, filled)

    def get_side_length(self):
        return self.__side_length

    def set_side_length(self, side_length):
        self.__side_length = side_length

    def get_area(self):
        return round(6 * pow(self.__side_length, 2), 2)

    def get_volume(self):
        return round(pow(self.__side_length, 3), 2)


# IMPORTANT!!! I only got 2.8 out of 3 Points... I have no idea why... if you see it.. let me know  :)
class MagicDrawingBoard:
    def __init__(self, x, y):

        if not isinstance(x, int) or not isinstance(y, int):
            raise Warning("non valid x or y")

        if x < 1 or y < 1:
            raise Warning("Invalid Board")

        self.__width, self.__height = x, y
        self.__matrix = []
        for i in range(self.__height):        # create matrix with all zeros
            self.__matrix.append([0] * self.__width)

    def pixel(self, pixel_coord):

        if not isinstance(pixel_coord[0], int) or not isinstance(pixel_coord[1], int):
            raise Warning("non valid x or y")

        if pixel_coord[0] < 0 or pixel_coord[1] < 0:
            raise Warning("Invalid pixel input")

        try:
            self.__matrix[pixel_coord[1]][pixel_coord[0]] = "1"
        except:
            raise Warning("Invalid Pixel Input")

    def rect(self, start, end):

        if not isinstance(start[0], int) or not isinstance(start[1], int) or not isinstance(end[0], int) or not isinstance(end[1], int):
            raise Warning("non valid start or end")

        if start[0] < 0 or start[1] < 0 or end[0] < 0 or end[1] < 0:
            raise Warning("Invalid rect input")

        if start[0] > end[0] or start[1] > end[1]:
            raise Warning("Invalid Rect Input: no negative rect allowed")

        try:
            for i in range (end[1] - start[1]):
                self.__matrix[start[1] + i][start[0]:end[0]] = "1" * (end[0] - start[0])  # draws rect line by line

        except:
            raise Warning("Invalid Rect Input: rect outside of borders")

    def img(self):
        __result = ""
        for row in self.__matrix:
            __result += "".join(map(str, row)) + "\n"
        __result = __result[:-1]                        # remove last \n
        return __result

    def reset(self):
        self.__matrix = []
        for i in range(self.__height):  # create matrix with all zeros
            self.__matrix.append([0] * self.__width)


# You can play around with your implementation in the body of the following 'if'.
# The contained statements will be ignored while evaluating your solution.
if __name__ == '__main__':
    db = MagicDrawingBoard(1, "e")
    # db = MagicDrawingBoard(6, 4)  # instantiation of a specific size
    db.pixel((1, 1))  # draw at one coordinate
    db.rect((2, 2), (5, 4))  # draw a rectangle
    img = db.img()  # return the drawn image
    print(img)
    db.reset()  # reset the field again

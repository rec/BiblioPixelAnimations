from bibliopixel.animation import BaseMatrixAnim


class Pinwheel(BaseMatrixAnim):

    def __init__(self, layout, dir=True):
        super().__init__(layout)
        self._center = (self.width // 2, self.height // 2)
        self._dir = dir
        self._len = (self.width * 2) + (self.height * 2) - 2

    def step(self, amt):
        if self._dir:
            s = 255 - self._step
        else:
            s = self._step

        pos = 0
        cX, cY = self._center
        for x in range(self.width):
            index = pos * 255 / self._len + s
            self.layout.drawLine(cX, cY, x, 0, self.palette(index))
            pos += 1

        for y in range(self.height):
            color = self.palette(pos * 255 / self._len + s)
            self.layout.drawLine(cX, cY, self.width - 1, y, color)
            pos += 1

        for x in range(self.width - 1, -1, -1):
            color = self.palette(pos * 255 / self._len + s)
            self.layout.drawLine(cX, cY, x, self.height - 1, color)
            pos += 1

        for y in range(self.height - 1, -1, -1):
            color = self.palette(pos * 255 / self._len + s)
            self.layout.drawLine(cX, cY, 0, y, color)
            pos += 1

        self._step += amt
        if(self._step >= 255):
            self._step = 0

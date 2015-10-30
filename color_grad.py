"""Interpolate colours in colour gradients"""

class ColorGrad(object):

    def __init__(self):

        self.transform = lambda x: x
    @staticmethod
    def from_ascii_ppm(filename):

        self = ColorGrad()

        def getints(fromfile):
            for line in fromfile:
                line = line.split('#', 1)[0]
                for i in line.split():
                    try:
                        ans = int(i)
                        yield ans
                    except ValueError:
                        pass

        ints = getints(open(filename))
        next(ints)  # res x
        next(ints)  # res y
        next(ints)  # depth

        self.colors = []

        for i in ints:
            r,g,b = i, next(ints), next(ints)
            self.colors.append((r,g,b))

        return self
    def get_pos(self, x):    

        pos = (float(x) - self.min) / self.range

        pos = self.transform(pos)

        pos = min(1., max(0., pos))

        return pos
    def set_min_max(self, min, max):

        self.min = float(min)
        self.max = float(max)
        self.range = self.max - self.min
    def set_transform(self, transform):

        self.transform = transform

    def rgb_int(self, x):
        """rgb tuple for value x"""

        return self.colors[int((len(self.colors)-1) * self.get_pos(x))]

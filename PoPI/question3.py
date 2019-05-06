class ManhattanTaxi:
    '''implement the class'''

    def __init__(self, initX, initY, consuption, init_fuel):
        self.X = initX
        self.Y = initY
        self.pos = (self.X, self.Y)
        self.cons = consuption
        self.fuel = init_fuel

    def moveto(self, toX, toY):
        self.distance = abs(toX - self.X) + abs(toY - self.Y)
        self.fuel -= self.distance * self.cons
        self.X = toX
        self.Y = toY
        self.pos = (self.X, self.Y)
        return True

    def add_fuel(self, xtfuel):
        self.fuel += xtfuel


if __name__ == "__main__":
    t789 = ManhattanTaxi(5, 5, 1, 30)
    print(t789.moveto(3, 9))

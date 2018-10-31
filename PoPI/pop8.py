# Circular Sector Class


class Sector():
    def __init__(self):
        self.sfrom = 0
        self.to = 0
        self.rad = 0

    def rotate(self, angle):
        # implement this
        # rotates sector by angle
        # you man assume the rotation never results in a sector with from > to
        #(it is optional to solve this problem without this assumption; see above)#
        self.sfrom += angle
        self.to += angle

    def intersect(self, other):
        # implement this
        # returns sector that is intersection of this and other sector
        self.sfrom = max(self.sfrom, other.sfrom)
        self.to = min(self.to, other.to)
        self.rad = min(self.rad, other.rad)
        return self

    def is_empty(self):
        # implement this
        # returns True if the sector has empty area, otherwise False
        return self.sfrom == self.to

    def __eq__(self, other):
        # implement this
        # returns True this sector is the same as the other, otherwise False
        return (self.sfrom == other.sfrom) and (self.to == other.to)

    def __str__(self):
        # implement this
        # returns string "F T R" where F is from angle, T is to, and R is radius
        return '{} {} {}'.format(self.sfrom, self.to, self.rad)


# NO modications below this line
s1 = Sector()
s1.sfrom = 0
s1.to = 20
s1.rad = 40
print(s1)
s1.rotate(50)
print(s1)
s2 = Sector()
s2.sfrom = 50
s2.to = 80
s2.rad = 40
print(s1 == s2)
s2.sfrom = 60
s2.to = 100
s2.rad = 30
s3 = s1.intersect(s2)
print(s3)

# Advanced Counter Class


class Counter:
    def __init__(self, id):
        # complete the code below;
        #id is string;
        self._items = {}  # initialize with a value
        self._id = id

    def add(self, item_name, amount, price_of_unit):
        # implement this method;
        # item_name is string, amount is integer, price of unit is float
        # adds amount of items with item_name and specifies price_of_unit
        # you may assume that every addition for the same item_name will set
        # the same price_of_unit
        # see the examples of use in the code of main program below
        if item_name not in self._items.keys():
            self._items[item_name] = [amount, price_of_unit]
        else:
            self._items[item_name][0] += amount

    def remove(self, item_name, amount):
        # implement this method;
        # if the item_name is not among the items previously added, do nothing;
        # if the item_name is among them but the amount is greater or equal to the
        # number of previously added items with this name, remove the record
        # associated with item_name;
        # see the examples of use in the code of main program below
        self._items[item_name][0] -= amount

    def reset(self):
        # implement this method;
        # simply erases info about all the items previously added;
        # see the examples of use in the code of main program below
        self._items = {}

    def get_total(self):
        # implement this method;
        # returns the float number representing the total price
        # of all the items (think of due to pay) rounded to the 2nd fractional digit,
        # use standard round(x,2) function
        self._total = 0
        for items in self._items.keys():
            self._total += self._items[items][0] * self._items[items][1]
        return self._total

    def status_print(self):
        # implement this method;
        # prints "Id N M"
        # where Id is id of counter, N is total amount of all items and M total price of them
        # round M to the 2nd fractional digit as above
        # see the examples of use below
        self._total = 0
        for items in self._items.keys():
            self._total += self._items[items][0] * self._items[items][1]
        self._count = 0
        for i in self._items.keys():
            self._count += self._items[i][0]
        print('{} {} {}'.format(self._id, self._count, self._total))


# NO modifications modify below this line
c = Counter("C001")
c.add("Spaghetti", 5, 1.8)
c.status_print()
c.add("Ice Cream", 2, 3.4)
c.status_print()
print(c.get_total())
c.add("Spaghetti", 3, 1.8)
c.status_print()
c.remove("Ice Cream", 1)
c.status_print()
c.reset()
c.add("Coke", 5, 1.45)
c.status_print()

# our class Ship
class Ship:
    def __init__(self, name, capacity, country):
        self.country = country
        self.name = name
        self.capacity = capacity
        self.cargo = 0

    # the old sail method that you need to rewrite
    def sail(self):
        print("The {} has sailed for {}!".format(self.name, self.country))


x = input()
black_pearl = Ship("Black Pearl", 800, x)
black_pearl.sail()

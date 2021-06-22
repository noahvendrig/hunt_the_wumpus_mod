import random


class hazard:
    def __init__(self, type, location):
        self.type = type
        self.location = location

    def show(self):
        print("\n")
        print("Type is", self.type)
        print("Location is", self.location)


wumpus = hazard("wumpus", ("n" + str(random.randint(1, 20))))
bottomlessPit = hazard("pit", ("n" + str(random.randint(1, 20))))
bats = hazard("bats", ("n" + str(random.randint(1, 20))))


wumpus.show()
bottomlessPit.show()
bats.show()

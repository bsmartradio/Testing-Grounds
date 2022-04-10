class Bedroom:
    numberOfBeds = 0

    def __init__(self):
        self.numberOfBeds = 1

    def add_beds(self, number):
        self.numberOfBeds += number

    def get_number_of_beds(self):
        return self.numberOfBeds

class Kitchen:
    sinks = 0
    oven = 0
    fridge = 0
    table = 0

    def __init__(self):
        self.sinks = 1
        self.oven = 1

    def add_fridge(self, number):
        if self.fridge + number > 1:
            raise ValueError('You are only allowed 1 fridge')
        else:
            self.fridge += number

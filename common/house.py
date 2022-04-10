from common.kitchen import Kitchen
from common.bedroom import Bedroom


class House:
    kitchen = Kitchen()
    bedroom = Bedroom()

    def __init__(self, kitchen=None, bedroom=None):
        if kitchen is not None:
            self.kitchen = kitchen
        if bedroom is not None:
            self.bedroom = bedroom

class Channel:
    header = None

    def __init__(self, path):
        self.header = path

    def get_frequency(self):
        return self.header

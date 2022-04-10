from common.channel import Channel


class Image:
    channels = []

    def init_channel(self, path):
        files = ['file1', 'file2']
        for file in files:
            self.channels.append(self.create_channel(file))

    @staticmethod
    def create_channel(file):
        return Channel(file)

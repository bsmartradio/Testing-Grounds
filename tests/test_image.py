from unittest import TestCase

from common.channel import Channel
from common.image import Image


class TestImage(TestCase):
    def test_init_channel(self):
        image = Image()
        image.init_channel('Test')
        self.assertIsNotNone(image.channels)
        self.assertEqual(len(image.channels), 2)
        self.assertEqual('file1', image.channels[0].get_frequency())

    def test_create_channel(self):
        channel = Image.create_channel('test')
        self.assertTrue(isinstance(channel, Channel))
        self.assertTrue(isinstance(channel.header, str))
        self.assertEqual('test', channel.header)

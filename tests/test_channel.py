from unittest import TestCase

from common.channel import Channel


class MyTestCase(TestCase):

    def test_channel_should_return_header_from_init(self):
        channel = Channel('TestPath')
        result = channel.get_frequency()

        self.assertIsNot(None, 'Result is None!')
        self.assertEqual('TestPath', result)

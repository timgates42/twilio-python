# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class BrandedChannelTestCase(IntegrationTestCase):

    def test_fetch_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.preview.trusted_comms.branded_channels("BWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.holodeck.assert_has_request(Request(
            'get',
            'https://preview.twilio.com/TrustedComms/BrandedChannels/BWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX',
        ))

    def test_fetch_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "business_sid": "BXaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "brand_sid": "BZaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "sid": "BWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "links": {
                    "channels": "https://preview.twilio.com/TrustedComms/BrandedChannels/BWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa/Channels"
                },
                "url": "https://preview.twilio.com/TrustedComms/BrandedChannels/BWaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            }
            '''
        ))

        actual = self.client.preview.trusted_comms.branded_channels("BWXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX").fetch()

        self.assertIsNotNone(actual)

from rest_framework import status
from rest_framework.test import APITestCase
from vng_api_common.tests import JWTAuthMixin

from openzaak.brc.api.tests.utils import get_operation_url
from openzaak.brc.datamodel.tests.factories import BesluitFactory

from .mixins import MockSyncMixin

BESLUITTYPE = 'https://ztc.com/besluittype/abcd'


class BesluitPaginationTestCase(MockSyncMixin, JWTAuthMixin, APITestCase):

    heeft_alle_autorisaties = True

    def test_pagination_default(self):
        """
        Deleting a Besluit causes all related objects to be deleted as well.
        """
        BesluitFactory.create_batch(2)
        besluit_list_url = get_operation_url('besluit_list')

        response = self.client.get(besluit_list_url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['count'], 2)
        self.assertIsNone(response_data['previous'])
        self.assertIsNone(response_data['next'])

    def test_pagination_page_param(self):
        BesluitFactory.create_batch(2)
        besluit_list_url = get_operation_url('besluit_list')

        response = self.client.get(besluit_list_url, {'page': 1})

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response_data = response.json()
        self.assertEqual(response_data['count'], 2)
        self.assertIsNone(response_data['previous'])
        self.assertIsNone(response_data['next'])

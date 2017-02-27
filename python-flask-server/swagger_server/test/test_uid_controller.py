# coding: utf-8

from __future__ import absolute_import

from swagger_server.models.error import Error
from swagger_server.models.generic_object import GenericObject
from swagger_server.models.uid_info import UidInfo
from . import BaseTestCase
from six import BytesIO
from flask import json


class TestUidController(BaseTestCase):
    """ UidController integration test stubs """

    def test_root_get(self):
        """
        Test case for root_get

        Returns the current versions information
        """
        response = self.client.open('/v1/',
                                    method='GET')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_root_post(self):
        """
        Test case for root_post

        creates a new uid
        """
        response = self.client.open('/v1/',
                                    method='POST')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_uid_delete(self):
        """
        Test case for uid_delete

        delete a uid
        """
        response = self.client.open('/v1/{uid}'.format(uid=789),
                                    method='DELETE',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_uid_get(self):
        """
        Test case for uid_get

        get the particular uid for the version
        """
        response = self.client.open('/v1/{uid}'.format(uid=789),
                                    method='GET',
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_uid_post(self):
        """
        Test case for uid_post

        update an existing uid
        """
        body = GenericObject()
        response = self.client.open('/v1/{uid}'.format(uid=789),
                                    method='POST',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))

    def test_uid_put(self):
        """
        Test case for uid_put

        update an existing uid
        """
        body = GenericObject()
        response = self.client.open('/v1/{uid}'.format(uid=789),
                                    method='PUT',
                                    data=json.dumps(body),
                                    content_type='application/json')
        self.assert200(response, "Response body is : " + response.data.decode('utf-8'))


if __name__ == '__main__':
    import unittest
    unittest.main()

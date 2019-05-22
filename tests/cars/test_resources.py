# -*- coding: utf-8 -*-
import pytest

from apps.cars.models import Car

from apps.messages import MSG_INVALID_DATA

class TestResource:

    def set_up(self):
        self.data = {}
        self.ENDPOINT = '/cars'

        Car().drop_collection()

    def test_post_without_body(self, client):
        resp = client.post(
            self.ENDPOINT,
            data=dumps(dict()),
            content_type='application/json'
        )

        assert resp.json.get('message') == MSG_INVALID_DATA

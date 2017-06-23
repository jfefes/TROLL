# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
import requests as request
from models import *


class SearchTestCase(TestCase):
    def test_search_endpoint(self):
        path = "https://amtgard.com/ork/orkservice/Json/index.php"
        params = {
            "call":"SearchService/Player",
            "type":"all",
            "kingdom_id":"",
            "park_id":"198",
            "search": "rit",
        }
        response = request.get(path, params)
        return response.text

    def search_model_works(self):
        result = self.test_search_endpoint()
        api_test = OrkSearchRequest(kingdom="", park="198", player="rit")._send_request()
        self.assertEqual(result, api_test.text)

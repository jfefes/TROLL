# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import requests as request

class BaseOrkRequest():
    def __init__(self, params=None):
        self.service_name = "{}Service".format(params["service_name"])
        self.callname = "{}/{}".format(self.service_name, self.call_name)

    def _send_request(self, access_token=None, params={}):
        # if access_token is not None:
        #     # TODO: Validate token
        #     params["access_token"] = access_token
        # TODO: Inspect request and return either instance of response or error
        return request.get("https://amtgard.com/ork/orkservice/Json/index.php", self.params)

class OrkApiError():
    def __init__(self, path, body):
        self.path = path
        self.error_code = ""
        self.error_text = body.text

class OrkSearchRequest(BaseOrkRequest):
    def __init__(self, kingdom=None, park=None, player=None):
        self.params = {}
        if player is not None:
            assert park is not None
            assert kingdom is not None
            self.params["search"] = player
            self.params["park_id"] = park
            self.params["kingdom_id"] = kingdom
            self.params["call"] = "SearchService/Player"
            self.params["type"] = "all"

class OrkAuthRequest(BaseOrkRequest):
    def __init__(self, player_id=None, player_password=None, player_token=None):
        self.player = {
            "player_id": player_id,
            "player_password": player_password,
            "player_token": player_token
        }
        if player_token is not None:
            validate_or_create_token(self, player)

    def validate_or_create_token(self, player):
        # TODO: Validate token, or get a new one.
        pass

class OrkAttendanceRequest(BaseOrkRequest):
    def __init__(self):
        self.authorized_user = ""
        self.player = ""
        self.player_class = ""
        self.date = ""
        self.park = ""
        self.kingdom = ""

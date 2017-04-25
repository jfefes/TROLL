# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import requests as request

# Create your models here.
class OrkRequest():
    def __init__():
        search_url = "https://amtgard.com/ork/orkservice/Json/index.php"

        CALLTYPES = {
            "Search":
                ["Player"],
            "Authorization":
                ["GetAuthorizations"]
        }
        assert call_type in CALLTYPES
        assert call_scope in CALLTYPES[call_type]

        params["call"] = "{}Service/{}".format(call_type, call_scope)


class OrkResponse():
    def __init__():
        request.get(ork_request.search_url, ork_request.params)
        response_json = self.json

import requests as request
from ork_requests.models import *

def test_search_endpoint():
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

result = test_search_endpoint()

api_test = OrkSearchRequest(kingdom="", park="198", player="rit")._send_request()

print result == api_test.text

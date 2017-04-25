import requests as request

class OrkRequest:
    def __init__(self, params={}):
        self.path = "https://amtgard.com/ork/orkservice/Json/index.php"
        self.params = params
        self.params.update({
            "call":"SearchService/Player",
            "type":"all",
            "kingdom_id":"",
            "park_id":"198",
            "search": "rit",
        })
    def _send_request(self):
        self.response = request.get(self.path, self.params)
        self.data = self.response.text

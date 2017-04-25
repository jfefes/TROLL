import requests as request

search_url = "https://amtgard.com/ork/orkservice/Json/index.php"
params = {
    "call":"SearchService/Player",
    "type":"all",
    "kingdom_id":"",
    "park_id":"198",
    "search": "rit",
}

r = request.get(search_url, params)

print r
print r.text
# print r.json

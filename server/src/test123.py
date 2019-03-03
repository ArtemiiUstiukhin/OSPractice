import urllib.request
import json
response = urllib.request.urlopen('https://httpbin.org/test_recursive')
with open("rectest.json", "w", encoding="utf-8") as file:
    json.dump(response, file)

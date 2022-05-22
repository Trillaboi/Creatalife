import json
import urllib2

data = {'wallet_address': 'Hcq7uEiaJcukzZ9Kmyaz8wN4Q4fffMW8qrj98Xvknvk7','amount': 1}

req = urllib2.Request("http://127.0.0.1:5000/request_tokens")
req.add_header('Content-Type', 'application/json')

response = urllib2.urlopen(req, json.dumps(data))


print(response.read())

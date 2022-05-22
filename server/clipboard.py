import pyperclip
# req = requests.Session()
# response = req.post("http://127.0.0.1:5000/request_tokens", json={'wallet_address': 'Hcq7uEiaJcukzZ9Kmyaz8wN4Q4fffMW8qrj98Xvknvk7','amount': 1})
# print(response.text)

def get_clipboard():
    return pyperclip.paste()

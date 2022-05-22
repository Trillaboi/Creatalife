#!/usr/bin/env python
# encoding: utf-8
import tool, json, clipboard
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify({})

@app.route('/request_tokens', methods=['POST'])
def request_tokens():
    data = json.loads(request.data)
    print(data)
    response = tool.transfer_tokens(data['amount'], data['wallet_address'])
    print(response['result'])
    return jsonify(data)

@app.route('/get_clipboard')
def get_clipboard():
    address = clipboard.get_clipboard()
    print(address)
    return jsonify({"address":address})

# @app.rout('/upload_storj')
# def upload_stroj():



app.run()

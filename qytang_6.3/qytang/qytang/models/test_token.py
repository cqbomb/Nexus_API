#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import requests
import json

def get_token():
    base_url = 'http://192.168.1.101/api/'

    # create credentials structure
    name_pwd = {'aaaUser': {'attributes': {'name': 'admin', 'pwd': 'Cisc0123'}}}
    json_credentials = json.dumps(name_pwd)

    # log in to API
    login_url = base_url + 'aaaLogin.json'
    post_response = requests.post(login_url, data=json_credentials)

    # get token from login response structure
    auth = json.loads(post_response.text)
    login_attributes = auth['imdata'][0]['aaaLogin']['attributes']
    auth_token = login_attributes['token']

    return auth_token

if __name__ == "__main__":
    print(get_token())

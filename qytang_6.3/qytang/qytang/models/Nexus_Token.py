from Nexus_Core_Info import *

disable_warnings()
http = PoolManager()
import requests
import json

def nxos_token(nxos_ip):
    base_url = 'http://' + nxos_ip + '/api/'

    # create credentials structure
    name_pwd = {'aaaUser': {'attributes': {'name': username, 'pwd': password}}}
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
    nxos_token(nxos1_ip)

nxos1_headers = {'content-type': 'application/json', 'Cookie': "APIC-Cookie=" + nxos_token(nxos1_ip)}
nxos2_headers = {'content-type': 'application/json', 'Cookie': "APIC-Cookie=" + nxos_token(nxos2_ip)}
nxos3_headers = {'content-type': 'application/json', 'Cookie': "APIC-Cookie=" + nxos_token(nxos3_ip)}
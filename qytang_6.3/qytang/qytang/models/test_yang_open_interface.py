from N9K_Core_Info import *
from test_token import get_token

nxos1_url = "http://192.168.1.101/restconf/data/Cisco-NX-OS-device:System/bgp-items/inst-items/dom-items/Dom-list=default"

yang_headers = {'content-type': 'application/yang.data+xml'}
yang_headers["Authorization"] = 'Basic %s' % userAndPass
yang_headers["Accept"] = 'application/yang.data+xml'
def test_yang():
    payload = """<always>enabled</always><rtrId>2.2.2.2</rtrId>"""

    r = http.request('POST', nxos1_url, headers=yang_headers,body=payload.encode())
    #r = http.request('GET', nxos1_url, headers=yang_headers)
    print(r.data)


if __name__ == "__main__":
    test_yang()

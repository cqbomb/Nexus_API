from N9K_Core_Info import *
from test_token import get_token

nxos1_url = "http://192.168.1.101/api/mo/sys/bd.json"

yang_headers = {'content-type': 'application/json', 'Cookie': "APIC-Cookie=" + get_token()}


def test_yang():
    payload = {
        "bdEntity": {
          "children": [
            {
              "l2BD": {
                "attributes": {
                  "fabEncap": "vlan-88",
                  "pcTag": "1"
                }
              }
            }
          ]
        }
      }

    r = http.request('POST', nxos1_url, headers=yang_headers, body=json.dumps(payload))
    print(r.data)


if __name__ == "__main__":
    test_yang()

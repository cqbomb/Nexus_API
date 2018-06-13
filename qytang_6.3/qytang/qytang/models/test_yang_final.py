from N9K_Core_Info import *
from test_token import get_token

nxos1_url = "http://192.168.1.102/restconf/data/Cisco-NX-OS-device:"

yang_headers = {'content-type': 'application/yang.data+xml'}
yang_headers["Authorization"] = 'Basic %s' % userAndPass
yang_headers["Accept"] = 'application/yang.data+xml'
def test_yang():
    payload = """<System xmlns="http://cisco.com/ns/yang/cisco-nx-os-device">
  <bd-items>
    <bd-items>
      <BD-list>
        <fabEncap>vlan-90</fabEncap>
        <pcTag>1</pcTag>
      </BD-list>
    </bd-items>
  </bd-items>
</System>"""

    r = http.request('POST', nxos1_url, headers=yang_headers,body=payload.encode())
    #r = http.request('GET', nxos1_url, headers=yang_headers)
    print(r.data)


if __name__ == "__main__":
    test_yang()

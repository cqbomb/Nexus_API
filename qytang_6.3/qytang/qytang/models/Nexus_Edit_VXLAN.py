from Nexus_Token import *

def Edit_VXLAN(inputi):
    Vlan_ID = str(inputi)

    nxos1_api_url = "https://" + nxos1_ip + "/api/mo/sys/bd.json"
    nxos3_api_url = "https://" + nxos3_ip + "/api/mo/sys/bd.json"

    payload = {
        "bdEntity": {
            "children": [{
                "l2BD": {
                    "attributes": {
                        "accEncap": "vxlan-100" + Vlan_ID,
                        "fabEncap": "vlan-" + Vlan_ID,
                        "pcTag": "1"
                        }
                    }
                }
            ]
        }
    }

    http.request('POST', nxos1_api_url, headers=nxos1_headers, body=json.dumps(payload))
    http.request('POST', nxos3_api_url, headers=nxos3_headers, body=json.dumps(payload))

    payload_1 = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "configure terminal", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "interface nve 1", "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli",
         "params": {"cmd": "member vni 100" + str(Vlan_ID) + " mcast-group 225.0.0." + Vlan_ID, "version": 1}, "id": 3},
    ]
    http.request('POST', nxos1_url, headers=my_headers, body=json.dumps(payload_1))
    http.request('POST', nxos3_url, headers=my_headers, body=json.dumps(payload_1))

if __name__ == "__main__":
    Edit_VXLAN(55)
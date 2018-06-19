from Nexus_Token import *

def Edit_VLAN(Vlan_ID):
    nxos1_api_url = "https://" + nxos1_ip + "/api/mo/sys/bd.json"
    nxos3_api_url = "https://" + nxos3_ip + "/api/mo/sys/bd.json"

    payload = {
        "bdEntity": {
            "children": [{
                "l2BD": {
                    "attributes": {
                        "fabEncap": "vlan-" + str(Vlan_ID),
                        "pcTag": "1"
                        }
                    }
                }
            ]
        }
    }

    http.request('POST', nxos1_api_url, headers=nxos1_headers, body=json.dumps(payload))
    http.request('POST', nxos3_api_url, headers=nxos3_headers, body=json.dumps(payload))

if __name__ == "__main__":
    Edit_VLAN(55)
from Nexus_Token import *

def Edit_SVI(iinputi):
    Vlan_ID = str(iinputi)
    nxos3_api_url = "https://" + nxos3_ip + "/api/node/mo/sys/intf/svi-[vlan" + Vlan_ID + "].json"

    payload = {
        "sviIf": {
            "attributes": {
                "id": "vlan" + Vlan_ID,
                "adminSt": "up"
            }
        }
    }

    http.request('POST', nxos3_api_url, headers=nxos3_headers, body=json.dumps(payload))

def Edit_SVI_IPAdd(inputi):
    Vlan_ID = str(inputi)

    nxos3_api_url = "https://" + nxos3_ip + "/api/mo/sys.json"

    payload = {
        "topSystem": {
            "children": [{
                "ipv4Entity": {
                    "children": [{
                        "ipv4Inst": {
                            "children": [{
                                "ipv4Dom": {
                                    "attributes": {
                                        "name": "vxlan-100" + Vlan_ID
                                    },
                                    "children": [{
                                        "ipv4If": {
                                            "attributes": {
                                                "id": "vlan" + Vlan_ID
                                            },
                                            "children": [{
                                                "ipv4Addr": {
                                                    "attributes": {
                                                        "addr": "172.16." + Vlan_ID + ".1/24"
                                                    }
                                                }
                                            }]
                                        }
                                    }]
                                }
                            }]
                        }
                    }]
                }
            }]
        }
    }

    http.request('POST', nxos3_api_url, headers=nxos3_headers, body=json.dumps(payload))

if __name__ == "__main__":
    Edit_SVI(40)
    Edit_SVI_IPAdd(40)
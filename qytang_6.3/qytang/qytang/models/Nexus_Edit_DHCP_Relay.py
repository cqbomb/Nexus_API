from Nexus_Token import *

DHCP_Server_Realy_IP = "172.16.254.254"

def Enable_DHCP_Relay():

    nxos3_api_url = "https://" + nxos3_ip + "/api/mo/sys/dhcp.json"

    payload = {
            "dhcpEntity": {
        "children": [{
            "dhcpInst": {
                "attributes": {
                    "v4RelayEnabled": "yes"
                    }
                }
            }]
        }
    }

    http.request('POST', nxos3_api_url, headers=nxos3_headers, body=json.dumps(payload))

def Edit_DHCP_Relay_Server(inputx):
    Vlan_ID = str(inputx)

    nxos3_api_url = "https://" + nxos3_ip + "/api/mo/sys/dhcp/inst.json"

    payload = {
        "dhcpInst": {
            "children": [{
                "dhcpRelayIf": {
                    "attributes": {
                        "id": "vlan" + Vlan_ID
                    },
                    "children": [{
                        "dhcpRelayAddr": {
                            "attributes": {
                                "address": DHCP_Server_Realy_IP,
                                "counter": "2",
                                "vrf": "!unspecified"
                            }
                        }
                    }]
                }
            }]
        }
    }

    http.request('POST', nxos3_api_url, headers=nxos3_headers, body=json.dumps(payload))

if __name__ == '__main__':
    Edit_DHCP_Relay_Server()
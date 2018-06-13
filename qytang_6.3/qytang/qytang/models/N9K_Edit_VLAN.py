from N9K_Core_Info import *

def nxos1andnxos3_edit_vlan(VLANid):

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "configure terminal", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "vlan " + str(VLANid), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "exit", "version": 1}, "id": 3}
    ]
    http.request('POST', nxos1_url, headers=my_headers, body=json.dumps(payload))
    http.request('POST', nxos3_url, headers=my_headers, body=json.dumps(payload))

if __name__ == "__main__":
    nxos1andnxos3_edit_vlan()
from N9K_Core_Info import *

def nxos3_edit_svi(VLANid):

    SVIipadd = '172.16.' + str(VLANid) + '.1'

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "configure terminal", "version": 1}, "id": 1},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "interface vlan " + str(VLANid), "version": 1}, "id": 2},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "ip address "+str(SVIipadd)+"/24", "version": 1}, "id": 3},
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "no shut", "version": 1}, "id": 4}
    ]
    http.request('POST', nxos3_url, headers=my_headers, body=json.dumps(payload))

    # print(SVIipadd)

if __name__ == "__main__":
    nxos3_edit_svi()
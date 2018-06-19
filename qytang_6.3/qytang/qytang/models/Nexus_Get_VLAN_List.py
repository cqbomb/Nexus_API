from Nexus_Core_Info import *

def nxos1_vlan_lists():
    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show vlan brief", "version": 1}, "id": 1}
    ]
    r = http.request('POST', nxos1_url, headers=my_headers, body=json.dumps(payload))
    response = json.loads(r.data.decode())
    vlan_response = response['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

    vlan_list1 = []

    if isinstance(vlan_response, list):
        for x in vlan_response:
            vlan_list1.append(x['vlanshowbr-vlanid-utf'])
        return vlan_list1
    else:
        vlan_list1.append(vlan_response['vlanshowbr-vlanid-utf'])
        return vlan_list1

def nxos3_vlan_lists():
    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show vlan brief", "version": 1}, "id": 1}
    ]
    r = http.request('POST', nxos3_url, headers=my_headers, body=json.dumps(payload))
    response = json.loads(r.data.decode())
    vlan_response = response['result']['body']['TABLE_vlanbriefxbrief']['ROW_vlanbriefxbrief']

    vlan_list3 = []

    if isinstance(vlan_response, list):
        for x in vlan_response:
            vlan_list3.append(x['vlanshowbr-vlanid-utf'])
        return vlan_list3
    else:
        vlan_list3.append(vlan_response['vlanshowbr-vlanid-utf'])
        return vlan_list3

if __name__ == "__main__":
    print('NXOS1 VLAN Lists:',nxos1_vlan_lists())
    print('NXOS3 VLAN Lists:',nxos3_vlan_lists())
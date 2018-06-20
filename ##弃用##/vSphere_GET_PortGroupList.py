from vSphere_QYTVC import get_networks,get_token
from vSphere_Core_Info import *

def get_network_id():
    token = get_token(vcip,username,password)

    result = get_networks(vcip,token)

    vlanid = []

    for x in result['value']:
        if 'VLAN' in x['name']:
            vlanid.append(int(x['name'].replace('VLAN','')))

    return  vlanid


if __name__ == "__main__":
    print(get_network_id())
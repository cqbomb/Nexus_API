from vSphere_QYTVC import get_networks,get_token,get_vms,add_vm_nic
from vSphere_Core_Info import *

def get_net_id(no):
    token = get_token(vcip,username,password)

    result = get_networks(vcip,token)

    for x in result['value']:
        if x['name'] == 'VLAN'+str(no):
            return x['network']

def get_vmhost_id(no):
    token = get_token(vcip,username,password)

    vm_list = get_vms(vcip,token)

    for x in vm_list:
        if x['name'] == 'CentOS_' + str(no):
            return x['vm']

def edit_nic(no):
    net_id = get_net_id(no)
    print('网络唯一ID:' + str(net_id))
    vm_id = get_vmhost_id(no)
    print('虚拟机唯一ID:' + str(vm_id))
    token = get_token(vcip,username,password)
    print('为虚拟机'+str(vm_id)+'关联端口组'+str(net_id))
    add_vm_nic(vcip, token, vm_id, net_id)

if __name__ == "__main__":
    print(get_net_id())
    print(get_vmhost_id())
    edit_nic()
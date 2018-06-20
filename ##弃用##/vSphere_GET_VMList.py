from vSphere_QYTVC import get_vms,get_token
from vSphere_Core_Info import *

def get_vm_id():
    token = get_token(vcip,username,password)

    vm_list = get_vms(vcip,token)

    vm_ids = []

    for vm in vm_list:
        if 'CentOS_' in vm['name']:
            vm_ids.append(int(vm['name'].replace('CentOS_','')))
    return  vm_ids
if __name__ == "__main__":
    print(get_vm_id())


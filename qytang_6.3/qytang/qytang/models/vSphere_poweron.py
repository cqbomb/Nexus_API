from vSphere_Core_Info import *
from vSphere_QYTVC import get_token, get_vms, poweron_vm

def vSphere_power_on(VLANID):
    token = get_token(vcip,username,password)

    vm_list = get_vms(vcip,token)
    print(vm_list)
    for vm in vm_list:
        if vm['name'] == 'CentOS_'+ str(VLANID):
            vmid = vm['vm']

    poweron_vm(vcip,token,vmid)

if __name__ == "__main__":
    vSphere_power_on(77)
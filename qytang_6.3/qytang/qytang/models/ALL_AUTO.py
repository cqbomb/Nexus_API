from vSphere_Clone_VM import clone_vm_from_no
from vSphere_Create_PortGroup import create_pg
from vSphere_EDIT_PortGroupLink import edit_nic
from vSphere_Edit_PortGroupVlanID import edit_pg_vlan_id
from vSphere_Power_On import vSphere_power_on
from ASA_Object import create_in_obj,create_out_obj
from ASA_NAT import create_nat
from ASA_ACL import create_acl

import time
from random import randint

def vsphere_all_auto(temp_no,VLANID):
    # while True:
    #     VLANID = randint(1,100)
    #     VMID = get_vm_id()
    #     NETID = get_network_id()
    #     if VLANID in VMID:
    #         continue
    #     if VLANID in NETID:
    #         continue
    #     break
    #print('=' * 100)
    #print('创建端口组VLAN' + str(VLANID) + '...')
    create_pg(VLANID)

    #print('创建虚拟机CentOS_'+str(VLANID)+'...')
    clone_vm_from_no(VLANID,temp_no)

    #print('创建主机网络适配器，并且关联端口组...')
    edit_nic(VLANID)

    #print('编辑端口组VLAN ID - '+str(VLANID)+'...')
    edit_pg_vlan_id(VLANID)

    vSphere_power_on(VLANID)
    #time.sleep(3)
    #print('=' * 100)
    #print('完成vSphere自动化任务！')
    return VLANID

def config_asa(VLANID):
    create_in_obj(VLANID)
    create_out_obj(VLANID)
    create_nat(VLANID)
    create_acl(VLANID)

Choose_VM_Banner = """ 1. OS: CentOS ; CPU: 1 ; RAM: 1
 2. OS: CentOS ; CPU: 1 ; RAM: 2
 3. OS: CentOS ; CPU: 2 ; RAM: 1
 4. OS: CentOS ; CPU: 2 ; RAM: 2
 Please select the Virtual Machine Template you want to create (1-4)"""

if __name__ == "__main__":
    # Choose_VM_No = input(Choose_VM_Banner+":")
    # VLANID = vsphere_all_auto(int(Choose_VM_No))
    # ALL_AUTO_N9K(VLANID)
    # config_asa(VLANID)
    vsphere_all_auto(1,79)




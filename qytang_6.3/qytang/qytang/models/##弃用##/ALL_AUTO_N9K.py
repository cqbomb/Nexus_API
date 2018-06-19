from N9K_Get_VLAN_List import nxos1_vlan_lists, nxos3_vlan_lists
from N9K_Edit_VLAN import nxos1andnxos3_edit_vlan
from N9K_Edit_VXLAN import nxos1andnxos3_edit_vxlan
from N9K_Edit_SVI import nxos3_edit_svi
from random import randint

VLANid = randint(1, 100)
def ALL_AUTO_N9K(VLANid):
    #print('='*100)
    #print('开始配置N9K网络:')
    VXLANid = '100' + str(VLANid)
    SVIipadd = '172.16.' + str(VLANid) + '.1'

    while True:
        NXOS1_VLAN_LISTS = nxos1_vlan_lists()
        NXOS3_VLAN_LISTS = nxos3_vlan_lists()
        if VLANid in NXOS1_VLAN_LISTS:
            continue
        if VLANid in NXOS3_VLAN_LISTS:
            continue
        break

    #print('NXOS-1 vlan lists Befor: ' + str(NXOS1_VLAN_LISTS))
    #print('NXOS-3 vlan lists Befor: ' + str(NXOS3_VLAN_LISTS))

    #print('create vlan \'' + str(VLANid) + '\' on NXOS-1 adn NXOS-3')
    nxos1andnxos3_edit_vlan(VLANid)

    #print('NXOS-1 vlan lists Now: ' + str(nxos1_vlan_lists()))
    #print('NXOS-3 vlan lists Now: ' + str(nxos3_vlan_lists()))

    #print('Create vxlan on NXOS-1 adn NXOS-3: ' + VXLANid)
    nxos1andnxos3_edit_vxlan(VLANid)

    #print('Create vlan ' + str(VLANid) + ' SVI address'+ ' on NXOS-3: ' + SVIipadd)
    nxos3_edit_svi(VLANid)

if __name__ == "__main__":
    ALL_AUTO_N9K(38)
    print('='*50)
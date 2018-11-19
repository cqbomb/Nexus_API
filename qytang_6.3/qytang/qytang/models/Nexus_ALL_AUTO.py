from Nexus_Get_VLAN_List import nxos1_vlan_lists, nxos3_vlan_lists
from Nexus_Edit_VLAN import Edit_VLAN
from Nexus_Edit_VXLAN import Edit_VXLAN
from Nexus_Edit_SVI import Edit_SVI,Edit_SVI_IPAdd
from Nexus_Edit_DHCP_Relay import Edit_DHCP_Relay_Server
from random import randint

# Vlan_ID = randint(1, 100)
def Nexus_ALL_AUTO(inputi):
    Vlan_ID = str(inputi)
    print('='*100)
    print('Start to Edit Nexus:')
    VXLANid = '100' + Vlan_ID
    SVIipadd = '172.16.' + Vlan_ID + '.1'

    while True:
        NXOS1_VLAN_LISTS = nxos1_vlan_lists()
        NXOS3_VLAN_LISTS = nxos3_vlan_lists()
        if Vlan_ID in NXOS1_VLAN_LISTS:
            continue
        if Vlan_ID in NXOS3_VLAN_LISTS:
            continue
        break

    print('NXOS-1 vlan lists Befor: ' + str(NXOS1_VLAN_LISTS))
    print('NXOS-3 vlan lists Befor: ' + str(NXOS3_VLAN_LISTS))

    print('Create Vlan \'' + Vlan_ID + '\' on NXOS-1 adn NXOS-3')
    Edit_VLAN(Vlan_ID)

    print('NXOS-1 vlan lists Now: ' + str(nxos1_vlan_lists()))
    print('NXOS-3 vlan lists Now: ' + str(nxos3_vlan_lists()))

    print('Create vxlan on NXOS-1 adn NXOS-3: ' + VXLANid)
    Edit_VXLAN(Vlan_ID)

    print('Edit DHCP Realy for Vlan' + Vlan_ID)
    Edit_DHCP_Relay_Server(Vlan_ID)

    print('Create Vlan' + Vlan_ID + ' SVI address' + ' on NXOS-3: ' + SVIipadd)
    Edit_SVI(Vlan_ID)
    Edit_SVI_IPAdd(Vlan_ID)

if __name__ == "__main__":
    Nexus_ALL_AUTO(27)
    # print('='*100)
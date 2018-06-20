from Nexus_Core_Info import username, password
import paramiko
import time

dhcp_server_ip = "192.168.1.105"

def dhcp_server_edit(inputx):
    VlanID = str(inputx)
    network_sub = "172.16." + VlanID + "."
    # print(network_sub)
    dhcp_edit_command = ["enable", "cisco", "configure terminal",
                         "ip dhcp pool Vlan" + VlanID,
                         "network " + network_sub + "0 /24",
                         "default-router " + network_sub + "1",
                         "dns-server 8.8.8.8",
                         "exit",
                         "ip dhcp excluded-address " + network_sub + "1 " + network_sub + "99",
                         "ip dhcp excluded-address " + network_sub + "101 " + network_sub + "254",
                         "exit"]
    # print(dhcp_edit_command)

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(dhcp_server_ip, port=22, username=username, password=password,
                look_for_keys=False, allow_agent=False)
    ssh_conn = ssh.invoke_shell()
    # output = ssh_conn.recv(65535)
    # print(output)

    for x in dhcp_edit_command:
        ssh_command = x + "\n"
        # print(ssh_command)
        ssh_conn.send(ssh_command)
        time.sleep(.5)
        # output = ssh_conn.recv(65535)
        # print(output)

    print('=' * 100)
    print("DHCP Service for CentOS_" + VlanID + " is all ready")
    ssh.close()

if __name__ == "__main__":
    dhcp_server_edit(66)
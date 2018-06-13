import paramiko


def sshclient_execmd(hostname, port, username, password, execmd):
    paramiko.util.log_to_file("paramiko.log")

    s = paramiko.SSHClient()
    s.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    s.connect(hostname=hostname, port=port, username=username, password=password)
    stdin, stdout, stderr = s.exec_command(execmd)

    s.close()

def edit_pg_vlan_id(vlan_no):
    hostname = "172.16.1.201"
    port = 22
    username = "root"
    password = "Cisc0123"
    execmd = "esxcli network vswitch standard portgroup set -p VLAN"+str(vlan_no)+" -v "+str(vlan_no)

    sshclient_execmd(hostname, port, username, password, execmd)

if __name__ == "__main__":

    edit_pg_vlan_id()

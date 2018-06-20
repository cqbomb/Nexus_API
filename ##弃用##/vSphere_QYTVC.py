from urllib3 import *
import json
from vSphere_Core_Info import *
from base64 import b64encode

disable_warnings()#关闭SSL告警

http = PoolManager()#控制并发的POOL

user_pass_str = username + ':' + password#拼接用户名:密码
user_pass_str_encode = user_pass_str.encode()
userAndPass = b64encode(user_pass_str_encode).decode("ascii")#进行Base64转码

authen_headers = { 'Authorization' : 'Basic %s' %  userAndPass }#拼接为HTTP认证头部

def get_token(vcip,username,password):
    url = 'https://'+vcip+'/rest/com/vmware/cis/session'#请求的URL
    r = http.request('POST', url, headers=authen_headers)#使用POST发起请求,并且使用认证头部
    token = r.data.decode()
    return json.loads(token)['value']#返回JSON数据中的Token内容

def get_vms(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']

def get_vm_power_status(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())['value']

def poweron_vm(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power/start'
    r = http.request('POST', url, headers=headers)
    try:
        return json.loads(r.data.decode())
    except Exception as e:
        return 'vm has power on'

def poweroff_vm(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/power/stop'
    r = http.request('POST', url, headers=headers)
    try:
        return json.loads(r.data.decode())
    except Exception as e:
        return 'vm has power off'

def get_vm_nics(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())

def get_vm_nic_detail(vcip,token,vmid,nic):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet/' + nic
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())

def get_networks(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/network'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())

def update_vm_nic(vcip,token,vmid,nic,network_name):
    headers = {'vmware-api-session-id':token,'Content-Type':'application/json'}
    network_nic_json = {
        "spec": {
            "backing": {
                "type": "STANDARD_PORTGROUP",
                "network": network_name
            },
        }
    }
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet/' + nic
    r = http.request('PATCH', url, headers=headers, body=json.dumps(network_nic_json))
    return r.data

def get_hosts(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/host'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())

def get_datastores(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/datastore'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())

def get_folders(vcip,token):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/folder'
    r = http.request('GET', url, headers=headers)
    return json.loads(r.data.decode())

def create_vm(vcip,token,vmname):
    headers = {'vmware-api-session-id':token,'Content-Type':'application/json'}
    vm_json = {
               "spec": {
                        "placement": {
                                      "folder": "group-v65",
                                      "host": "host-28",
                                      "datastore": "datastore-29"
                                      },
                        "name": vmname,
                        "guest_OS": "RHEL_7_64",
                        "memory": {
                                   "hot_add_enabled": True,
                                   "size_MiB": 1024
                                  },
                        "cpu": {
                                "count": 1,
                                "hot_add_enabled": True,
                                "hot_remove_enabled": True,
                                "cores_per_socket": 1
                                }
                        }
               }
    url = 'https://' + vcip + '/rest/vcenter/vm/'
    r = http.request('POST', url, headers=headers, body=json.dumps(vm_json))
    return r.data

def delete_vm(vcip,token,vmid):
    headers = {'vmware-api-session-id':token}
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid
    r = http.request('DELETE', url, headers=headers)
    return r.data

def add_vm_nic(vcip,token,vmid,network_name):
    headers = {'vmware-api-session-id':token,'Content-Type':'application/json'}
    add_nic_json = {
                        "spec": {
                                 "backing": {
                                             "type": "STANDARD_PORTGROUP",
                                             "network": network_name
                                            },
                                 "allow_guest_control": True,
                                 "mac_type": "ASSIGNED",
                                 "wake_on_lan_enabled": True,
                                 "start_connected": True,
                                 "type": "VMXNET3"
                                 }
                        }
    url = 'https://' + vcip + '/rest/vcenter/vm/' + vmid + '/hardware/ethernet'
    r = http.request('POST', url, headers=headers, body=json.dumps(add_nic_json))
    return r.data

if __name__ == '__main__':
    token = get_token(vcip,username,password)
    #print(token)
    print(get_vms(vcip,token))
    #print(get_vm_power_status(vcip,token,'vm-32'))
    #print(poweron_vm(vcip, token, 'vm-32'))
    #print(poweroff_vm(vcip, token, 'vm-32'))
    #print(get_networks(vcip, token))
    #print(get_vm_nics(vcip,token,'vm-32'))
    #print(get_vm_nic_detail(vcip,token,'vm-32','4000'))
    #print(update_vm_nic(vcip,token,'vm-32','4000','network-68'))
    #print(get_hosts(vcip,token))
    #print(get_datastores(vcip, token))
    #print(get_folders(vcip,token))
    #print(create_vm(vcip,token,'qytang_newvm'))
    #print(delete_vm(vcip,token,"vm-72"))
    #print(add_vm_nic(vcip,token,'vm-72','network-30'))
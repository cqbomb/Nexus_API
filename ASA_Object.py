import json
from urllib3 import *
from base64 import b64encode


def create_in_obj(VLANID):
    username = "admin"
    password = "Cisc0123"
    ip = "192.168.1.104"
    disable_warnings()
    http = PoolManager()

    ipaddress = "172.16."+str(VLANID)+".100"
    object_name = "VLAN_" + str(VLANID) + "_HOST"
    print('创建ASA内部Object' + object_name)
    headers = {}

    headers['Content-Type'] = 'application/json'

    user_pass_str = username + ':' + password
    user_pass_str_encode = user_pass_str.encode()
    userAndPass = b64encode(user_pass_str_encode).decode("ascii")

    headers["Authorization"] = 'Basic %s' % userAndPass

    json_data = {
                 "host" : {
                          "kind" : "IPv4Address",
                          "value" : ipaddress
                         },
                 "kind" : "object#NetworkObj",
                 "name" : object_name
                 }
    url = 'https://' + ip + '/api/objects/networkobjects'  # 请求的URL
    r = http.request('POST', url, headers=headers, body=json.dumps(json_data))  # 使用POST发起请求,并且使用认证头部
    print(r.data.decode())

def create_out_obj(VLANID):
    username = "admin"
    password = "Cisc0123"
    ip = "192.168.1.104"

    disable_warnings()
    http = PoolManager()

    outside_ip = "202.100.1."+ str(VLANID)
    object_name = "outside_" + str(VLANID)
    print('创建ASA外部Object'+object_name)
    headers = {}

    headers['Content-Type'] = 'application/json'

    user_pass_str = username + ':' + password
    user_pass_str_encode = user_pass_str.encode()
    userAndPass = b64encode(user_pass_str_encode).decode("ascii")

    headers["Authorization"] = 'Basic %s' % userAndPass

    json_data = {
                 "host" : {
                          "kind" : "IPv4Address",
                          "value" : outside_ip
                         },
                 "kind" : "object#NetworkObj",
                 "name" : object_name
                 }
    url = 'https://' + ip + '/api/objects/networkobjects'  # 请求的URL
    r = http.request('POST', url, headers=headers, body=json.dumps(json_data))  # 使用POST发起请求,并且使用认证头部
    print(r.data.decode())

if __name__ == "__main__":
    create_in_obj(46)
    create_out_obj(46)
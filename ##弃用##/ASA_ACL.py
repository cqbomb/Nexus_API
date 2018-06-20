import json
from urllib3 import *
from base64 import b64encode


def create_acl(VLANID):
    username = "admin"
    password = "Cisc0123"
    ip = "192.168.1.104"

    disable_warnings()
    http = PoolManager()
    print('配置ACL')
    object_name = "VLAN_" + str(VLANID) + "_HOST"
    headers = {}

    headers['Content-Type'] = 'application/json'

    user_pass_str = username + ':' + password
    user_pass_str_encode = user_pass_str.encode()
    userAndPass = b64encode(user_pass_str_encode).decode("ascii")

    headers["Authorization"] = 'Basic %s' % userAndPass

    json_data = {
                "sourceAddress": {
                "kind": "AnyIPAddress",
                "value": "any"
                },
                "destinationAddress": {
                "kind": "objectRef#NetworkObj",
                "objectId":object_name
                },
                "destinationService": {
                "kind": "NetworkProtocol",
                "value": "icmp"
                },
                "permit": True,
                "active": True
                }
    url = 'https://' + ip + '/api/access/in/Outside/rules'  # 请求的URL
    r = http.request('POST', url, headers=headers, body=json.dumps(json_data))  # 使用POST发起请求,并且使用认证头部
    print(r.data.decode())


if __name__ == "__main__":
    create_acl(46)
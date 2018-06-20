import json
from urllib3 import *
from base64 import b64encode


def create_nat(VLANID):
    username = "admin"
    password = "Cisc0123"
    ip = "192.168.1.104"

    disable_warnings()
    http = PoolManager()

    inside_obj = "VLAN_" + str(VLANID) + "_HOST"
    outside_obj = "outside_" + str(VLANID)
    print('开始配置NAT')
    headers = {}

    headers['Content-Type'] = 'application/json'

    user_pass_str = username + ':' + password
    user_pass_str_encode = user_pass_str.encode()
    userAndPass = b64encode(user_pass_str_encode).decode("ascii")

    headers["Authorization"] = 'Basic %s' % userAndPass

    json_data = {
                "isPatPool": False,
                "useInterfaceIPv6": False,
                "isRoundRobin": False,
                "isNetToNet": False,
                "isNoProxyArp": False,
                "translatedService": "original",
                "originalSource": {
                    "kind": "objectRef#NetworkObj",
                    "objectId": inside_obj
                },
                "isRouteLookup": False,
                "mode": "static",
                "translatedSource": {
                    "kind": "objectRef#NetworkObj",
                    "objectId": outside_obj
                },
                "isDNS": False,
                "originalInterface": {
                    "kind": "objectRef#Interface",
                    "name": "Inside"
                },
                "translatedInterface": {
                    "kind": "objectRef#Interface",
                    "name": "Outside"
                },
                "isInterfacePAT": False
                }
    url = 'https://' + ip + '/api/nat/auto'  # 请求的URL
    r = http.request('POST', url, headers=headers, body=json.dumps(json_data))  # 使用POST发起请求,并且使用认证头部
    print(r.data.decode())


if __name__ == "__main__":

    create_nat(46)

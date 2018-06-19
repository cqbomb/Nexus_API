from N9K_Core_Info import *

def nxos1_shwo_version():

    payload = [
        {"jsonrpc": "2.0", "method": "cli", "params": {"cmd": "show version", "version": 1}, "id": 1}
    ]
    r = http.request('POST', nxos1_url, headers=my_headers, body=json.dumps(payload))

    response = json.loads(r.data.decode())
    kick_start_image = response['result']['body']['kickstart_ver_str']
    chassis_id = response['result']['body']['chassis_id']
    hostname =  response['result']['body']['host_name']

    print("ip : {0} is a \"{1}\" \nhostname : {2} \nrunning software version : {3}".format(nxos1_ip, chassis_id, hostname, kick_start_image))

if __name__ == "__main__":
    nxos1_shwo_version()



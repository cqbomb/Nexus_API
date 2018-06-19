from urllib3 import *
from base64 import b64encode

disable_warnings()
http = PoolManager()

username = "admin"
password = "Cisc0123"
nxos1_ip = "192.168.1.101"
nxos2_ip = "192.168.1.102"
nxos3_ip = "192.168.1.103"
nxos1_url = "https://" + nxos1_ip + "/ins"
nxos2_url = "https://" + nxos2_ip + "/ins"
nxos3_url = "https://" + nxos3_ip + "/ins"


my_headers = {"content-type" : "application/json-rpc"}


user_pass_str = username + ":" + password
user_pass_str_encode = user_pass_str.encode()
userAndPass = b64encode(user_pass_str_encode).decode("ascii")

my_headers["Authorization"] = "Basic %s" % userAndPass

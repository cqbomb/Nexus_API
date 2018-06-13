from N9K_Core_Info import *


def test_json_rpc():
    payload = [
  {
    "jsonrpc": "2.0",
    "method": "cli",
    "params": {
      "cmd": "show ver",
      "version": 1
    },
    "id": 1
  }
]
    r = http.request('POST', nxos1_url, headers=my_headers, body=json.dumps(payload))
    print(r.data)


if __name__ == "__main__":
    test_json_rpc()

import requests
import json
import sys

ip_api = "https://api.ipify.org?format=json"

cf_api_key = "95df3de23ca83c26201155068abf725e71cd2"

cf_email = "starlingjarred@gmail.com"

zone_id = "dc6ef59e26da897cc15050ab2cebe226"

record_id = 'bfeea464f7e80cf38ad47e0237086f5a'


if not record_id:
    resp = requests.get(
        "https://api.cloudflare.com/client/v4/zones/{}/dns_records".format(zone_id),
        headers={
            'X-Auth-Key': cf_api_key,
            'X-Auth-Email': cf_email
            }
        )
    print(json.dumps(resp.json(), indent=4, sort_keys=True))
    print("please find the required redcord id")
    sys.exit(0)
    
    
resp = requests.get(ip_api)
ip = resp.json()['ip']

print(resp)
print(ip)

resp = requests.put(
    "https://api.cloudflare.com/client/v4/zones/{}/dns_records/{}".format(
        zone_id, record_id
        ), json={
            'type': 'A',
            'name': 'beardbrothersbetterbeardbalm.com',
            'content': ip,
            'proxied': True
            },
        headers={
            'X-Auth-Key': cf_api_key,
            'X-Auth-Email': cf_email
        }
    )
assert resp.status_code == 200

print("updated dns record for {}".format(ip))
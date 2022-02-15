import requests
import urllib3
import json

def getLab(node):
    labId = '0dd1ab'
    url = f'https://192.168.128.20/api/v0/labs/{labId}/nodes/{node}'
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uY2lzY28udmlybCIsImlhdCI6MTY0NDk0MTE5MiwiZXhwIjoxNjQ1MDI3NTkyLCJzdWIiOiJkMGNhMTM4Ni0xMDViLTQzMTctYmNiZi03Nzc0ZDE2NTQwZmUifQ.TnjzkAXmmOn2XY3u_BTTWY2BzwtRHh3BR5Q_ktUlV68'}
    output = requests.get(url, headers = headers, verify = False)
    string = json.loads(output.text)
    print(string['data']['configuration'])

def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    getLab('n1')

main()
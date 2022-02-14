import requests
import urllib3

def getLab(node):
    labId = 'ebbd8e'
    url = f'https://192.168.68.132/api/v0/labs/{labId}/nodes/{node}'
    headers = {'Authorization': 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJjb20uY2lzY28udmlybCIsImlhdCI6MTY0NDc4NTg0MCwiZXhwIjoxNjQ0ODcyMjQwLCJzdWIiOiJiMDc3ZDY4Mi05ZjU4LTQ0MjAtYTI5ZS03MjdmOGVmMGI3MmYifQ.d-zaJ5ar-eAkEgKKEqWg7VOYO4GRWb0DKGP_pgQAseI'}
    output = requests.get(url, headers = headers, verify = False)
    print(output.text)


def main():
    urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
    print(getLab('n1'))

main()
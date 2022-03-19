import json
from sampledata import datas
data = json.loads(datas)
print("Interface Status", '=' * 80, sep='\n')
print(f"DN{' ':50}Description{' ':10}Speed{' ':3}MTU")
print('-'*50, '-'*20, '-'*6, '-'*6)
for el in data["imdata"]:
    dn = el["l1PhysIf"]["attributes"]["dn"]
    descr = el["l1PhysIf"]["attributes"]["descr"]
    speed = el["l1PhysIf"]["attributes"]["speed"]
    mtu = el["l1PhysIf"]["attributes"]["mtu"]
    print(f'{dn:42}{" ":15}{descr}{" ":14}{speed}{" ":2}{mtu}')


import json
import requests
from netbox_item import NetboxItem

def get_items() -> list[NetboxItem]:
    headers = {
        'Authorization' : 'Token 0d8cf57d35084035866851a18a22fde2678cd204',
        'Content-Type': 'application/json'
        }
    # for i in range(0, 1101, 50):
    response = requests.get(f'https://10.0.1.1/api/dcim/devices/?limit=1200', headers=headers, verify=False).json()['results']

    with open('all_netbox.json', 'w') as fp:
        json.dump(response, fp=fp, indent=4)

    with open('all_netbox.json', 'r') as f:
        raw_data = json.load(f)
        
    items = []
    for raw_item in raw_data:
        item = NetboxItem(**raw_item)
        items.append(item)
    return items

def get_statistics_by_role(role_slug: str):
    if role_slug != 'all':
        items = list(i for i in get_items() if i.role['slug'] == role_slug)
    else:
        allowed_roles = ["device_type","switch","router","server","cable-organizer","optical-cross","patch-panel","san-switch","ups","wireless-lan-controllers","all"]
        items = list(i for i in get_items() if i.role['slug'] in allowed_roles)

    statistics = {}

    for item in items:
        for k, v in item.__dict__.items():
            if k not in statistics:
                if k == 'custom_fields':
                    statistics[k] = {k1: 0 for k1, v1 in v.items()}
                else:
                    statistics[k] = 0
            
            if k == 'custom_fields':
                for k1, v1 in v.items():
                    if v1 != None:
                        statistics[k][k1] += 1
            
            else:
                if v != None and v != '':
                    statistics[k] += 1

    for k, v in statistics.items():
        if k != 'custom_fields':
            statistics[k] /= float(len(items))
            statistics[k] *= 100
            statistics[k] = f'{statistics[k] : .2f}'
        else:
            for k1, v1 in v.items():
                statistics[k][k1] /= float(len(items))
                statistics[k][k1] *= 100
                statistics[k][k1] = f'{statistics[k][k1] : .2f}'

    return statistics
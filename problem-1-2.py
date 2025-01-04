import json
from packaging.version import Version

# Helper functions to simulate OS inspection
def parse_json (path: str):
    with open(path, 'r') as file:
        return json.load(file)

def get_dmo_info (path='dmo.json'):
    return parse_json(path)

def get_dotnet_info (path='dotnet.json'):
    return parse_json(path)

def get_upgrade_status (upgrade_pref: bool) -> bool:
    dmo = get_dmo_info
    dotnet = get_dotnet_info

    if dotnet.Name == '.NET Framework' and dmo.Name == 'Nuance Dragon Medical One':
        if Version(dotnet.Version) >= Version('4.8.0'):
            False
        elif Version(dmo.Version) > Version('2020.1'):
            True
        else:
            upgrade_pref
    else:
        False

def main(upgrade_pref = True, restart = None):
    data = { 'title': '.NET Status for DMO' }
    data['upgrade'] = get_upgrade_status(upgrade_pref)
    data['restart'] = data['upgrade'] if restart == None else restart
    return json.dumps(data)
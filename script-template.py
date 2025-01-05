import argparse
import json
from packaging.version import Version

# Helper functions to simulate OS inspection
def parse_json (path: str):
    try:
        with open(path, 'r') as file:
            return json.load(file)
    except:
        pass

def get_dragon_info (path='dragon.json'):
    return parse_json(path)

def get_dotnet_info (path='dotnet.json'):
    return parse_json(path)

def get_upgrade_status (upgrade_pref: bool) -> bool:
    dragon = get_dragon_info()
    dotnet = get_dotnet_info()

    if dotnet is not None and dragon is not None:
        if (Version(dotnet['Version']) <= Version('4.5')) and (Version(dragon['Version']) > Version('2020.1')):
            return True
        return upgrade_pref
    return False

# parser = argparse.ArgumentParser(description='Determine whether to upgrade .NET Framework')
# parser.add_argument('--example', action='store_true', default=None)
# args = parser.parse_args()
## `args.example`` to access argument value

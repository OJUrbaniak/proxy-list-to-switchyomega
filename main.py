import json
import tkinter as tk
from tkinter import filedialog
import re

# Global var
proxies = []

def load_proxies():
    root = tk.Tk()
    root.withdraw()
    try:
        file_path = filedialog.askopenfilename()
        with open(file_path) as f:
            count = 0
            for line in f:
                p = re.compile('([0-9a-zA-Z.]+):([0-9a-zA-Z._-]+):([0-9a-zA-Z._-]+):([0-9a-zA-Z._-]+)')
                search = re.search(p, line)
                proxy = Proxy(search.group(1), search.group(2), search.group(3), search.group(4))
                proxies.append(proxy)
                count += 1
            return count
    except:
        print("Incorrect proxy file")
        return 0


class Proxy:
    def __init__(self, domain, port, username, password):
        self.password = password
        self.username = username
        self.port = port
        self.domain = domain


def convert():
    load_proxies()
    with open('converted_proxies_omega.bak', 'w') as f:
        f.truncate(0)
        print("The json file is created")
        base = {
            "-addConditionsToBottom": False,
            "-confirmDeletion": True,
            "-downloadInterval": 1440,
            "-enableQuickSwitch": False,
            "-monitorWebRequests": True,
            "-quickSwitchProfiles": [],
            "-refreshOnProfileChange": True,
            "-revertProxyChanges": True,
            "-showExternalProfile": True,
            "-showInspectMenu": True,
            "-startupProfileName": "",
            "schemaVersion": 2
        }
        base_name = "importedProxy_"
        for i, proxy in enumerate(proxies):
            proxy_name = (base_name + str(i))
            base["+"+proxy_name] = {
                "auth": {
                    "fallbackProxy": {
                        "password": proxy.password,
                        "username": proxy.username
                    }
                },
                "bypassList": [
                    {
                        "conditionType": "BypassCondition",
                        "pattern": "127.0.0.1"
                    },
                    {
                        "conditionType": "BypassCondition",
                        "pattern": "[::1]"
                    },
                    {
                        "conditionType": "BypassCondition",
                        "pattern": "localhost"
                    }
                ],
                "color": "#47b",
                "fallbackProxy": {
                    "host": proxy.domain,
                    "port": int(proxy.port),
                    "scheme": "http"
                },
                "name": proxy_name,
                "profileType": "FixedProfile",
                "revision": "1821c434d4e"
            }

        json.dump(base, f)

if __name__ == '__main__':
    convert()
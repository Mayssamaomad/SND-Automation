from utils.logger import get_logger
from .netconf_client import NetconfClient
from .restconf_client import RestconfClient

logger = get_logger("inventory")

class DeviceInventory:
    def __init__(self, device_list: dict):
        self.devices = device_list

    def pull_inventory(self):
        inventory = {}

        for name, device in self.devices.items():
            logger.info(f"Collecting inventory for {name}")

            if device["protocol"] == "netconf":
                client = NetconfClient(device["host"], device["username"], device["password"])
                inventory[name] = client.get_interfaces()

            elif device["protocol"] == "restconf":
                client = RestconfClient(device["host"], device["username"], device["password"])
                inventory[name] = client.get_inventory()

        return inventory

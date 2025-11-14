import requests
from utils.logger import get_logger

logger = get_logger("restconf")

class RestconfClient:
    def __init__(self, host, username, password):
        self.base_url = f"https://{host}/restconf"
        self.auth = (username, password)
        self.headers = {"Content-Type": "application/yang-data+json"}

    def get_inventory(self):
        url = f"{self.base_url}/data/ietf-network:networks"
        logger.info("Fetching RESTCONF inventory")
        response = requests.get(url, auth=self.auth, headers=self.headers, verify=False)
        return response.json()

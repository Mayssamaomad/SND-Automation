from devices.netconf_client import NetconfClient
from utils.logger import get_logger

logger = get_logger("deactivate")

class ServiceDeactivator:
    def __init__(self, device):
        self.device = device

    def deactivate_service(self, service_id: str):
        logger.info(f"Deactivating service: {service_id}")

        client = NetconfClient(
            host=self.device["host"],
            username=self.device["username"],
            password=self.device["password"]
        )

        payload = f"""
        <config>
            <l2vpn xmlns="urn:mycompany:services">
                <id>{service_id}</id>
                <state>inactive</state>
            </l2vpn>
        </config>
        """

        try:
            result = client.push_config(payload)
            logger.info(f"Service {service_id} deactivated.")
            return result
        except Exception as e:
            logger.error(f"Failed to deactivate: {e}")
            return None

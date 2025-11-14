from devices.netconf_client import NetconfClient
from utils.logger import get_logger

logger = get_logger("provision")

class ServiceProvisioner:
    def __init__(self, device):
        self.device = device

    def provision_l2vpn(self, service_data):
        logger.info(f"Provisioning service: {service_data['service_id']}")

        client = NetconfClient(
            host=self.device["host"],
            username=self.device["username"],
            password=self.device["password"]
        )

        # Example payload (edit this based on your platform)
        payload = f"""
        <config>
            <l2vpn xmlns="urn:mycompany:services">
                <id>{service_data['service_id']}</id>
                <ce>{service_data['ce']}</ce>
                <pe>{service_data['pe']}</pe>
            </l2vpn>
        </config>
        """

        return client.push_config(payload)

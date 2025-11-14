from ncclient import manager
from utils.logger import get_logger

logger = get_logger("netconf")

class NetconfClient:
    def __init__(self, host, username, password, port=830):
        self.host = host
        self.username = username
        self.password = password
        self.port = port

    def get_interfaces(self):
        filter_xml = """
        <filter>
            <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
        </filter>
        """

        with manager.connect(
            host=self.host,
            port=self.port,
            username=self.username,
            password=self.password,
            hostkey_verify=False
        ) as conn:
            logger.info(f"Fetching interface info from {self.host}")
            return conn.get(filter_xml).xml

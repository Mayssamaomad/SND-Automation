from utils.config import load_yaml
from services.provision import ServiceProvisioner

def main():
    devices = load_yaml("configs/devices.yml")
    services = load_yaml("configs/services.yml")

    provisioner = ServiceProvisioner(devices["router1"])
    
    for svc in services:
        result = provisioner.provision_l2vpn(svc)
        print(result)

if __name__ == "__main__":
    main()

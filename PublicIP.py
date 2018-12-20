import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

class PublicIP:
    def __init__(self, network_client, location, group_name, node_ip):
        self.network_client=network_client
        self.location=location
        self.group_name=group_name
        self.node_ip=node_ip

        # -------- Create the Public IP address for the VM -----
    def create_public_ip_address(self):
            public_ip_addess_params = {
                'location': self.location,
                'public_ip_allocation_method': 'Dynamic'
            }
            creation_result = self.network_client.public_ip_addresses.create_or_update(
                    self.group_name,
                    self.node_ip,
                    public_ip_addess_params
                )

            return creation_result.result()
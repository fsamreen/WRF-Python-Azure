import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption


class CreateNIC:
    def __init__(self, network_client, location, group_name, node_ip, node_nic):
        self.network_client = network_client
        self.location = location
        self.group_name = group_name
        self.node_ip = node_ip
        self.node_nic=node_nic

    # ------- Create a Network interface ------
    def create_nic(self):
        subnet_info = self.network_client.subnets.get(
            self.group_name,
            'myVNet',
            'mySubnet'
        )
        publicIPAddress = self.network_client.public_ip_addresses.get(
            self.group_name,
            self.node_ip
        )
        nic_params = {
            'location': self.location,
            'ip_configurations': [{
                'name': 'myIPConfig',
                'public_ip_address': publicIPAddress,
                'subnet': {
                    'id': subnet_info.id
                }
            }]
        }
        creation_result = self.network_client.network_interfaces.create_or_update(
            self.group_name,
            self.node_nic,
            nic_params
        )

        return creation_result.result()


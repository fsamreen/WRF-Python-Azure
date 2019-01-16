# """
# @Desc: creates a virtual network.
# @Input: location and resource group name.
# @Output: creates a virtual network within a resource group in a given location.
# """

import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption


class VirtualNet:
    def __init__(self, network_client, location, group_name):
        self.network_client = network_client
        self.location = location
        self.group_name = group_name

    # ------- Create subnet (A VM must be in a subnet of a virtiual network)----
    def create_vnet(self):
        vnet_params = {
            'location': self.location,
            'address_space': {
                'address_prefixes': ['10.2.0.0/16']
            }
        }
        creation_result = self.network_client.virtual_networks.create_or_update(
            self.group_name,
            'myVNet',
            vnet_params
        )
        return creation_result.result()

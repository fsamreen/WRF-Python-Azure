# """
# @Desc: creates a subnet.
# @Input: location and resource group name.
# @Output: creates a subnet in a given Resource Group.
# """

import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption


class Subnet:
    def __init__(self, network_client,group_name):
        self.network_client= network_client
        self.group_name=group_name

    # ------ Add subnet to a virtual network------
    def create_subnet(self):
        subnet_params = {
            'address_prefix': '10.2.0.0/16'
        }
        creation_result = self.network_client.subnets.create_or_update(
            self.group_name,
            'myVNet',
            'mySubnet',
            subnet_params
        )

        return creation_result.result()

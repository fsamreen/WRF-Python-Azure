# """
# @Desc: creates VM-specific resources.
# @Input: objects of ResourceGroup, AvailabilitySet, VirtualNet and Subnet.
# @Output: creates subnet in a virtual network within a defined resource group and location.
# """

import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from ReseourceGroup import ResourceGroup
from AvailabilitySet import AvailabilitySet
from VirtualNet import VirtualNet
from Subnet import Subnet

class VmResources(ResourceGroup,AvailabilitySet,VirtualNet,Subnet):
    def __init__(self,resource_group_client, network_client,compute_client,location,group_name ):
        self.resource_group_client=resource_group_client
        self.network_client=network_client
        self.compute_client=compute_client
        self.location=location
        self.group_name=group_name

    def create_vm_resources(self):
        self.create_resource_group()
        self.create_availability_set()
        self.create_vnet()
        self.create_subnet()

# """
# @Desc: creates availability set.
# @Input: location and resource group name.
# @Output: creates availability set within a resource group in a given location.
# """

import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption


class AvailabilitySet:
    def __init__(self, compute_client, location, group_name):
        self.compute_client=compute_client
        self.location=location
        self.group_name=group_name

    def create_availability_set(self):
        avset_params = {
            'location': self.location,
            'sku': {'name': 'Aligned'},
            'platform_fault_domain_count': 3
        }
        availability_set_result = self.compute_client.availability_sets.create_or_update(
            self.group_name,
            'myAVSet',
            avset_params
        )

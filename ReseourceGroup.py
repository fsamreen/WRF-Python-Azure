import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

class ResourceGroup:
    def __init__(self, reseource_group_client, location, group_name):
        self.resource_group_client=reseource_group_client
        self.location=location
        self.group_name=group_name
    # ------Create the VM supporting resources ------

    def create_resource_group(self):
        resource_group_params = {'location': self.location}
        resource_group_result = self.resource_group_client.resource_groups.create_or_update(
            self.group_name,
            resource_group_params
        )

    def delete_resource_group(self):
        delete_async_operation = self.resource_group_client.resource_groups.delete(self.group_name)
        delete_async_operation.wait()


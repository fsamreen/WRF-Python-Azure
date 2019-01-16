# """
# @Desc: parse the credential file to extract relevant information.
# @Input: '.txt' file (credentials.txt)
# @Output: subscriptionID, clientID, tenantID, secreteID and credentials as a complete object.
# """

import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

class AzureCredentials:
    def __init__(self, filename):
        self.filename=filename

    def get_subscription_id(self):
        file = open(self.filename, "r")
        line = file.readlines()
        fields = line[0].split(" ")
        subscriptionID = fields[1]
        return subscriptionID

    def get_client_id(self):
        file = open(self.filename, "r")
        line = file.readlines()
        fields = line[1].split(" ")
        clientID = fields[1]
        return clientID

    def get_secret_id(self):
        file = open(self.filename, "r")
        line = file.readlines()
        fields = line[1].split(" ")
        fields = line[2].split(" ")
        secreteID = fields[1]
        fields = line[3].split(" ")
        return secreteID

    def get_tenant_id(self):
        file = open(self.filename, "r")
        line = file.readlines()
        fields = line[1].split(" ")
        fields = line[2].split(" ")
        fields = line[3].split(" ")
        tenantID = fields[1]
        return tenantID


    def get_credentials(self):
        file = open(self.filename, "r")
        line = file.readlines()
    # fields=line[0].split(" ")
    # SUBSCRIPTION_ID=fields[1]
        fields = line[1].split(" ")
        ClientID = fields[1]
        fields = line[2].split(" ")
        SecreteID = fields[1]
        fields = line[3].split(" ")
        TenantID = fields[1]
        credentials = ServicePrincipalCredentials(
        client_id=ClientID,
        secret=SecreteID,
        tenant=TenantID
        )

        return credentials

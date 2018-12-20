import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from VirtualMachine import VirtualMachine

#node_ip1='nodeIP'
#node_nic1='node_nic'
#vm_name1='WRF_Node'

class CreateCluster(VirtualMachine):
    def __init__(self,network_client,compute_client, location, group_name, user_name, password, number_nodes):
      #  VirtualMachine.__init__(self,network_client,compute_client, location, group_name, user_name, password,node_ip,node_nic,vm_name)
       # self.node_ip=node_ip
        #self.node_nic=node_nic
        #self.vm_name=vm_name
        self.network_client=network_client
        self.compute_client=compute_client
        self.location=location
        self.group_name=group_name
        self.user_name=user_name
        self.password=password
        #self.node_ip=node_ip
        self.number_nodes=number_nodes

    def cluster(self):
        node_ip='nodeIP2'
        self.create_public_ip_address(self,node_ip)

        #for i in range(1, self.number_nodes):
        #    node_ip = node_ip1  + str(i)
         #   creation_result = self.create_public_ip_address(self.network_client, node_ip)
         #   print('*****************************************************************************')
         #   print(' Step 5: Public IP is created.........................')
         #   print('*****************************************************************************')
         #   node_nic = node_nic1 + str(i)
         #   creation_result = self.create_nic(self.network_client, node_ip, node_nic)
         #   print('*****************************************************************************')
         #   print(' Step 6: Network Interface is created.........................')
         #   print('*****************************************************************************')
         #   vm_name = vm_name1 + str(i)
         #   if i == 1:
         #       creation_result = self.create_vm_master(self.network_client, self.compute_client, node_nic, vm_name)
         #       print('*****************************************************************************')
         #       print(' Step 7: VM is created.........................')
         #       print('*****************************************************************************')
         #   else:
         #       creation_result = self.create_vm_client(self.network_client, self.compute_client, node_nic, vm_name)
         #       print('*****************************************************************************')
         #       print(' Step 7: VM is created.........................')
         #       print('*****************************************************************************')

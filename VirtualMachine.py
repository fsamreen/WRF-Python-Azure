import azure
from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption

#node_ip1='nodeIP'
#node_nic1='node_nic'
#vm_name='WRF_Node'

class VirtualMachine:
    def __init__(self, network_client,compute_client,location,group_name,user_name, password,node_nic,vm_name):
        self.network_client=network_client
        self.compute_client=compute_client
        self.location=location
        self.group_name=group_name
        self.user_name=user_name
        self.password=password
        #self.number_nodes=number_nodes
        #self.node_ip=node_ip
        self.node_nic=node_nic
        self.vm_name=vm_name


    # ------- Create a Virtual Machine ------
    # two kind of machines can be generated, a master node and a client node.
    # Under TESTING
    def create_vm_master(self):
        nic = self.network_client.network_interfaces.get(
            self.group_name,
            self.node_nic
        )
        avset = self.compute_client.availability_sets.get(
            self.group_name,
            'myAVSet'
        )
        vm_parameters = {
            'location': self.location,
            'os_profile': {
                'computer_name': self.vm_name,
                'admin_username': self.user_name,
                'admin_password': self.password
            },
            'hardware_profile': {
                #'vm_size': 'Standard_DS1_v2'
                #'vm_size': 'Standard_D4s_V3' ### did not work for this machine
                'vm_size': 'Standard_D8s_V3'
            },
            ####client machine
            # 'storage_profile': {
            #   'image_reference': {
            #  'id' : ''
            # }
            ##### master node
            'storage_profile': {
                'image_reference': {
                    #'id': ''
                    #'id': ''
                    #'id': ''
                    'id': ''
                }
                # 'storage_profile': {
                #   'image_reference': {
                #      'publisher': 'MicrosoftWindowsServer',
                #     'offer': 'WindowsServer',
                #    'sku': '2012-R2-Datacenter',
                #   'version': 'latest'
                # }
            },
            'network_profile': {
                'network_interfaces': [{
                    'id': nic.id
                }]
            },
            'availability_set': {
                'id': avset.id
            }
        }
        creation_result = self.compute_client.virtual_machines.create_or_update(
            self.group_name,
            self.vm_name,
            vm_parameters
        )

        return creation_result.result()

    # Create client machine.....
    def create_vm_client(self):
        nic = self.network_client.network_interfaces.get(
            self.group_name,
            self.node_nic
        )
        avset = self.compute_client.availability_sets.get(
            self.group_name,
            'myAVSet'
        )
        vm_parameters = {
            'location': self.location,
            'os_profile': {
                'computer_name': self.vm_name,
                'admin_username': self.user_name,
                'admin_password': self.password
            },
            'hardware_profile': {
                #'vm_size': 'Standard_DS1_v2'
                #'vm_size': 'Standard_D4s_V3'
                'vm_size': 'Standard_D8s_V3'
            },
            ####client machine
             'storage_profile': {
               'image_reference': {
              'id' : ''
             }
            ##### master node
            #'storage_profile': {
            #    'image_reference': {
            #        'id': ''
             #   }
                # 'storage_profile': {
                #   'image_reference': {
                #      'publisher': 'MicrosoftWindowsServer',
                #     'offer': 'WindowsServer',
                #    'sku': '2012-R2-Datacenter',
                #   'version': 'latest'
                # }
            },
            'network_profile': {
                'network_interfaces': [{
                    'id': nic.id
                }]
            },
            'availability_set': {
                'id': avset.id
            }
        }
        creation_result = self.compute_client.virtual_machines.create_or_update(
            self.group_name,
            self.vm_name,
            vm_parameters
        )

        return creation_result.result()



#class CreateCluster(VirtualMachine):
 #   def __init__(self,network_client,compute_client, location, group_name, user_name, password, number_nodes):
  #      VirtualMachine.__init__(self,network_client,compute_client, location, group_name, user_name, password)
   #     self.number_nodes=number_nodes

    #def cluster(self):
     #   for i in range(1, self.number_nodes):
      #      node_ip = node_ip  + str(i)
       #     creation_result = self.create_public_ip_address(self.network_client, node_ip)
        #    print('*****************************************************************************')
         #   print(' Step 5: Public IP is created.........................')
          #  print('*****************************************************************************')
           # node_nic = node_nic + str(i)
            #creation_result = self.create_nic(self.network_client, node_ip, node_nic)
            #print('*****************************************************************************')
            #print(' Step 6: Network Interface is created.........................')
            #print('*****************************************************************************')
            #vm_name = vm_name + str(i)
            #if i == 1:
            #    creation_result = self.create_vm_master(self.network_client, self.compute_client, node_nic, vm_name)
             #   print('*****************************************************************************')
              #  print(' Step 7: VM is created.........................')
              #  print('*****************************************************************************')
            #else:
             #   creation_result = self.create_vm_client(self.network_client, self.compute_client, node_nic, vm_name)
              #  print('*****************************************************************************')
               # print(' Step 7: VM is created.........................')
                #print('*****************************************************************************')








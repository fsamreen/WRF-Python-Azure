from azure.common.credentials import ServicePrincipalCredentials
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient
from azure.mgmt.network import NetworkManagementClient
from azure.mgmt.compute.models import DiskCreateOption
from AzureCredentials import AzureCredentials
from ReseourceGroup import ResourceGroup
from AvailabilitySet import AvailabilitySet
from VirtualNet import VirtualNet
from Subnet import Subnet
from VirtualMachine import VirtualMachine
from CreateCluster import CreateCluster
from PublicIP import PublicIP
from CreateNIC import CreateNIC
from VmResources import VmResources
from GetIP import GetIP


# ---- Define variable values .......
# ----Default values are given, could be changhed accordingly....
File_Name = "credentials.txt"
Location= 'westeurope'
Group_Name='WRFPhase2'
vm_name='wrfnode'
node_ip='nodeIP'
node_nic='nodeNI'
user_name='wrfuser'
password='xyz'
number_nodes=3


# ---- Call object of Azurecredential class to get credentials .....
#----------------------------------------------------------------------
# ---- i.e. Resource group, Availability Set, Virtual Network and Subnet.
credential_object=AzureCredentials(File_Name)
subscription_id=credential_object.get_subscription_id()
credentials=credential_object.get_credentials()

# ---- Initialise the management clients....
resource_group_client = ResourceManagementClient(
    credentials,
    subscription_id
)
network_client = NetworkManagementClient(
    credentials,
    subscription_id
)
compute_client = ComputeManagementClient(
    credentials,
    subscription_id
)

# ---- Create all VM specific resources on Azure .....
#-----------------------------------------------------
# i.e. Resource group, Availability Set, Virtual Network and Subnet.
# An alternate way of creating each resource is given under "Alternate-Code-1".

create_resource_object=VmResources(resource_group_client,network_client,compute_client,Location,Group_Name)
create_resource_object.create_vm_resources()

# ---- Create an MPI and NFS supported Cluster to run WRF simulation ....
#------------------------------------------------------------------------
# A cluster is created using pre-built machine images of master and client nodes, where WRF and all the dependencies
# are already installed on these images.

for i in range(1,number_nodes):
    public_ip_object=PublicIP(network_client,Location,Group_Name,node_ip=node_ip+str(i))
    nic_object=CreateNIC(network_client,Location,Group_Name,node_ip=node_ip+str(i),node_nic=node_nic+str(i))
    if i ==1:
        vm_object=VirtualMachine(network_client,compute_client,Location,Group_Name,user_name,password,node_nic=node_nic+str(i),vm_name="wrfmaster")
    else:
        vm_object = VirtualMachine(network_client, compute_client, Location, Group_Name, user_name, password,
                                   node_nic=node_nic + str(i), vm_name=vm_name + str(i))
    public_ip_object.create_public_ip_address()
    nic_object.create_nic()
    if i==1:
        vm_object.create_vm_master()
    else:
        vm_object.create_vm_client()
# ------ end of create cluster....

## ---- Get Public IP .....
# Sort passwor-less access in a cluster.
public_ip_object=GetIP(network_client,Group_Name,number_nodes)

public_ip_object.get_write_public_ip()

public_ip_object.execute_ssh_command()



# ---- Alternate-Code-1 ----
#-----------------------------------------------------------------------
# ---- Create a resource group in Azure ....
#resource_group_object=ResourceGroup(resource_group_client,Location,Group_Name)
#resource_group_object.create_resource_group()

# --- Create availability set in Azure ....
#availability_set_object=AvailabilitySet(compute_client,Location,Group_Name)
#availability_set_object.create_availability_set()

# --- Create VirtualNetwork in Azure ....
#vnet_object=VirtualNet(network_client,Location,Group_Name)
#vnet_object.create_vnet()

# ---- Create Subnetwork in Azure ....
#subnet_object=Subnet(network_client,Group_Name)
#subnet_object.create_subnet()
# ------------- end of Alternate-Code-1-------------------------------

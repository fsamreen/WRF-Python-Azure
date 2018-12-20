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
File_Name = "credentials.txt"
Location= 'westeurope'
Group_Name='WRFPhase2'
vm_name='wrfnode'
node_ip='nodeIP'
node_nic='nodeNI'
#user_name='wrfuser'
#password=''
user_name='wrfuser'
password='Ensemble@2017'
number_nodes=3


# ---- Call object of Azurecredential class to get credentials .....
credential_object=AzureCredentials(File_Name)
subscription_id=credential_object.get_subscription_id()
credentials=credential_object.get_credentials()
print(credentials)
print(subscription_id)

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
create_resource_object=VmResources(resource_group_client,network_client,compute_client,Location,Group_Name)
create_resource_object.create_vm_resources()

#------ create each resource separately---- sub classes of above........
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
# ------------- end of create each resource -------------------------------

# ---- Create Cluster ....
#for i in range(1,number_nodes):
 #   public_ip_object=PublicIP(network_client,Location,Group_Name,node_ip=node_ip+str(i))
  #  nic_object=CreateNIC(network_client,Location,Group_Name,node_ip=node_ip+str(i),node_nic=node_nic+str(i))
   # if i ==1:
    #    vm_object=VirtualMachine(network_client,compute_client,Location,Group_Name,user_name,password,node_nic=node_nic+str(i),vm_name="wrfmaster")
    #else:
     #   vm_object = VirtualMachine(network_client, compute_client, Location, Group_Name, user_name, password,
      #                             node_nic=node_nic + str(i), vm_name=vm_name + str(i))
    #public_ip_object.create_public_ip_address()
    #nic_object.create_nic()
    #if i==1:
     #   vm_object.create_vm_master()
    #else:
     #   vm_object.create_vm_client()

# ------ end of create cluster....

# ---- Create Cluster with try catch....
#### write commands

# ---- Get Public IP .....

#public_ip_object=GetIP(network_client,Group_Name,number_nodes)

#public_ip_object.get_write_public_ip()

#public_ip_object.execute_ssh_command()




###public_ip_object.get_public_ip()
#(stdoutstring, stderrstring)=public_ip_object.execute_ssh_command()
#for stdoutrow in stdoutstring:
 #   print (stdoutrow)
#public_ip_object.execute_command()


#print(public_ip)

#ip=public_ip_object.write_host_file()


#file=open("tasty.txt", "a")
#file.write(public_ip + " " + "hello\n")

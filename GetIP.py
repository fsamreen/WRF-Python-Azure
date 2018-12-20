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
# This code will copy any file from the local directory to the virtual machine.
import paramiko
import sys, os, time

#paramiko.util.log_to_file('/Users/samreen/Documents/Jupyter2018/testscript.sh')


class GetIP():
    def __init__(self, network_client, group_name, i):
        self.network_client=network_client
        self.group_name=group_name
        #self.my_ip=my_ip
        self.i=i

    def get_public_ip(self):
        rng=self.i
        for l in range(1, rng):
            my_ip="nodeIP"+str(l)
            public_ip_address = self.network_client.public_ip_addresses.get(self.group_name, my_ip)
            public_ip = public_ip_address.ip_address
           # private_ip = public_ip_address.ip_configuration.private_ip_address
            print("Public IP of node" + str(l) + ": "+ public_ip_address.ip_address)
            #print(public_ip_address.ip_configuration.private_ip_address)

        # print current file path and directory ----
        print(repr(sys.argv[0]))
        print(os.path.dirname(__file__)+'/hostname.sh')


        # list all files in the current directory----
        files= [f for f in os.listdir('.') if os.path.isfile(f)]
        for f in files:
            print(f)

        #return public_ip

    def get_write_public_ip(self):
        os.remove(os.path.dirname(__file__) + '/hostname.sh')
        file = open("hostname.sh", "a")
        file.write("#!/bin/bash" + "\n")
        port=22
        rng = self.i
        for j in range(1, rng):
            ip="nodeIP"+str(j)
            public_ip_address = self.network_client.public_ip_addresses.get(self.group_name, ip)
            public_ip = public_ip_address.ip_address
            #private_ip = public_ip_address.ip_configuration.private_ip_address
            print("Public IP of node" + str(j) + ": " + public_ip_address.ip_address)
            #print(public_ip_address.ip_configuration.private_ip_address)
            if j==1:
                file.write("sed -i " + "\"" + str(j+1) + "i " + public_ip + " " + "wrfmaster" + "\"" + " /etc/hosts\n")
            else:
                file.write("sed -i " + "\"" + str(j + 1) + "i " + public_ip + " " + "wrfnode" + str(
                    j) + "\"" + " /etc/hosts\n")

        file.close()
        for k in range(1, rng):
            ip = "nodeIP" + str(k)
            public_ip_address = self.network_client.public_ip_addresses.get(self.group_name, ip)
            host = public_ip_address.ip_address
            transport = paramiko.Transport((host, port))

            # Auth
            password = "Faiza@1234567"
            username = "wrfuser"
            transport.connect(username=username, password=password)

            # Go!
            sftp = paramiko.SFTPClient.from_transport(transport)

            # Download
            # filepath = '/etc/passwd'
            # localpath = '/home/remotepasswd'
            # sftp.get(filepath, localpath)

            # Upload

            filepath = '/home/wrfuser/hostname.sh'
            # for Jupyter--#localpath = '/Users/.../hostname.sh'
            #localpath = '/Users/...../hostname.sh'
            localpath=os.path.dirname(__file__) + '/hostname.sh'
            sftp.put(localpath, filepath)

            # Close

            sftp.close()
            transport.close()

        #return public_ip


    def execute_ssh_command(self):
        """
        execute_ssh_command(host, port, username, password, keyfilepath, keyfiletype, command) -> tuple

        Executes the supplied command by opening a SSH connection to the supplied host
        on the supplied port authenticating as the user with supplied username and supplied password or with
        the private key in a file with the supplied path.
        If a private key is used for authentication, the type of the keyfile needs to be specified as DSA or RSA.
        :rtype: tuple consisting of the output to standard out and the output to standard err as produced by the command
        """
        port = 22
        username = 'wrfuser'
        password = 'Faiza@1234567'
        keyfilepath = None
        keyfiletype = None
        #independent command# command = "echo Faiza@1234567 | sudo -S sh /home/wrfuser/hostname.sh"
        command = "echo Faiza@1234567 | sudo -S sh /home/wrfuser/hostname.sh;echo Faiza@1234567 | sudo -S mount /dev/sdc1 /wrfstorage;ssh-keygen -R wrfmaster >> /home/wrfuser/.ssh/known_hosts"
        command1 = "echo Faiza@1234567 | sudo -S sh /home/wrfuser/hostname.sh;echo Faiza@1234567 | sudo -S mount wrfmaster:/wrfstorage /wrfstorage;echo Faiza@1234567 | sudo -S mount -a;ssh-keygen -R wrfmaster >> /home/wrfuser/.ssh/known_hosts;echo yes | ssh wrfmaster hostname;cp ~/.ssh/authorized_key /wrfstorage;cp /wrfstorage/authorized_key /home/wrfuser/.ssh/"
        command2= "echo Faiza@1234567 | sudo -S mount /dev/sdc1 /wrfstorage"
        command3 = "echo Faiza@1234567 | sudo -S mount wrfmaster:/wrfstorage /wrfstorage"
        command4 = "echo Faiza@1234567 | sudo -S mount -a"
        command5 = "ssh-keygen -R wrfmaster >> /home/wrfuser/.ssh/known_hosts"
        #ssh-keygen -f "/home/wrfuser/.ssh/known_hosts" -R wrfmaster
        command6 = "echo yes | ssh wrfmaster hostname"
        command7 = "cp ~/.ssh/authorized_key /wrfstorage"
        command8 = "cp /wrfstorage/authorized_key /home/wrfuser/.ssh/"
        command9="ssh-keyscan -H wrfmaster >> ~/.ssh/known_hosts"
        command10 = "ssh-keyscan -H wrfnode2 >> ~/.ssh/known_hosts"

        ssh = None
        key = None
        rng=self.i
        for k in range(1, rng):
            ip = "nodeIP" + str(k)
            public_ip_address = self.network_client.public_ip_addresses.get(self.group_name, ip)
            host = public_ip_address.ip_address
            print("***" + host)

            try:
                if keyfilepath is not None:
                    # Get private key used to authenticate user.
                    if keyfiletype == 'DSA':
                        # The private key is a DSA type key.
                        key = paramiko.DSSKey.from_private_key_file(keyfilepath)
                    else:
                        # The private key is a RSA type key.
                        key = paramiko.RSAKey.from_private_key(keyfilepath)

                # Create the SSH client.
                ssh = paramiko.SSHClient()

                # Setting the missing host key policy to AutoAddPolicy will silently add any missing host keys.
                # Using WarningPolicy, a warning message will be logged if the host key is not previously known
                # but all host keys will still be accepted.
                # Finally, RejectPolicy will reject all hosts which key is not previously known.
                ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

                # Connect to the host.
                if key is not None:
                    # Authenticate with a username and a private key located in a file.
                    ssh.connect(host, port, username, None, key)
                else:
                    # Authenticate with a username and a password.
                    ssh.connect(host, port, username, password)

                # Send the command (non-blocking)
                if k==1:
                    stdin, stdout, stderr = ssh.exec_command(command)
                    for p in range(2,rng):
                        command10 = "ssh-keyscan -H " + "wrfnode"+str(p)+" >> ~/.ssh/known_hosts"
                        stdin, stdout, stderr = ssh.exec_command(command10)
                    #stdin, stdout, stderr = ssh.exec_command(command2)
                    #stdin, stdout, stderr = ssh.exec_command(command5)
                    #old#stdin, stdout, stderr = ssh.exec_command(command10)

                else:
                    print("hello")
                    stdin, stdout, stderr = ssh.exec_command(command1)
                    #stdin, stdout, stderr = ssh.exec_command(command)
                    #stdin, stdout, stderr = ssh.exec_command(command3)
                    #stdin, stdout, stderr = ssh.exec_command(command4)
                    #stdin, stdout, stderr = ssh.exec_command(command5)
                    #stdin, stdout, stderr = ssh.exec_command(command6)
                    #stdin, stdout, stderr = ssh.exec_command(command7)
                    #stdin, stdout, stderr = ssh.exec_command(command8)
                    #stdin, stdout, stderr = ssh.exec_command(command9)
                    #command10 = "ssh-keyscan -H " + "wrfnode"+str(k)+" >> ~/.ssh/known_hosts"
                    #stdin, stdout, stderr = ssh.exec_command(command10)

                # Wait for the command to terminate
                while not stdout.channel.exit_status_ready() and not stdout.channel.recv_ready():
                    time.sleep(1)

                #stdoutstring = stdout.readlines()
                #stderrstring = stderr.readlines()
                #return stdoutstring, stderrstring
            finally:
                if ssh is not None:
                    # Close client connection.
                    ssh.close()


    ######### Not in use function ------
    def write_host_file(self):
        file = open("hostname.sh", "a")
        file.write("#!/bin/bash" + "\n")
        rng=self.i
        for j in range (1, rng):
            myip="nodeIP"+str(j)
            public_ip_address = self.network_client.public_ip_addresses.get(self.group_name, myip)
            public_ip = public_ip_address.ip_address
            # any of these forms could be used to write in a file...... sed option is preferrable.....
            # dont delete ##file.write("echo " + "\"" + public_ip + " " + "wrfnode" + str(j) + "\"" + " " + "|" + " " + "tee -a /etc/hosts" + "\n")
            file.write("sed -i " + "\"" + str(j) + "i " + public_ip + " " + "wrfnode" + str(j) + "\"" + " /etc/hosts")
            file.close()


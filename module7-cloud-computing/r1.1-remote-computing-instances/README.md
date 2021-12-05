# Remote computing instances

A computer running in the cloud is a remote computer that is also known as **Instance**. It is usually either a bare-metal machine dedicated to you or a virtual machine that is provisioned for you using virtualization technology. Cloud computers are quite similar to your personal computer for all intents and purposes. They can run any operating system you require and have the necessary hardware to function like CPUs, Memory, Storage Devices, and Network adapters.

A cloud instance requires an operating system to be installed on it so it can provide basic functionality, and offer you a way to connect to it. In this lesson, we will explore how to connect to a cloud instance. We will explore new protocols like SSH, SCP, and RDP that help us connect to remote systems.

## The OS

Cloud providers have lots of offerings that can be tailored to your business needs. Two of these offerings are Infrastructure as a Service (IaaS), and Platform as a Service (PaaS). These will be covered in depth later in this course. However, for this lesson, we will consider the IaaS offering as it allows us to run computing instances.

All IaaS providers offer consoles and tools that help you manage the infrastructure, like creating and managing instances, allocating storage, defining a network, etc. Whenever you create a machine, you will have to also select an operating system that will get installed on that machine. These OSes are usually offered in what is called an Image.

In the instance creation wizard, you can select the type of image that will get installed. There are usually standard images that are created by the cloud provider, community images that are created by 3rd parties, and custom images that you or your team creates.

An image is a bundle of software that contains the operating system alongside tools and configurations that the image creator adds to serve a purpose. For example, there are images for most popular Linux distributions, some of these images come with preconfigured servers or apps like WordPress images. You can also run Microsoft Windows and Windows Server images.

For running most web applications, Linux is usually the preferred choice for OS. You might need Windows Server if your web app is ASP.NET based. Otherwise, Linux is the industry standard web hosting OS.

## Ports

In computer networking, a port is a communication endpoint. It is a virtual place within an operating system where a network connection starts and ends. Ports help computers sort the network traffic they receive.

Ports are software-based and managed by a computer's operating system. Each port is associated with a specific process or service. Ports allow computers to easily differentiate between different kinds of traffic: emails go to a different port than webpages, for instance, even though both reach a computer over the same Internet connection and address (IP).

Ports are standardized across all network-connected devices, with each port assigned a number. Most ports are reserved for certain protocols — for example, all Hypertext Transfer Protocol (HTTP) messages go to port `80`. Secure HTTP (HTTPS) on the other hand uses port `443`. While IP addresses enable messages to go to and from specific devices, port numbers allow targeting of specific services or applications within those devices.

So far, when running our servers, we were using ports like 3000, 5000, etc. For instance, when Node.js server is started and is listening to port `3000`, that port will be reserved by the OS to that Node.js process. Any connection that comes over port `3000` will be directed to that Node.js process which will be able to handle it and read the transmitted data. This means that two processes can't use or listen to the same port.

The OS or the cloud infrastructure has network protection in place that guards these ports. It is called a firewall, which blocks access to ports by default unless specified otherwise by a _rule_. A rule is to either accept or deny a connection based on the port, the type of the port, the connecting host, or the connecting network. For example, accept connections on TCP port 22 only from a machine with a specific IP address. Otherwise, the connection should be rejected.

Some cloud vendors offer virtual firewalls that can be managed through their consoles. For example, AWS uses [Security Groups](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_SecurityGroups.html). Other vendors like DigitalOcean, fallback onto the firewall shipped with the OS like [UFW](https://wiki.ubuntu.com/UncomplicatedFirewall) for Ubuntu, or [Windows Firewall](https://www.vultr.com/docs/how-to-configure-the-firewall-on-windows-server-2019).

This is connected to our remote computing instances because they are by default also isolated through a firewall. You have to open the required port if you want to host a web server, or to accept remote connections.

## Remote Desktop Protocol (RDP)

To connect to a remote Windows instance, you need to use an RDP-compatible app. If you want to connect from a machine that runs Windows as well, then the app comes preinstalled by default by the name "Remote Desktop Connection". This tool lets you connect and stream what is on the remote computer display so you can interact with the graphical user interface (GUI) using your mouse and keyboard. The protocol also supports file sharing so you can transfer files between your machine and the remote instance. This protocol uses the port `3389`.

There are lots of [tutorials](https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/connecting_to_windows_instance.html) online that go step by step on how to connect using RDP. However, we won't go into further details in this lesson.

## Secure Socket Shell (SSH)

Secure Shell is a network communication protocol that enables two computers to communicate and share data. An inherent feature of ssh is that the communication between the two computers is encrypted meaning that it is suitable for use on insecure networks. SSH is most commonly used with Unix-based systems but now it is also supported in Windows.

SSH is often used to "login" and perform operations on remote computers. On Linux, it will give a shell to run your commands as if you were working on that computer directly. SSH uses port `22` by default.

To connect to a remote host (remote machine), the basic command you can run in any terminal is:

```bash
ssh REMOTE_HOST
```

The `REMOTE_HOST` in this example is the IP address or domain name of the machine you are trying to connect to.

This command assumes that your username on the remote system is the same as your username on your local system.

If your username is different on the remote system, you can specify it by using this syntax:

```bash
ssh REMOTE_USERNAME@REMOTE_HOST
```

Once you have connected to the server, you may be asked to verify your identity by providing a password. Later, we will cover how to generate keys to use instead of passwords.

To exit the ssh session and return into your local shell session, type:

```bash
exit
```

SSH works by connecting a client program `ssh` to an ssh server, called `sshd` or SSH Daemon. If you run an image that comes with SSH server already installed, the ssh server would be already running on the `REMOTE_HOST` that we specified.

On your server, the `sshd` server should already be running. If this is not the case, you may need to access your server through a web-based console, or local serial console.

The process needed to start an ssh server depends on the distribution of Linux that you are using.

On Ubuntu, you can start the ssh server by typing:

```bash
sudo systemctl start ssh
```

That should start the `sshd` server and you can then log in remotely.

You can login to a secure shell using passwords if accepted by the remote configuration. Otherwise, it can be better and faster to use key-based authentication.

Key-based authentication works by creating a pair of keys: a `private key` and a `public key`. The private key is located on your local machine (the client computer) and is secured and kept secret. The public key can be given to anyone or placed on any server you wish to access (the remote instance).

When you attempt to connect using a key-pair, the server will use the public key to create an encrypted message for the client computer that can only be decrypted with the private key. The client computer then sends the decrypted response back to the server and the server will know that the client is legitimate effectively letting the client in. This entire process is done automatically after you set up keys.

### How to create SSH Keys

SSH keys should be generated on the computer you wish to log in from. This is usually your local machine.

Enter the following into the command line and press enter to accept the defaults:

```bash
ssh-keygen -t rsa
```

Your keys will be created at `~/.ssh/id_rsa.pub` and `~/.ssh/id_rsa`. 

Change directory into the `.ssh` directory by typing `cd ~/.ssh` then list the files `ls -l` you will get this output if your local machine is using a UNIX-based system (assuming your username is `demo`):

```bash
-rw-r--r-- 1 demo demo  807 Dec  9 22:15 authorized_keys
-rw------- 1 demo demo 1679 Dec  9 23:13 id_rsa
-rw-r--r-- 1 demo demo  396 Dec  9 23:13 id_rsa.pub
```

As you can see, the **private key** `id_rsa` file is readable and writable only to the owner. This is how it should be to keep it secret.

The **public key** `id_rsa.pub` file, however, can be shared and has permissions appropriate for this activity. It should be transferred to your remote instance so you can use it to login. If you currently have password-based access to a server, you can copy your public key to it by issuing this command:

```bash
ssh-copy-id REMOTE_HOST
```

This will start an SSH session. After you enter your password, it will copy your public key to the server’s authorized keys file, which will allow you to log in without the password next time.

If you don't have password access to the remote server, then you need to put the public key contents inside your remote instance in the file called `authorized_keys` that is located in `~/.ssh` inside the remote instance. The content of `id_rsa.pub` should be appended entirely to the `authorized_keys` file. You can do this using vendor-based ssh console access. 

Alternatively, the vendor has to offer you a way to set up keys on the machine so you can connect to it. For example, AWS offers auto-generated private/public key-pair upon instance creation. You should download the generated private key to your machine so you can use it. If you lose it you will lose access to that machine.

To connect to the remote instance using the private key, you can use the command (assuming the remote username `demo`):

```bash
ssh -i ~/.ssh/id_rsa demo@REMOTE_HOST
```

Or you can automate identity association using the ssh configuration file as explored in [this tutorial](https://linuxize.com/post/using-the-ssh-config-file/).

## Secure Copy Protocol (SCP)

SCP is a file transfer protocol based on SSH. It uses the same port and can easily transfer files between local and remote hosts or between 2 remote hosts. SCP is considered outdated and inflexible. But it is still secure to copy files quickly. To copy from the remote host to the local machine, the syntax is as follows:

```bash
# For single file
scp demo@REMOTE_HOST:PATH_TO_REMOTE_FILE LOCAL_PATH

# For folder transfer
scp -r demo@REMOTE_HOST:PATH_TO_REMOTE_FOLDER LOCAL_PATH
```

To copy from local host to remote host, simply reverse the FROM/TARGET. You can also use the private key using the `-i` option:

```bash
scp -i ~/.ssh/id_rsa PATH_TO_LOCAL_FILE demo@REMOTE_HOST:REMOTE_PATH
```
When working with lots of files, you might be better off using the newer Secure File Transfer Protocol (SFTP) for this purpose. It is covered in depth in this [article](https://hevodata.com/learn/file-transfer-using-sftp/).


## Conslusion

In this lesson, we discovered how to connect to remote computers so we can set them up to host our web applications. If your server is Node.js based, it is recommended that you go with a Linux server, like Ubuntu, or Debian. You can connect to the remote machine using SSH with SSH Keys securely so you can set up the machine and deploy your apps. 

Always remember to make sure all the needed ports are open. Mostly ports 80 and 443 for HTTP and HTTPs respectively should be open to all so people can access your server. While ports like 22 shouldn't be open to all, preferably only to your local machine public IP address.

Always generate SSH Keys and keep them safe. If you lose a private key, you won't be able to login to a remote machine again. If your private key is leaked, then everyone can access your server and tamper with it.

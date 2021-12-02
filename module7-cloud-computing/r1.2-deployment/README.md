# Deployment

Once your site is finished (or finished "enough" to start public testing) you're going to need to host it somewhere more public and accessible than your personal development computer.

Up to now, you've been working in a development environment, using Express/Node as a web server to share your site to the local browser/network, and running your website with (insecure) development settings that expose debugging and other private information.

## Production Enviroment

The production environment is the environment provided by the server computer where you will run your website for external consumption. The environment includes:

- Computer hardware on which the website runs.
- Operating system (e.g. Linux or Windows).
- Programming language runtime and framework libraries on top of which your website is written.
- Web server infrastructure, possibly including a web server, reverse proxy, load balancer, etc.
- Databases on which your website is dependent.

The server computer could be located on your premises and connected to the Internet by a fast link, but it is far more common to use a computer that is hosted "in the cloud". What this actually means is that your code is run on some remote computer (or possibly a "virtual" computer) in your hosting company's data center(s). The remote server will usually offer some guaranteed level of computing resources (e.g. CPU, RAM, storage memory, etc.) and Internet connectivity for a certain price.

This sort of remotely accessible computing/networking hardware is referred to as Infrastructure as a Service (IaaS). Many IaaS vendors provide options to preinstall a particular operating system, onto which you must install the other components of your production environment. Other vendors allow you to select more fully-featured environments, perhaps including a complete Node setup.

Other hosting providers support Express as part of a Platform as a Service (PaaS) offering. When using this sort of hosting you don't need to worry about most of your production environment (servers, load balancers, etc.) as the host platform takes care of those for you. That makes deployment quite easy because you just need to concentrate on your web application and not any other server infrastructure.

Some developers will choose the increased flexibility provided by IaaS over PaaS, while others will appreciate the reduced maintenance overhead and easier scaling of PaaS. When you're getting started, setting up your website on a PaaS system is much easier.

## Choosing a hosting provider

There are numerous hosting providers that are known to either actively support or work well with Node (and Express). These vendors provide different types of environments (IaaS, PaaS), and different levels of computing and network resources at different prices.

Few popular options are:

- Amazon Web Services (EC2)
- DigitalOcean
- Heroku
- Linode

## Creating and starting the server

After picking a provider, we need to pick an operating system for our cloud computer and other specifications like Ram. Most servers run Linux and it is a great choice for developing Node.js, Windows servers are only really useful for specialized applications such as .NET. For the basic things there isn’t much difference between the Linux images. You can go with Ubuntu Server because it is widely used and has tonnes of guides and plenty of questions and answers on the internet.

An image is an exact copy of a hard drive that can be easily loaded onto an empty hard drive, in this case they are being used as presets to get your machine setup easily. Without at least an operating system and SSH, it wouldn’t be possible to even configure the server so some preset software is necessary.

Serving HTTP traffic on the standard port, 80, try to paste this URL into a URL bar in a new tab.

http://imgur.com:80/

You will notice the 80 gets dropped in the URL bar. That’s because port 80 is the default port for HTTP traffic.

HTTPS traffic uses port 443. Try Hacker News.
https://news.ycombinator.com:443/

Because these ports are often public, you need special privileges to run processes using them. Also, it is not great to run Node.js on port 80 or 443 directly because you may want to open up a few different applications on these ports. With a router you will be able to send traffic from port 80 or 443 to any program you wish, depending on the headers of the incoming HTTP request.

## SSH into your server

There are many ways to establish a connection with a remote machine depending on the operating system you are running, the most common is Secure Shell (SSH) fro linux-based machines by using a text-based interface or CLI.

To SSH we need to have a username, an address and a key. The address is available usually in your server provider dashboard, it look something like this `52.214.64.31`. The key is usually provided to as `.pem` file or a string key when you run your server for the first time.
Almost there. By default, connecting to your instance without a username will try to login as root which is generally not allowed. So from your server provider, you can get the username to use when you SSH to your server. for ubuntu the username is by default ubuntu.

To connect, the SSH command should look something like
`ssh USERNAME@[IP FROM PROVIDER]`

## Installing node and system dependencies

Once in an SSH session the first thing to do is get Node.js. NVM (Node Version Manager) is a pretty great way to install Node.js and allows you to easily switch versions if required.

To install NVM just run this command (same as in the NVM installation instructions).

`$ curl -o- https://raw.githubusercontent.com/creationix/nvm/v0.32.1/install.sh | bash`

This command pulls down a script from a remote URL and runs it. But there aren’t any node versions installed! To get the latest version, just

`nvm install <latest version number>`.

To check node is ready to go just echo the version.

`node --version`

## Deploying code into the server

Now after having node installed, our server is ready to run our node app. To get your code, it does't make since to write code on SSH session, for that you can clone your code from github to your server and run it (don't forget, your remote server is just like your local computer but somewhere else).

We need to SSH into the server, generate a SSH private/public key pair and then add it as a deployment key in source control (i.e. Github). Only when the server is allowed access to the remote repo will it be able to clone the code and pull down changes.
SSH into your server and generate the key pair.

`ssh-keygen -t rsa`

Show the contents of the file

`cat ~/.ssh/id_rsa.pub`

Select the key’s contents and copy it into Github. Deploy keys are added in a section called Deploy keys in the settings for your repo. Paste your key and call it something meaningful.

Whenever you are logged in over SSH, you want the keys to be added so that they are used to authenticate with Github. To do this, add these lines to the top of your ~/.bashrc file.

<code>
# Start the SSH agent <br>
eval `ssh-agent -s` <br>
# Add the SSH key <br>
ssh-add
</code>

This will make sure you use the keys whenever you log on to the server. To run the code without logging out, execute the .bashrc file

`source ~/.bashrc`

Now we can clone the repo!

<code>
You should use your own git URL. <br>
git clone git@github.com:roberttod/tutorial-pt-2.git
</code>

## Keeping the Node.js process running

It’s quite tedious using ctrl+z to pause a process, and then running it in the background. Also, doing it this way will not allow the Node.js process to restart when you restart your server after an update or crash.

To keep these processes running we are going to use a great NPM package called PM2. While in an SSH session, install PM2 globally.

`npm i -g pm2`

To start your server, simply use pm2 to execute index.js.

`pm2 start index.js`

To make sure that your PM2 restarts when your server restarts

`pm2 startup`

This will print out a line of code you need to run depending on the server you are using. Run the code it outputs.
Finally, save the current running processes so they are run when PM2 restarts.

`pm2 save`

Great! Check out the [PM2 docs](https://pm2.keymetrics.io/) to see what else you can do with process management, like using PM2 in order for us to do the git cloning on the server for us.

## Deploying on PaaS

As we mentioned earlier, There are many platforms out there that enables you to deploy your node app with only few clicks without the need to setup everything manually by yourself.
These are more popular now days for small projects and way quicker than the cloud server approach. you can simply upload your code and the platform (eg. [aws elastic beanstalk](https://aws.amazon.com/getting-started/hands-on/deploy-nodejs-web-app/)) automatically handles the deployment, from capacity provisioning, load balancing, auto-scaling to application health monitoring.

---

## References

- https://developer.mozilla.org/en-US/docs/Learn/Server-side/Express_Nodejs/deployment
- https://hackernoon.com/tutorial-creating-and-managing-a-node-js-server-on-aws-part-1-d67367ac5171
- https://phoenixnap.com/kb/ssh-to-connect-to-remote-server-linux-or-windows
- https://medium.com/hackernoon/tutorial-creating-and-managing-a-node-js-server-on-aws-part-2-5fbdea95f8a1#.mnlkymeti
- https://www.bezkoder.com/deploy-node-js-app-heroku-cleardb-mysql/
- https://www.freecodecamp.org/news/lessons-learned-from-deploying-my-first-full-stack-web-application-34f94ec0a286/

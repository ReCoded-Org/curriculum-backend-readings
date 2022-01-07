# Cloud Providers

Now that you are familiar with cloud machines and how to deploy your applications, it is time to get familiar with the different cloud providers in the market currently. PS, they are plenty!

Cloud vendors mostly have the same offering when it comes to computing power. Their machines are marketed usually as secure and resizable that can support any workload.

Cloud computers come with broad selection and customization for processors (number of vCPUs), memory, storage, networking, operating system, and pricing model. Vendors also offer GPU-enabled machines to be used for machine learning applications.

You can run Linux, Windows, and macOS (currently AWS only) on these machines with Intel, AMD, or ARM-based processors. The machines can be shared (multi-tenant) or dedicated/bare-metal (single-tenant). And can be run on-demand. Shared tenancy means that multiple compute instances from different users may exist on the same piece of physical hardware. The dedicated model means that your compute instances will only run on hardware with other instances that you've deployed, no other customers will use the same piece of hardware as you.

For most web servers use cases, shared, on-demand machines are a good bargain. You define your machine size and the image that would be running on your instance. Then start the machine. You will be charged an hourly rate under the on-demand pricing model.

Some vendors also offer Spot instances, which are a cost-effective choice (up to 90% cheaper) if you can be flexible about when your applications run and if your applications can be interrupted. For example, Spot Instances are well-suited for data analysis, batch jobs, background processing, and optional tasks. Their price is usually floating and when it becomes more expensive than your bid (threshold), they get terminated and released back to the cloud.

Below is a list of some cloud vendors that you can explore on your own. They are mostly similar in their offerings and pricing for raw computing power, however, each offers versatile solutions for different use cases.

- Amazon Web Services (AWS)
- Google Cloud Platform (GCP)
- Microsoft Azure
- DigitalOcean
- Oracle Cloud
- Linode
- Alibaba Cloud
- IBM Cloud
- Salesforce Cloud

In the next lesson, we will cover AWS and some of its services that can be used to host backend web applications.

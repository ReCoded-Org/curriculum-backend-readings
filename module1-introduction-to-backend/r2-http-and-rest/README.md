# HTTP and REST

So what exactly happens when you enter a URL starting with http:// or https:// on your browser? How do the client and server communicate? The objectives of this lesson are:
1. Understanding HTTP communication
2. Understanding the request-response lifecycle
3. Understanding REST APIs

## What is HTTP?
HTTP stands for Hypertext Transfer Protocol and is used to structure requests and responses over the internet. The transfer of resources happens using TCP(Transmission Control Protocol). TCP is used to manage many types of internet connections in which one computer or device wants to send something to another. HTTP is the command language that the devices on both sides of the connection must follow in order to communicate.

Imagine two people on two sides of a river trying to send goods across to each other. TCP is the bridge they build while HTTP is the language they use to communicate.

### HTTP & TCP: How it Works
When you type a web address such as www.re-coded.com in your browser, here is what happens:
1. You enter the URL(Uniform Resource Locator) in the browser.
2. The browser looks for the IP address of the domain name in the DNS(Domain Name Server).
3. The browser initiates a TCP connection with the server.
4. The browser sends an HTTP request to the server.
5. The server handles the incoming request and sends an HTTP response.
6. The browser displays the HTML content.

All these steps happen each time we enter any URL and they happen in the background within milliseconds.

Suppose you want to check out the upcoming coding bootcamps at http://www.re-coded.com. After you type the URL into your browser, your browser will extract the http part and recognize that it is the name of the network protocol to use. Then, it takes the domain name from the URL, in this case “re-coded.com”, and asks the Domain Name Server (DNS) to return an Internet Protocol (IP) address. Once the client knows the destination’s IP address, it then opens a connection to the server at that address, using the http protocol as specified. It will initiate a GET request to the server which contains the IP address of the host and optionally a data payload. The GET request contains the following text:
```
GET / HTTP/1.1
Host: www.re-coded.com
```
This identifies the type of request "GET", the path on www.re-coded.com (in this case, “/“) and the protocol “HTTP/1.1.” It could also be "HTTP/2.0". These are latest revisions of the original HTTP.

If the server is able to locate the path requested, the server might respond with the header:
```
HTTP/1.1 200 OK
Content-Type: text/html
```
This header is followed by the content requested, which in this case is the information needed to render www.re-coded.com.

The first line of the header, HTTP/1.1 200 OK, is confirmation that the server understands the protocol that the client wants to communicate with (HTTP/1.1), and an HTTP status code signifying that the resource was found on the server. The second line, Content-Type: text/html, shows the type of content that it will be sending to the client.

If the server is not able to locate the path requested by the client, it will respond with the header:
```
HTTP/1.1 404 NOT FOUND
```
In this case, the server identifies that it understands the HTTP protocol, but the 404 NOT FOUND status code signifies that the specific piece of content requested was not found. This might happen if the content was moved or if you typed in the URL path incorrectly or if the page was removed.

You can also try to explore this on your browser. If you're using Google Chrome, open a new tab, right click and select "Inspect". This opens up the developer console of the browser. From the top menu on this console, select "Network". Now type https://www.re-coded.com/ in your browser bar and hit Enter. You will see a bunch of requests processed in the Network tab as the website loads. If you navigate to the top most request, you should be able to see the request and response headers we just talked about.<br/><br/><img src="https://drive.google.com/uc?export=view&id=1SJPdV6-75u8iTr5xrlMGGb5IgGeH9nn9"><br/><br/>

### What is HTTPS?
Since your HTTP request can be read by anyone at certain network junctures, it might not be a good idea to deliver information such as your credit card or password using this protocol. Fortunately, many servers support HTTPS, short for HTTP Secure, which allows you to encrypt data that you send and receive.

HTTPS is important to use when passing sensitive or personal information to and from websites. However, it is up to the businesses maintaining the servers to set it up. In order to support HTTPS, the business must apply for a certificate from a Certificate Authority. The certificate has a validity period and must be renewed from time-to-time to keep the secure services running.

### What is an API?
API stands for application programming interface, which is a set of definitions and protocols for building and integrating application software. APIs let your product or service communicate with other products and services without having to know how they’re implemented. APIs are sometimes thought of as contracts, with documentation that represents an agreement between parties: If party 1 sends a remote request structured a particular way, this is how party 2’s software will respond.

When you are developing a server, you will be developing an API that enables the frontend to communicate with your server without necessarily knowing the implementation details on your server. The most popular API architecture is the REST API.

## What is REST?
REST, or REpresentational State Transfer, is an architectural style for providing standards between computer systems on the web, making it easier for systems to communicate with each other. REST-compliant systems, often called RESTful systems, are characterized by how they are stateless and separate the concerns of client and server. It means when a RESTful API is called, the server will transfer to the client a representation of the state of the requested resource.

### Guiding Principles of REST
1. **Client–server** – By separating the user interface concerns from the data storage concerns, we improve the portability of the user interface across multiple platforms and improve scalability by simplifying the server components.
2. **Stateless** – Each request from client to server must contain all of the information necessary to understand the request, and cannot take advantage of any stored context on the server. Session state is therefore kept entirely on the client.
3. **Cacheable** – Cache constraints require that the data within a response to a request be implicitly or explicitly labeled as cacheable or non-cacheable. If a response is cacheable, then a client cache is given the right to reuse that response data for later, equivalent requests.
4. **Uniform interface** – By applying the software engineering principle of generality to the component interface, the overall system architecture is simplified and the visibility of interactions is improved. In order to obtain a uniform interface, multiple architectural constraints are needed to guide the behavior of components. REST is defined by four interface constraints: identification of resources; manipulation of resources through representations; self-descriptive messages; and, hypermedia as the engine of application state.
5. **Layered system** – The layered system style allows an architecture to be composed of hierarchical layers by constraining component behavior such that each component cannot “see” beyond the immediate layer with which they are interacting.
6. **Code on demand (optional)** – REST allows client functionality to be extended by downloading and executing code in the form of applets or scripts. This simplifies clients by reducing the number of features required to be pre-implemented.

### Resource
The key abstraction of information in REST is a resource. Any information that can be named can be a resource: a document or image, a temporal service, a collection of other resources, a non-virtual object (e.g. a person), and so on. REST uses a resource identifier to identify the particular resource involved in an interaction between components.

### Making Requests
REST requires that a client make a request to the server in order to retrieve or modify data on the server. A request generally consists of:
- an HTTP verb, which defines what kind of operation to perform
- a header, which allows the client to pass along information about the request
- a path to a resource
- an optional message body containing data

#### HTTP Verbs
There are 4 basic HTTP verbs we use in requests to interact with resources in a REST system:
- **GET** — retrieve a specific resource or a collection of resources
- **POST** — create a new resource
- **PUT** — update a specific resource
- **DELETE** — remove a specific resource

### REST and HTTP are not same!
A lot of people tend to compare HTTP with REST but REST and HTTP are not same. Roy Fielding who presented REST for the first time in 2000 in his famous dissertation did not mention any implementation directive – including any protocol preference and HTTP. REST intends to make the web (internet) more streamline and standard, but as long as you are honoring the 6 guiding principles of REST, you can call any interface RESTful.

In simplest words, in the REST architectural style, data and functionality are considered resources and are accessed using Uniform Resource Identifiers (URIs). The resources are acted upon by using a set of simple, well-defined operations. The clients and servers exchange representations of resources by using a standardized interface and protocol – typically HTTP.

----
## References
- https://www.codecademy.com/articles/http-requests
- https://afteracademy.com/blog/what-happens-when-you-type-a-url-in-the-web-browser
- https://medium.com/extend/what-is-rest-a-simple-explanation-for-beginners-part-1-introduction-b4a072f8740f
- https://www.redhat.com/en/topics/api/what-is-a-rest-api
- https://www.redhat.com/en/topics/api/what-are-application-programming-interfaces
- https://www.codecademy.com/articles/what-is-rest
- https://restfulapi.net/
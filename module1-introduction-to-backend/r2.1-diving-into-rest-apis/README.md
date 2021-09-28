# Diving into REST APIs
HTTP messages are how data is exchanged between a server and a client. There are two types of messages: requests sent by the client to trigger an action on the server, and responses, the answer from the server. The learning objectives of this lesson are:
1. Understanding HTTP request types
2. Understanding HTTP request and response structure
3. Understanding HTTP response status codes

## HTTP Requests
In the previous lesson, we briefly talked about GET, POST, PUT and DELETE request methods.

HTTP defines a set of request methods to indicate the desired action to be performed for a given resource. This set includes:
- **GET**: Requests a representation of the specified resource. Requests using GET should only retrieve data.
- **HEAD**: Asks for a response identical to that of a GET request, but without the response body.
- **POST**: Used to submit an entity to the specified resource, often causing a change in state or side effects on the server.
- **PUT**: Replaces all current representations of the target resource with the request payload.
- **DELETE**: Requests to delete the specified resource.
- **CONNECT**: Establishes a tunnel to the server identified by the target resource.
- **OPTIONS**: Used to describe the communication options for the target resource.
- **TRACE**: Performs a message loop-back test along the path to the target resource.
- **PATCH**: Used to apply partial modifications to a resource.

While developing APIs, GET and POST are the most commonly and frequently used methods.

## Structure of a HTTP Request

HTTP requests, and responses, share similar structure and are composed of:
1. A start-line describing the requests to be implemented, or its status of whether successful or a failure. This start-line is always a single line.
2. An optional set of HTTP headers specifying the request, or describing the body included in the message.
3. A blank line indicating all meta-information for the request has been sent.
4. An optional body containing data associated with the request (like content of an HTML form), or the document associated with a response. The presence of the body and its size is specified by the start-line and HTTP headers.

### Start line
HTTP requests are messages sent by the client to initiate an action on the server. Their start-line contain three elements:
1. An **HTTP method**, a verb (like GET, PUT or POST) or a noun (like HEAD or OPTIONS), that describes the action to be performed. For example, GET indicates that a resource should be fetched or POST means that data is pushed to the server.
2. The **HTTP version**, which defines the structure of the remaining message, acting as an indicator of the expected version to use for the response.
3. The **request target**, usually a URL, or the absolute path of the protocol, port, and domain are usually characterized by the request context. The format of this request target varies between different HTTP methods. It can be
- An absolute path, ultimately followed by a '?' and query string. This is the most common form, known as the origin form, and is used with GET, POST, HEAD, and OPTIONS methods.
```
POST / HTTP/1.1 GET /background.png HTTP/1.0 HEAD /test.html?query=alibaba HTTP/1.1 OPTIONS /anypage.html HTTP/1.0
```
- A complete URL, known as the absolute form, is mostly used with GET when connected to a proxy. 
```
GET https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages HTTP/1.1
```
- The authority component of a URL, consisting of the domain name and optionally the port (prefixed by a ':'), is called the authority form. It is only used with CONNECT when setting up an HTTP tunnel.
```
CONNECT developer.mozilla.org:80 HTTP/1.1
```
- The asterisk form, a simple asterisk ('*') is used with OPTIONS, representing the server as a whole.
```
OPTIONS * HTTP/1.1
```

### Headers
HTTP headers from a request follow the same basic structure of an HTTP header: a case-insensitive string followed by a colon (':') and a value whose structure depends upon the header. The whole header, including the value, consist of one single line, which can be quite long.

Many different headers can appear in requests. They can be divided in several groups:
- General headers, like Via, apply to the message as a whole.
- Request headers, like User-Agent or Accept, modify the request by specifying it further (like Accept-Language), by giving context (like Referer), or by conditionally restricting it (like If-None).
- Representation headers like Content-Type that describe the original format of the message data and any encoding applied (only present if the message has a body).<br/><br/><img src="https://drive.google.com/uc?export=view&id=1kM2zFsDEUS6ZfHWsfMqN8LCvjM_23Fs0"><br/><br/>

### Body
The final part of the request is its body. Not all requests have one: requests fetching resources, like GET, HEAD, DELETE, or OPTIONS, usually don't need one. Some requests send data to the server in order to update it: as often the case with POST requests (containing HTML form data).

Bodies can be broadly divided into two categories:
- Single-resource bodies, consisting of one single file, defined by the two headers: Content-Type and Content-Length.
- Multiple-resource bodies, consisting of a multipart body, each containing a different bit of information. This is typically associated with HTML Forms.

## Structure of a HTTP Response

The structure is similar to HTTP Requests.

### Status line
The start line of an HTTP response, called the status line, contains the following information:
1. The protocol version, usually HTTP/1.1.
2. A status code, indicating success or failure of the request. Common status codes are 200, 404, or 302
3. A status text. A brief, purely informational, textual description of the status code to help a human understand the HTTP message.

### Headers
HTTP headers for responses follow the same structure as any other header: a case-insensitive string followed by a colon (':') and a value whose structure depends upon the type of the header. The whole header, including its value, presents as a single line.

Many different headers can appear in responses. These can be divided into several groups:
- General headers, like Via, apply to the whole message.
- Response headers, like Vary and Accept-Ranges, give additional information about the server which doesn't fit in the status line.
- Representation headers like Content-Type that describe the original format of the message data and any encoding applied (only present if the message has a body).

### Body
The last part of a response is the body. Not all responses have one: responses with a status code that sufficiently answers the request without the need for corresponding payload (like 201 Created or 204 No Content) usually don't.

Bodies can be broadly divided into three categories:
- Single-resource bodies, consisting of a single file of known length, defined by the two headers: Content-Type and Content-Length.
- Single-resource bodies, consisting of a single file of unknown length, encoded by chunks with Transfer-Encoding set to chunked.
- Multiple-resource bodies, consisting of a multipart body, each containing a different section of information. These are relatively rare.

## HTTP response status codes
HTTP response status codes indicate whether a specific HTTP request has been successfully completed. Responses are grouped in five classes:
- Informational responses (100–199)
- Successful responses (200–299)
- Redirects (300–399)
- Client errors (400–499)
- Server errors (500–599)

You can read more about each status code [here](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status).

The most commonly used status codes are:
- Status Code 200 OK – This is the standard "OK" status code for a successful HTTP request. The response that is returned is dependent on the request. For example, for a GET request, the response will be included in the message body. For a PUT/POST request, the response will include the resource that contains the result of the action.
- Status Code 201 Created – This is the status code that confirms that the request was successful and, as a result, a new resource was created. Typically, this is the status code that is sent after a POST/PUT request.
- Status Code 204 No Content – This status code confirms that the server has fulfilled the request but does not need to return information. Examples of this status code include delete requests or if a request was sent via a form and the response should not cause the form to be refreshed or for a new page to load.
- Status Code 304 Not Modified – This status code used for browser caching. If the response has not been modified, the client/user can continue to use the same response/cached version. For example, a browser can request if a resource has been modified since a specific time. If it hasn’t, the status code 304 is sent. If it has been modified, a status code 200 is sent, along with the resource.
- Status Code 400 Bad Request – The server cannot understand and process a request due to a client error. Missing data, domain validation, and invalid formatting are some examples that cause the status code 400 to be sent.
- Status Code 401 Unauthorized – This status code request occurs when authentication is required but has failed or not been provided.
- Status Code 403 Forbidden – Very similar to status code 401, a status code 403 happens when a valid request was sent, but the server refuses to accept it. This happens if a client/user requires the necessary permission or they may need an account to access the resource. Unlike a status code 401, authentication will not apply here.
- Status Code 404 Not Found – The most common status code the average user will see. A status code 404 occurs when the request is valid, but the resource cannot be found on the server. Even though these are grouped in the Client Errors "bucket," they are often due to improper URL redirection.
- Status Code 409 Conflict – A status code 409 is sent when a request conflicts with the current state of the resource. This is usually an issue with simultaneous updates, or versions, that conflict with one another.
- Status Code 410 Gone – Resource requested is no longer available and will not be available again. Clients are expected to remove their caches and links to the resource.
- Status Code 500 Internal Server Error – Another one of the more commonly seen status codes by users, the 500 series codes are similar to the 400 series codes in that they are true error codes. The status code 500 happens when the server cannot fulfill a request due to an unexpected issue. Web developers typically have to comb through the server logs to determine where the exact issue is coming from.

---
## References
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Messages
- https://developer.mozilla.org/en-US/docs/Web/HTTP/Status
- https://www.dotcom-monitor.com/blog/2019/10/03/the-10-most-common-http-status-codes/

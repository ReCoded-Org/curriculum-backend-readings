# Introduction to Backend
Welcome to your first lesson of the Backend Web Development Bootcamp! The objectives of this lesson are:
1. To understand the roles of frontend developer vs backend developer vs fullstack developer
2. To get familar with the basics of backend web architecture

Here we go!

## Frontend Developer vs Backend Developer vs Fullstack Developer
As of June 2021, it is estimated that the Internet contains more than 1.8 million websites. No doubt that this a great time to start a career as a web developer, the people who are responsible for coding, building, analyzing, and maintaining all those websites.

If you have some experience with web development or have been reading about it, then you already know that web development tends to break down into three main concentrations: frontend, backend, and fullstack.

### What is a Frontend Developer?
The frontend of a website is the visible part that users interact with. It is also called the User Interface (UI). Everything that you see when you’re navigating around the Internet, from text, fonts and colors to buttons, dropdown menus,and sliders, is a combination of HTML, CSS, and JavaScript being rendered and controlled by your computer’s browser.

A frontend developer is responsible for writing and maintaining the code for the user interface of the website and the architecture and functionality for the user experience of the website. Frontend developers must be competent in HTML, CSS and Javascript as their foundation along with one or more modern frameworks like ReactJS, AngularJS, VueJS, EmberJS, BackboneJS, Foundation or Svelte. They also work with UI libraries like Sass, Bootstrap, Tailwind, React Bootstrap, Material UI, Ant Design and Semantic UI and tools like Babel, Webpack, Gatsby.

Frontend developers are sometimes seen as a combination of a user interface designer, user experience designer and software developer – someone who appreciates the aesthetic, usability as well as functionality of an application. They care about delivering the features and functionalities, but they also go the extra mile to ensure the user interface is aesthetically pleasing and the experience is seamless. A great frontend developer is not only proficient in programming but also good at empathising with the end users.<br/><br/><img src="https://drive.google.com/uc?export=view&id=1EiN2DOjCpmS05ZLyrT73kVhM34Ne0S5-"><br/><br/>

### What is a Backend Developer?
But where does all the data to be displayed on the frontend come from? How is a website personalized for the logged in user? This is where the backend comes in. The backend of a website consists of a server, an application, and a database.

A backend developer builds and maintains the code that powers those components which together enable the user-facing side of the website to even exist in the first place. Backend developers must be competent with one or more server-side languages such as NodeJS, Ruby, Python, PHP or Java, frameworks like ExpressJS, Ruby on Rails, Python Django and databases like MySQL, PostgreSQL or MongoDB. They are also familiar with Linux as a deployment environment and DevOps tools like AWS, GCP, Apache, Nginx, Docker and Kubernetes.

Backend developers need to be able to navigate across larger codebases and not get lost in the complexities of what may seem like programming labyrinths. They also need to be very meticulous when making changes to not "break" anything as there are usually delicate dependencies. Finally, unlike frontend development where the written code translates directly to visual output one can see and interact with, backend development of business logic is often hard to visualise. Therefore to be a good backend developer, you need to be comfortable with dealing with abstracts.<br/><br/><img src="https://drive.google.com/uc?export=view&id=1PkIrF_pNnGbX1NiW-q1JIKokql1v4FI7"><br/><br/>

### What is a Fullstack Developer?
A jack of all trades? Pretty much! Often there isn't a black-and-white distinction between frontend and backend development. Frontend developers sometimes need to understand backend concepts like how REST APIs work and backend developers sometimes need to understand how components are rendered with data in their state.

The role of a fullstack developer was popularized by Facebook’s engineering department. The idea is that a fullstack developer can work cross-functionally on the full "stack" of technology, both the frontend and backend. They are capable of performing both frontend and backend tasks and have a complete understanding of how a web application works, and how the "front" and the "back" are connected. They can build a complete web application on their own. In the current digital economy, companies are looking for such cross-discipline developers or generalists.

To be a good fullstack developer, you need to be comfortable with dealing with abstracts as well as empathising with end users. Good fullstack developers also need to know when to wear which hat to work effectively and efficiently because there will always be division of responsibilities.<br/><br/><img src="https://drive.google.com/uc?export=view&id=13hdTlUW0tk0J91wV-r7ruPX7uATpt9pe"><br/><br/>

## Backend web architecture
Let's start diving deeper into what do we mean when we say frontend and backend. The frontend is the code that is executed on the client side. This code runs in the user’s browser and creates the user interface. The backend is the code that runs on the server, receives requests from the clients, and contains the logic to send the appropriate data back to the client. The backend also includes the database, which will persistently store all of the data for the application.

### What are clients?
The clients are entities that send requests to the backend. They are often browsers that make requests for the HTML and JavaScript code that they will execute to display websites to the end user. However, there are many different kinds of clients: they might be a mobile application, an application running on another server, or even a web enabled smart appliance.

### What is a backend?
The backend is all of the technology required to process the incoming request and generate and send the response to the client. This typically includes three major parts:
- The server. This is the computer that receives requests.
- The app. This is the application running on the server that listens for requests, retrieves information from the database, and sends a response.
- The database. Databases are used to organize and persist data.

### What is a server?
A server is simply a computer that listens for incoming requests. Though there are machines made and optimized for this particular purpose, any computer that is connected to a network can act as a server. In fact, you will often use your very own computer as server when developing apps.

### What kinds of responses can a server send?
The data that the server sends back can come in different forms. For example, a server might serve up an HTML file, send data as JSON, or it might send back only an HTTP status code. You’ve probably seen the status code "404 - Not Found" whenever you’ve tried navigating to a URI that doesn’t exist, but there are many more status codes that indicate what happened when the server received the request.

> Okay I want to see some code now!

We heard you. In the next lesson, we will learn about Node.js which will be the primary server-side programming framework that we will be using throughout this bootcamp.

---
## References
- https://www.freecodecamp.org/news/front-end-developer-vs-back-end-developer-definition-and-meaning-in-practice
- https://www.udacity.com/blog/2020/12/front-end-vs-back-end-vs-full-stack-web-developers.html
- https://sg.alphacamp.co/2018/07/31/what-kind-of-web-developer-should-you-be/
- https://www.codecademy.com/articles/back-end-architecture
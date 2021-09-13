# Backend Curriculum Readings
This serves as a content monorepo for all the readings of the backend bootcamp curriculum developed by Re:Coded. Content from this repo will be transferred to the course on Canvas LMS. Each markdown file inside the module folders and sub-folders corresponds to a reading on the LMS.

## Folder Structure
```
.
│   README.md                       // We are here   
│
└───module1-introduction-to-backend
|   └───assets                      // common assets folder for module
│   └───r1-introduction-to-backend
|       | README.md                 // reading content goes here
│   └───r1.1-beginners-guide-nodejs-npm
|       | README.md
|   └───r2-http-and-rest
|       | README.md
|   └───r2.1-diving-into-rest-apis
|       | README.md
|   └───...                         // and so on
|
└───module2-database-technologies
|   └───assets                      // common assets folder for module
│   └───r1-introduction-to-databases
|       | README.md                 // reading content goes here
│   └───r2-introduction-to-relational-databases
|       | README.md
|   └───r2.1-relational-database-structure
|       | README.md
|   └───...                         // and so on
|
└───...                             // and so on
```

## Folder Naming Conventions

- For every new reading, name the folder as: `r[number]-name-of-reading`. For example, `r1-introduction-to-backend` or `r2.1-relational-database-structure`.
- Use your discretion to shorten certain folder names if required while maintaining the same meaning. For example, the folder for "Beginners guide to Node.js and NPM" can be named as `r1.1-beginners-guide-nodejs-npm`.

## Reading Format

- Each reading should begin with the title as an h1.
- Below the title it should have the summary and learning goals.
- After this goes in the main content of the reading.
- Finally each reading should conclude with a section called References, where we can link the external blogs/tutorials/videos we referred to.

## General Formatting Conventions

- Use proper header hierarchy (h1 # to h6 ######) to convey the flow of topics and sub-topics.
- Use code and syntax highlighting for code blocks and referring variable/function names.
- Use tables and lists for non-code content blocks.
- Always share links through inline links. For example, check out [this markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is preferred over check out this markdown cheatsheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet 
- Make sure to run your content through [Grammarly](https://www.grammarly.com/) to get rid of typos and grammatical errors.


## Peer Review Process
- Work on a module or reading on it's own branch and open a PR into main branch.
- Request at least 2 reviewers on your PRs.
- Open draft PRs early for large modules to get continuous peer reviews. This helps your peers know that the PR is still WIP and is also helpful to review the content in chunks.

## Example

`Start with a H1 for the title`👇
# Beginners guide to Node.js and NPM
`Enter a quick summary and numbered list of learning objectives`👇<br/>
We will be working in the Node.js and NPM environment throughout this bootcamp. The objectives of this lesson are:
1. Understanding the Node.js framework
2. Advantages of Node.js and why this course is focussed on Node.js

`Detail out first sub-topic under a H2`👇
## Introduction to Node.js
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

`Detail out further sections with H3 inside the sub-topic`👇
### Features of Node.js
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.
1. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.
2. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.
3. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

`Detail out next sub-topic under a H2`👇
## Why are we teaching Node.js in this bootcamp?
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.

`Use the end space of last section for a quick outro or recap of the reading.`👇<br/>
Now that you have enough context on Node.js, let's prepare our coding environments on our computers. Coming up next is your first assignment of this course which will walk you through setting up your Node.js environment.

`End with a horizontal rule and list References under an H2`👇

---
## References
- https://www.freecodecamp.org/news/what-is-npm-a-node-package-manager-tutorial-for-beginners/
- https://nodejs.dev/learn/introduction-to-nodejs
- https://medium.com/jspoint/how-javascript-works-in-browser-and-node-ab7d0d09ac2f
- https://www.geeksforgeeks.org/top-8-reasons-to-learn-nodejs-in-2020/
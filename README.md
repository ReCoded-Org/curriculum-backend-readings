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

## Folder naming Conventions

- For every new reading, name the folder as: `r[number]-name-of-reading`. For example, `r1-introduction-to-backend` or `r2.1-relational-database-structure`.
- Use your discretion to shorten certain folder names if required while maintaining the same meaning. For example, the folder for "Beginners guide to Node.js and NPM" can be named as `r1.1-beginners-guide-nodejs-npm`.

## Reading format

- Each reading should begin with the title as an h1.
- Below the title it should have the summary and learning goals.
- After this goes in the main content of the reading.
- Finally each reading should conclude with a section called Resources, where we can link the external blogs/tutorials/videos we referred to.

## General formatting Conventions

- Use proper header hierarchy (h1 # to h6 ######) to convey the flow of topics and sub-topics.
- Use code and syntax highlighting for code blocks and referring variable/function names.
- Use tables and lists for non-code content blocks.
- Always share links through inline links. For example, check out [this markdown cheatsheet](https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet) is preferred over check out this markdown cheatsheet: https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet 


## Peer review process
- Work on a module or reading on it's own branch and open a PR into main branch.
- Request at least 2 reviewers on your PRs.
- Open draft PRs early for large modules to get continuous peer reviews. This helps your peers know that the PR is still WIP and is also helpful to review the content in chunks.
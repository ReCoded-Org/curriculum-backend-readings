# CI/CD

Have you heard of the terms Continuous Integration and Continuous Delivery before? Specially in the context of automated testing and it's use in DevOps. The objectives of this lesson are:
1. To understand the role of automated testing in CI/CD
2. Get familiar with few methodologies for implementing CI/CD checks

## What is CI/CD?
CI/CD is a method to frequently deliver apps to customers by introducing automation into the stages of app development. The main concepts attributed to CI/CD are continuous integration, continuous delivery, and continuous deployment. CI/CD is a solution to the problems integrating new code can cause for development and operations teams (AKA "integration hell").

Specifically, CI/CD introduces ongoing automation and continuous monitoring throughout the lifecycle of apps, from integration and testing phases to delivery and deployment. Taken together, these connected practices are often referred to as a "CI/CD pipeline" and are supported by development and operations teams working together in an agile way with either a DevOps or site reliability engineering (SRE) approach.

We will be learning about CI/CD in little bit more detail in one of the upcoming modules on Cloud Computing. In this module, we will focus on deploying automated tests during continuous integration.

So far we have seen how we can run tests and static analysis while working on our code. However, in what we have learned so far there is a huge dependency of each developer to run `npm test` and `npm run lint` and `npm run format` on their local machine before pushing the code to a shared remote repository. What if a developer forgets to execute these steps? Or what if a new team member unaware of these practices ends up pushing code without executing these checks?

Are you thinking what we are thinking? "Let's automate this!"
Yup, one main approach in continuous integration is to automate the execution of tests before integrating the new incoming code changes.

## Husky

[Husky](https://www.npmjs.com/package/husky) is a popular tool used to enforce running checks on each devloper's local machines. It works with the concepts of Git hooks. Basically Husky can execute commands automatically in relation to git commands. So let's say, we want to ensure that no developer can commit any code that is not validated. We can configure Husky to run `npm run validate` on the pre-commit hook.

All you need to do is add Husky as a dev dependency on your project.
```bash
npm install husky --save-dev
```

And then create a `.huskyrc` file as:
```js
{
    "hooks": {
        "pre-commit": "npm run validate"
    }
}
```

Now whenever a git commit is about to be performed, Husky will first run the validate script (which basically runs lint and format) and proceed or abort the commit depending on the validations.

You can also configure Husky to automatically make formatting corrections and add them to the current commit. Or you can also configure Husky to run your unit tests in a pre-push hook. You can read more about setting up and using Husky in [this article](https://www.freecodecamp.org/news/how-to-add-commit-hooks-to-git-with-husky-to-automate-code-tasks/).

## GitHub Actions

[GitHub Actions](https://github.com/features/actions) is an awesome tool used to automate CI/CD workflows on GitHub repositories. It has many many different possibilities, but when it comes to testing it is very useful to automate the running of unit tests on a new pull request.

So, consider the scenario where multiple developers are contributing to a shared codebase using a single remote repository on GitHub. Each developer would work on dedicated branches and then open a pull request (PR) into the main branch once they are ready to have their code merged. In order to make sure that the code changes of a PR does not break any existing features, we can use GitHub Actions to automatically run tests and block merging in case any tests fail.

We can setup a workflow for GitHub Actions by adding a `.yml` file in the repository that has all the configuration options for running tests. Take a look at [this example](https://lannonbr.com/blog/2020-03-30-github-actions-ci-tests) in which the workflow runs `npm install` and `npm test` in an Ubuntu environment using Node 12.

You can look at the `.github` folder on any of your previous assignments which had automated tests for submission, and explore the configuration files. You can see the results of these tests on any of your PRs in the tab called "Checks". In fact, if your PR passed the tests on GitHub Actions workflow you will see a green check mark next to the PR title. And for details of the tests execution you can explore the "Checks" tab.

There are many more tools and options for CI/CD which we will learn about soon, but one of the main components is setting up automated tests and now you know how to setup the same using the above tools.
# Cron Jobs

While working on your backend projects, have you ever thought of building regularly repeated operations? Like sending a weekly newsletter email to your subscribers or logging a count of daily new customers. This is where cron jobs come in. The objectives of this lesson are:

1. Familiarizing ourselves with cron jobs
2. Setting up cron jobs in Node.js

## What is a cron job?

Cron is a utility program that lets users input commands for scheduling tasks repeatedly at a specific time. Tasks scheduled in cron are called cron jobs. Users can determine what kind of task they want to automate and when it should be executed. If you're curious about the name, it originated from "Chronos", the Greek word for time.

Cron is a daemon – a background process executing non-interactive jobs. In Windows, you might be familiar with background processes such as Services that work similarly to the cron daemon. A daemon is always idle, waiting for a command to request it to perform a particular task. The command can be entered on any computer on the network but it can be executed only on the computer running the daemon.

A cron file is a simple text file that contains commands to run periodically at a specific time. The default system cron table or `crontab` configuration file is `/etc/crontab`, located within the crontab directory `/etc/cron.*/`.

Only system administrators can edit the system crontab file. However, Unix-like operating systems support multiple admins. Each can create a crontab file and write commands to perform jobs anytime they want. With cron jobs, users can automate system maintenance, disk space monitoring, and schedule backups. Because of their nature, cron jobs are great for computers that work 24/7, such as servers. While cron jobs are used mainly by system administrators, they can be beneficial for web developers too. For instance, as a website administrator, you can set up one cron job to automatically backup your site every day at midnight, another to check for broken links every Monday at midnight, and a third to clear your site cache every Friday at noon.

However, like any other program, cron has limitations you should consider before using it:

1. The shortest interval between jobs is 60 seconds. With cron, you won’t be able to repeat a job every 59 seconds or less.
2. Centralized on one computer. Cron jobs can’t be distributed to multiple computers on a network. So if the computer running cron crashes, the scheduled tasks won’t be executed, and the missed jobs will only be able to be run manually.
3. No auto-retry mechanism. Cron is designed to run at strictly specified times. If a task fails, it won’t run again until the next scheduled time. This makes cron unsuitable for incremental tasks.

With these limitations, cron is an excellent solution for simple tasks that run at a specific time with regular intervals of at least 60 seconds.

## Basic Cron Job Operations

The simplest way to set up cron jobs is by inputting commands into a shell program like Bash on Linux or another Unix-like operating system. Before proceeding with the basic operations of cron, it’s essential to know the different cron job configuration files:

1. The system's `crontab`: Use it to schedule system-wide, essential jobs that can only be changed with root privileges.
2. The user's `crontab`: This file lets users create and edit cron jobs that only apply at the user level.

If you want to edit the system crontab, make sure that the current user has root privileges.

To create or edit a crontab file, enter the following into the command line: `crontab -e`

If no crontab files are found in your system, the command will automatically create a new one. It allows you to add, edit, and delete cron jobs.

You'll need a text editor like vi or nano to edit a crontab file. When entering `crontab -e` for the first time, you'll be asked to choose which text editor you want to edit the file with.

To see a list of active scheduled tasks in your system, enter the following command: `crontab -l`

### Crontab Syntax

To create a cron job, you'll need to understand cron's syntax and formatting first. Otherwise, correctly setting up cron jobs may not be possible. The crontab syntax consists of five fields with the following possible values:

1. **Minute.** The minute of the hour the command will run on, ranging from 0-59.
2. **Hour.** The hour the command will run at, ranging from 0-23 in the 24-hour notation.
3. **Day of the month.** The day of the month the user wants the command to run on, ranging from 1-31.
4. **Month.** The month that the user wants the command to run in, ranging from 1-12, thus representing January-December.
5. **Day of the week.** The day of the week for a command to run on, ranging from 0-6, representing Sunday-Saturday. In some systems, the value 7 represents Sunday.

Don't leave any of the fields blank.

If, for example, you want to set up a cron job to run `root/backup.sh` every Friday at 5:37 pm, here's what your cron command should look like: `37 17 * * 5 root/backup.sh`

In the example above, 37 and 17 represent 5:37 pm. Both asterisks for the Day of the month and Month fields signify all possible values. This means that the task should be repeated no matter the date or the month. Finally, 5 represents Friday. The set of numbers is then followed by the location of the task itself. Usually, the task is a script that performs certain actions.

You can look up more options for cron syntax online, but in most cases, these options should suffice.

## Cron jobs in Node.js

The above method is a classic solution, but with some disadvantages.

1. First of all it's tightly coupled with the server's OS, developers should not have to always worry about the server's environment.
2. Load balancing. For each new cron job, the Linux admin needs to find a server with enough free resources. It can be pretty difficult because cron jobs run on schedule, and the Linux admin has to check historical monitoring data about server load at the scheduled time in the past.
3. Simultaneous execution. If you have only one server, it's not a problem at all. But if you have multiple servers, you need to make sure that the cron job has been deployed on only one server, otherwise, it will be executed simultaneously. Your customer won't be happy to receive two identical emails, because your notifications cron job was deployed twice.

Here's where Node.js libraries for cron scheduling can save the day. Here is an example:

```js
const cron = require("node-cron");

cron.schedule("* * * * *", () => {
  console.log("running a task every minute");
});
```

This script never ends, it acts as a daemon. This solution doesn't depend on infrastructure, it can be run anywhere including Docker. You can also combine several cron jobs in one script and moreover, you can create new cron jobs dynamically in runtime. It's very convenient and flexible, but like in the previous solution, you need to make sure that your app is executed only in one instance.

You can read more about task scheduling with `node-cron` in [this article](https://blog.logrocket.com/task-scheduling-or-cron-jobs-in-node-using-node-cron/). And there are a few more libraries that help with cron scheduling such as [Bull](https://www.npmjs.com/package/bull) which supports task queuing and cron scheduling.

## Conclusion

Cron jobs are very useful for scheduling repeated tasks at a regular interval or specific time. We can use the Linux cron tab or Node.js libraries as per our needs and infrastructure to set up cron jobs.

---

## References

- https://www.hostinger.in/tutorials/cron-job
- https://medium.com/geekculture/cron-jobs-in-node-js-8df170445588
- https://www.geeksforgeeks.org/how-to-run-cron-jobs-in-node-js/

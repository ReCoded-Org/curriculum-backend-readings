# Introduction to Redis

We have mentioned Redis a few times while talking about databases in earlier modules of the curriculum. The objectives of this lesson are:
1. Getting familiar with the Redis database
2. Understanding the popular use cases of Redis
3. Learning to install and use Redis
4. Understanding data structures on Redis

## What is Redis?

[Redis](https://redis.io/), which stands for Remote Dictionary Server, is a fast, open source, in-memory, key-value data store. The project started when Salvatore Sanfilippo, the original developer of Redis, wanted to improve the scalability of his Italian startup. From there, he developed Redis, which is now used as a database, cache, message broker, and queue.

Redis delivers sub-millisecond response times, enabling millions of requests per second for real-time applications in industries like gaming, ad-tech, financial services, healthcare, and IoT. Redis is one of the most popular open source engines today, named the "Most Loved" database by StackOverflow for five consecutive years. Because of its fast performance, Redis is a popular choice for caching, session management, gaming, leaderboards, real-time analytics, geospatial, ride-hailing, chat/messaging, media streaming, and pub/sub apps.

Let's focus on two main characteristics of Redis: "in-memory" and "key-value data store".
1. Redis is a database that gets stored on the random access memory (RAM).
2. Redis is persistent, meaning that even if your system is off, you won't lose data.
3. Redis supports many data types but the default data model is of the key-value. Think hashmaps or associative arrays.

### How is Redis better than any SQL/NoSQL database?

Speed. Yup, that just it, Redis is much faster than your average database.

But why is that? It mainly comes down to where they are being stored.

Redis databases get saved in the random access memory (RAM) which is much faster than its counterpart where it gets saved in non-volatile storage like hard-drives, solid-state-drives, etc.

The downside is that it can't outgrow your usual database, but the bar is pretty high. So it's technically possible to use Redis as your main database. You can read up on comparison of Redis with other databases [here](https://redis.com/ebook/part-1-getting-started/chapter-1-getting-to-know-redis/1-1-what-is-redis/1-1-1-redis-compared-to-other-databases-and-software/).

### When would I want to use Redis?

While Redis seems, all nice and dandy. You most likely can't simply replace your database with it. It's mostly used in caching data. Caching is the mechanism of storing frequently requested data in memory so that it will be faster to fetch and ease the load to the database. But this is not the only use case for Redis. As of 2021, you can use Redis as a:
- Database
- Cache
- Message Broker
- Server for machine/deep learning models

## Testing Redis on your local machine

We will work on a containerized version of Redis, for that we need to make sure we have Docker installed. To install Redis, make sure your docker service is running if not then run this command on Linux.
```bash
sudo systemctl start docker
```

Then let us create a Redis instance.
```bash
docker run --name redis -d redis
```

Here we are basically creating a new docker container called redis using the Redis image take from DockerHub. To make sure your container us up and running, run the command to list all containers:
```bash
docker ps
```

You should redis in the list of running containers.

Moving on, run the command to bash into the Redis docker container.
```bash
docker exec -it redis bash
```

Now you should be inside the docker container.

### Redis CLI

Redis comes bundled in with its command-line interface (CLI) tool called plainly Redis-CLI. To check whether Redis-CLI is working run this command inside the Redis container:
```bash
redis-cli -v
```

You should see the installed version number of Redis. Congratulations you got Redis setup, let us try some commands now.

1. Entering the Redis-CLI: Make sure your Redis server is running, and run the command `redis-cli`

2. Exiting the Redis-CLI: `exit`

3. Setting a key: `SET key value` (For example, `SET name James`)

4. Getting a key: `GET key` (For example, `GET name`)

5. Listing all keys: `KEYS *`

6. Deleting a key: `DEL key` (For example, `DEL name`)

7. Dumping a key: `DUMP key` (For example, `DUMP name`)

8. Check whether a key exists: `EXISTS key` (For example, `EXISTS name`)

9. Set key expiry: `EXPIRE key seconds` (For example, EXPIRE name 20)

10. Get the remaining time in keys expiry in seconds: `TTL key` (For example, TTL name)

## Redis Data Structures

Redis is implemented in C, so naturally, all data structures internally are also implemented in C. Furthermore to allocate memory to these data structures, Redis wraps malloc in something called zmalloc. This allows Redis to select between different alloc libraries. A popular one is jemalloc due to its focus on avoiding fragmentation.

Redis allows us to store keys that map to any one of five different data structure types; STRINGs, LISTs, SETs, HASHes, and ZSETs.

### Strings
Strings are the most basic data type in Redis, they are binary safe, meaning we can store any kind of data, such as a JPEG image or a Ruby object. A String value can be at a maximum of 512 MB. You can read more about the string commands [here](https://redis.io/commands/#string).

### Lists
Lists in Redis are basically a list of strings, sorted by insertion order. You can add items in both ends of the list (head and tail) by using the commands LPUSH and RPUSH. You can read more about list commands [here](https://redis.io/commands#list).

### Sets
Redis sets are unordered collection of strings. The time complexity for insertion and deletion is constant time O(1). Like normal sets, Redis sets only contain unique values, meaning that if you try to put a duplicated value it won't show up in the set. With that in mind, Redis gives us some useful commands to manipulate sets: Union, Intersection and Difference. You can read more about set commands [here](https://redis.io/commands#set).

### Hashes
Redis hashes like normal hashes represent key-value pairs. You usually use hashes to represent objects. Hashes are the most versatile data type out there, so you can represent lots of different elements. You can read more about hash commands [here](https://redis.io/commands#hash).

You can go through [this detailed reading](https://redis.com/ebook/part-1-getting-started/chapter-1-getting-to-know-redis/1-2-what-redis-data-structures-look-like/) for a deeper dive into Redis data structures.

## Popular Use Cases of Redis

Redis data stays in memory, as opposed to traditional kinds of databases that persist to disk. This gives Redis an edge over other kinds of storage systems and makes it ultra fast with high throughput and low latency.

### Session management
Redis comes in handy in managing user sessions at the application level. Typical web applications store user session information about the user login, user IDs, recent user actions, and so on.

### Caching
For data that is frequently needed or retrieved by app users, a cache would serve as a temporary data store for quick and fast retrieval without the need for extra database round trips. Note that data stored in a cache is usually data from an earlier query or copy of data stored somewhere else. This feature is vital because the more data we can fetch from a cache, the faster and more efficiently the system performs overall.

### Chat and Messaging Applications
Redis supports [Pub/Sub model](https://en.wikipedia.org/wiki/Publish%E2%80%93subscribe_pattern) with pattern matching and many different varieties of data structures such as lists, sorted sets, and hashes. This allows Redis to support high-performance chat rooms, real-time comment streams, social media feeds and server intercommunication.

### Gaming leaderboard applications
Redis is a very popular choice among game developers looking to build real-time leaderboards or scoreboards. Redis Sorted Set data structure can be simply used to implement this use case, which provides uniqueness of elements while keeping the list sorted by users' scores(points) associated with the key. We can also use Sorted Sets to handle time-series data by using timestamps as the score for ranking based on timestamps.

### Job Queues
When handling requests from web clients, sometimes operations take more time to execute than we want to spend immediately. We can defer those operations by putting information about our task to be performed inside a queue, which we process later. This method of deferring work to some task processor is called a task queue or job queue.

Other than these use cases, you can read about some specific industry use cases of Redis [here](https://redis.com/blog/5-industry-use-cases-for-redis-developers/) for further learning.

Now that we have learned a little bit about Redis, we will explore some of these use cases and their implementation in the upcoming readings. Finally, we will work on assignment for implementing Redis in our Node applications. 

---

## References
- https://aws.amazon.com/redis/
- https://dev.to/tamerlang/a-beginners-guide-to-redis-1cb1
- https://blog.logrocket.com/guide-to-fully-understanding-redis/
- https://severalnines.com/database-blog/introduction-redis-what-it-what-are-use-cases-etc
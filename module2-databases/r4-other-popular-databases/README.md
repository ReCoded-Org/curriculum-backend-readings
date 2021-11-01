# Other Popular Databases
There are some other popular databases used widely in the industry besides MySQL and MongoDB. The objective of this lesson is to get familiar with these databases.

We briefly mentioned some of these databases when introducing NoSQL databases.

## Key-Value Store
Another way to store non-relational data is in a key-value store. A key-value store is basically a production-scale hashmap: a map from keys to values. There are no fancy schemas or relationships between data. No tables or other logical groups of data of the same type. Just keys and values, that's it.

Popular key-value stores are [Redis](https://redis.io/) and [Memcached](https://memcached.org/). Both are in-memory key-value stores, so their performance is top-notch.

### When to use a Key-Value Store?
Key-value stores are good for simple applications that need to store simple objects temporarily. An obvious example is a cache. A less obvious example is to use Redis lists to queue units of work with simple input parameters.

We will explore Redis in one of the upcoming modules of this course.

## Full-Text Search Engine
Search engines are a special type of data store designed for a very specific use case: searching text-based documents. Technically, search engines are NoSQL data stores. You ship semi-structured document blobs into them, but rather than storing them as-is and using XML or JSON parsers to extract information, the search engine slices and dices the document contents into a new format that is optimized for searching based on substrings of long text fields.

Search engines are persistent, but they"re not designed to be particularly durable. You should never use a search engine as your primary data store! It should be a secondary copy of your data, which can always be recreated from the original source in an emergency.

[Elasticsearch](https://www.elastic.co/) is a popular database that
specializes as a full-text search engine. While relational databases focus on a tabular
format, Elasticsearch can efficiently search through large text files, such as
application logs. The most important feature of any search engine, is that it performs exceptionally well for text searches. MongoDB also has a full-text search engine called [Atlas Search](https://www.mongodb.com/atlas/search) in their DbaaS offering.

### When to use a Full-Text Search Engine
If you have found yourself writing SQL queries with a lot of wildcard matches (for example, `SELECT * FROM products WHERE description LIKE "%cat%"` to find cat-related products) and you"re thinking about brushing up on your natural-language processing skills to improve the results, you might need a search engine!

Search engines are also pretty good at searching and filtering by exact text matches or numeric values, but databases are good at that, too. The real value add of a full-text search engine is when you need to look for particular words or substrings within longer text fields.

We will explore Elasticsearch in the next and final assignment of this module.

## Message Queue
Message queues are considered more of a data transfer tool than a data storage tool, but message queues store your data with as much reliability and even more persistence than some of the other tools we've discussed already!

One of the options for this is [Kafka](https://kafka.apache.org/). Kafka is typically treated as a message queue, but it's technically not a queue. It's more of a distributed log, which means that we can do things like set a data retention time of "forever" and compact our messages by key (which means we only retain the most recent value for each key) and we've basically got a key-value document store! You can read about the use cases of Kafka [here](https://kafka.apache.org/uses).

### When to use a Message Queue
Use a message queue when you need to temporarily store, queue, or ship data.

If the data is very simple and you're just storing it for use later in the same service, you could consider using a key-value store like Redis. You might consider using Kafka for the same simple data if it's very important data, because Kafka is more reliable and persistent than Redis. You might also consider using Kafka for a very large amount of simple data, because Kafka is easier to scale by adding distributed partitions.

Kafka is often used to ship data between services. The producer-consumer model has a big advantage over other solutions: because Kafka itself acts as the message broker, you can simply ship your data into Kafka and then the receiving service can poll for updates.

We won't explore Kafka as it is more clear in large-scale production applications. But with the fundamental knowledge of databases, if required you can learn these technologies on the job when required.
 
## Graph Databases
Graph Databases don't cluster data into collections but instead, every unit of data is a free-standing node. Instead of grouping data, relationships between individual nodes are details by creating edges.

[Neo4J](https://neo4j.com) is a [graph database](https://aws.amazon.com/nosql/graph/). These databases are optimized for data that can be represented easily by a [graph](http://web.cecs.pdx.edu/~sheard/course/Cs163/Doc/Graphs.html), a type of data structure
common in programming. Graphs are generally used to represent the relationships
between entities of the same type, such as in a social network (relationships between friends) or recommendation engines (relationships between movies). Graph databases like Neo4J use Cypher Query Language (CQL) in expressing queries to the database.

We won't explore Neo4J in this bootcamp, as it is seen in only very niche use cases. It can be easily integrated and used in Node.js applications, so if required can be learned on the job.

There are many databases in the market. In this bootcamp, our goal is to introduce you and help you learn some of the most popularly used databases in the industry so that you feel equipped for the job market. However, the tech industry is constantly growing and evolving, so you might have to learn about other databases or related concepts in the future. Web 3.0 is just around the corner! If you're wondering about Blockchain, then yes that is significantly growing more popular day-by-day. If you're feeling curious, you can read about the architecture of a Web 3.0 application [here](https://www.preethikasireddy.com/post/the-architecture-of-a-web-3-0-application).

As we approach the end of this module, we will go through an assignment on Elasticsearch, which is widely used by many companies today.

---
## References 
- https://shopify.engineering/five-common-data-stores-usage
- https://www.linkedin.com/pulse/understanding-data-databases-101-alex-merced
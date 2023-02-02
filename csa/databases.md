# Aurora

How many replicas / AZs does Aurora store data across?
6 replicas across 3 AZs

Which db uses a cluster of instances across multiple AZs with writer and reader endpoints?
Amazon Aurora

A serverless version of which database that is compatible with PostgreSQL and MySQL?
Aurora Serverless

How can you provide high write-availablity / failover to Aurora?
Aurora Multi-master (many masters across AZs)

How many DB instances does Aurora Global give you per region?
Up to 16

What service gives you multiple DB instances in each region and provides sub-second (<1 second) read replication?
Aurora Global

What feature of Aurora allows you to create a duplicate database faster than a snapshot?
Aurora Database Cloning

What two tools does Aurora Machine Learning use?
SageMaker and Comprehend

What version of Aurora is good for unpredictable/intermittent workloads?
Aurora Serverless

# Elasticache

What service provides managed Redis/Memcached dbs?
AWS Elasticache

What database service provides users with a username/password?
Redis Auth

Does Elasticache require a code change in your existing application?
Yes

What are 5 use cases for Elasticache?
Key/value store, user session data, frequent reads / less writes, cache queries and aggregate data

Can Elasticache use SQL?
No

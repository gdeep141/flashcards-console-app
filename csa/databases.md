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

# DynamoDB

This fully-managed NoSQL database comes with two provisioning modes - on-demand and provisioned.
DynamoDB

This feature allows integration with DynamoDB and Lambda/Kinesis to perform real-time processing on changes to the DB.
DynamoDB Streams

This cluster provides read-caching and microsecond latency for a NoSQL DB with TTL and rapidly changing schemas
DynamoDB Accelerator (DAX)

What feature allows DynamoDB to be replicated across regions when stream processing is enabled?
DynamoDB Global Tables

What are two backup modes of DynamoDB?
Automated PITR (up to 35 days) or On-Demand for longer-term retention

This fully-managed serverless NoSQL database is great for rapidly changing schemas
DynamoDB

This fully-managed serverless NoSQL database can have TTL enabled on objects for automated deletes of objects after a certain time
DynamoDB

How would you improve read performance on DynamoDB without impacting write performance?
Increase Read-Capacity-Units (RCU) while leaving Write-Capacity-Units (WCU) unchanged

Can DynamoDB be exported to S3?
Yes with PITR enabled and it won't affect RCU

What is the max object size in DynamoDB?
100kb

# DocumentDB

This NoSQL database stores JSON data
DocumentDB

This NoSQL database is an AWS-Native MongoDB-compatible db
DocumentDB

What NoSQL database can automatically scale up to millions of requests per second?
DocumentDB

# Amazon Neptune

What fully managed graph database is good for social networks?
Amazon Neptune

How many read-replicas / AZs does Neptune support?
15 read replicas across 3 AZs

# Amazon Keyspaces

This serverless NoSQL DB is good for Apache Cassandra
Amazon Keyspaces

What are two use cases for Amazon Keyspaces?
IoT devices, time-series data

# QLDB

This immutable database ledger stores all changes made over time and cannot be deleted
Amazon QLDB (Quantum Ledger DB)

What's the main difference between QLDB and Amazon Managed Blockchain?
QLDB has a centralized managed component - it's good for financial data regulations

# Amazon Timestream

This serverless DB is good for time-series data
Amazon Timestream

# Misc

What two databases are NoSQL?
DynamoDB and DocumentDB

This "database" is a key value store suitable for large objects
Amazon S3

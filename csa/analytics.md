# ATHENA

Serverless way to query data in S3 using SQL. Pay per TB scanned
AWS Athena

Used for ad-hoc queries / business intelligence / to query CloudTrail trails
AWS Athena

How can you improve Athena performance / cost savings?
Use AWS Glue / Apache Parquet to only retrieve the columns needed for scanning.

Column-oriented data format designed for efficient data storage and retrieval
Apache Parquet

Query data anywhere (data doesn't have to be in S3)
AWS Athena Federated Query

# ELASTIC MAP REDUCE

Analyse and process big data on AWS using FULLY MANAGED Hadoop Clusters
AWS EMR (Elastic Map Reduce)

100s of EC2 instances used for processing big data (FULLY MANAGED AND AUTOSCALING)
Hadoop Clusters used in AWS EMR (Elastic Map Reduce)

Used for web-indexing, data processing, machine learning
AWS EMR (Elastic Map Reduce)

Purchasing options for EMR (3 kinds)
On demand, spot instances, reserved instances (1-3 years)

What are the three node types for Elastic Map Reduce Hadoop Clusters?
Master node (cluster management), Core Node (run tasks and store data), Task node (run tasks, short-lived)

# GLUE

Fully serverless method to extract, transform, and load (ETL) data for analytics
AWS Glue

Transform data from S3 into a Parquet format then send to another S3 bucket (for use by AWS Athena)
AWS Glue

Run data crawlers on connected data sources, used by Athena, EMR, and Redshift Spectrum
AWS Glue Data Catalogue

Prevents you from reprocessing old data if running a new ETL job
AWS Glue Job Bookmarks

Create a combined view across multiple data stores using SQL
AWS Glue Elastic Views

Clean and normalise data using pre-built transforms
AWS Glue Databrew

A GUI to create, run, and monitor ETL jobs
AWS Glue Studio

Run ETL as streaming jobs (from streaming datasources such as kinesis) instead of batch jobs
AWS Glue Streaming ETL

# DATA LAKE FORMATION

Combine structured and unstructured data from multiple sources into a single source (using AWS Glue)
AWS Data Lakes

Use machine learning to automate complex steps to combine data from multiple sources
AWS Data Lakes

How long does AWS Data Lakes take to get started?
A few days

Centralized permissions for analytics sources - better than setting up security in multiple places
AWS Data Lakes

# MSK

Fully managed Apache Kafka Cluster on AWS
AWS MSK (Managed Streaming for Kafka)

An alternative to AWS Kinesis for data streaming, where you can store data indefinitely on EBS Volumes and have a higher message size limit than Kinesis's 1MB
AWS MSK (Managed Streaming for Kafka)

Run an Apache Kafka Cluster without managing capacity
AWS MSK Serverless

# Redshift

Online analysis and data warehousing for PETABYTES of data
AWS Redshift

Load massive amounts of data, but then get faster joins and queries due to indexing
AWS Redshift

Uses nodes in a cluster to load and SQL QUERY petabytes of data
AWS Redshift

Query petabytes of data stored in s3 without loading it first, by leveraging 1000s of nodes
AWS Redshift Spectrum

What's the difference between EMR and Redshift?
Both use clusters for analysing big data, but EMR uses Hadoop and is best for unstructured data. Redshift is pure SQL and better for structured data.

Pay as you go model for analysing big data.
AWS Redshift

# Quicksight

Interactive business intelligence dashboard with its own users (not IAM users)
AWS Quicksight

What engine does AWS Quicksight use for memory computation?
SPICE Engine, if the data is loaded into QuickSight

What pay model does AWS Quicksight use?
Per-session

Perform ad-hoc queries on data in s3 with a BI dashboard
AWS Quicksight

Athena and Redshift analytics can be used as sources for this service
AWS Quicksight

# Kinesis data analytics

Perform SQL statements from Kinesis Firehose or Kinesis Data Streams and send back into Firehose or Datastreams
Kinesis Data Analytics for SQL Applications

Uses Flink (more powerful than SQL) to analyse data from Kinesis Data Streams or Amazon MSK
Kinesis Data Analytics for Apache Flink

What is a more powerful tool than SQL that can analyse data streaming from Kinesis Data Streams or Amazon MSK only?
Kinesis Data Analytics for Apache Flink

# Opensearch

Search a database for partial matches
AWS OpenSearch

A good way to search databases such as DynamoDB for partial matches
AWS OpenSearch

How can data be loaded from other data sources into AWS OpenSearch
Kinesis Firehose or a Lambda Function that monitors changes to the data source

Is OpenSearch a fully-managed, SQL search engine?
No, the instances must be created manually and OpenSearch is NoSQL

# ATHENA

Serverless way to query data in S3 using SQL. Pay per TB scanned
Aws Athena

Used for ad-hoc queries / business intelligence / to query CloudTrail trails
AWS Athena

How can you improve Athena performance / cost savings?
Use AWS Glue or Apache Parquet to only retrieve the columns needed for scanning.

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

Clean and normalise data using pre-built transform
AWS Glue Databrew

A GUI to create, run, and monitor ETL jobs
AWS Glue Studio

Run ETL as streaming jobs (from streaming datasources such as kinesis) instead of batch jobs
AWS Glue Streaming ETL

# Data Lake Formation

Combine structured and unstructured data from multiple sources into a single source (using AWS Glue)
AWS Data Lakes

Use machine learning to automate complex steps to combine data from multiple sources
AWS Data Lakes

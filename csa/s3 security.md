Why might a website not be able to display images in a publicly accessible s3 bucket?
CORS is disabled on the bucket and must be enabled.

What default encryption do all s3 buckets use?
SSE-S3 encryption (server-side encryption)

How can you force encryption with a bucket policy?
Use a bucket policy that refuses PUT calls without encryption headers

How can you lock a Glacier vault so it can't be deleted for compliance and retention?
Using Glacier Vault Lock policies.

What criteria must be filled for an S3 object lock policy to be effective?
Versioning must be enabled on the bucket.

What allows you to lock down some objects within a bucket (instead of everything)?
S3 Object Lock

What two modes of s3 object lock have a retention period?
Compliance mode (cannot be deleted by anyone) and governance mode (can only be deleted by certain users)

What forever protects an s3 object from being deleted by anyone?
S3 Object Lock - Legal hold (can be removed by an admin)

How can you force users to use MFA whenever deleting an object or disabling versioning?
Enable MFA on the bucket via the command line

What is required for MFA delete to work on an s3 bucket?
Versioning enabled and a root user with MFA enabled

What 3 things does versioning enable for an s3 bucket?
Replication, Object Lock Policies, and MFA Delete

How can you generate a URL to allow anyone access to an object for a certain time?
Use a pre-signed URL

How can you track access to an s3 bucket from anywhere using another s3 bucket?
Use S3 Access Logs

Where must the target bucket for an S3 Access Logs be located?
In the same region as the source bucket.

How long will it take for s3 access logs to begin tracking access?
A few hours

How can you restrict access to certain folders within in an s3 bucket?
Use Access Points on folders with policies enabled

How can you modify an object before it is downloaded by a caller application?
Use s3 object lambda to connect to an access point

How could you remove PIID from data in an s3 bucket before it is retrieved by a caller-application?
Use s3 object lambda connected to an access point to modify the object before it is called

What does s3 object lambda connect to?
An access point on an s3 bucket

Which encryption method is fully managed by the customer?
Client-side encryption

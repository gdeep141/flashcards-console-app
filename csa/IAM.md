# AWS Directory services

Which service allows you to create an Active Directory in AWS?
AWS Directory Services

What are the three types of AWS Directory Service?
AWS Managed Microsoft AD, AD Connector, Simple AD

Which AWS Directory Service allows you to manage users on the cloud, share users with on-prem, and use MFA?
AWS Managed Microsoft AD

Which AWS Directory Service acts an a direct proxy to on-prem AD and supports MFA?
AD Connector

Which AWS Directory Service cannot be joined with an on-prem AD?
Simple AD

Which two AWS Directory Services allow you to connect to an on-prem AD?
AWS Managed Microsoft AD (to manage users on cloud) and AD Connector

# Cognito

Which AWS Service gives external users an identity to interact with web or mobile accounts?
AWS Cognito

Which serverless database of users gives sign-in functionality for app users?
Cognito User Pools

What provides AWS credentials for users to interact with AWS services directly?
Cognito Identity Pools

What's the difference between cognito user pools and cognito identity pools?
User pools are an authentication service (who are you), identity pools are an authorisation service (what you can do)

# AWS Control Tower

How would you set up a multi-account AWS environment based on best practices (using organisations etc)?
AWS Control Tower

How might you manage restricted access across multiple accounts?
AWS Control Tower Guardrails

What are the two types of AWS Control Tower Guardrails?
Preventive Guardrail (to stop accounts from doing things) and Detective Guardrail (to monitor accounts and resources)

# Roles and policies

Which tools can be used to generate and test policies?
AWS Policy Generator and AWS Policy Simulator

Which two services require IAM roles instead of policies?
ECS tasks and Kinesis Data Streams

What is the difference in using a role as a proxy vs a resource-based policy?
When using a role as a proxy you give up your original permissions, when using a policy you do not,

What sets the maximum permissions an IAM entity can get, regardless of policies attached to that entity?
IAM Permission Boundaries

Which managed policy restricts the client IP from which API calls are made?
aws:SourceIP

Which managed policy restricts the region the API calls are made to?
aws:RequestedRegion

Which managed policy restricts based on tags?
ec2:ResourceTag

Which managed policy forces MFA?
aws:MultiFactorAuthPresent

Which managed policy restricts accesses to accounts that are members of an organisation?
aws:PrincipalOrgID

You've set a policy on objects within a bucket using the ARN arn:aws:s3:::test, but the policy isn't affecting the objects in the bucket? What could be the issue?
ARNs must end in a /\* to affect objects within the bucket, the correct ARN would be arn:aws:s3:::test/\*

# IAM Identity Center

How can you manage one login to multiple AWS accounts within an Organisation?
IAM Identity Center

What identity providers can be used for IAM Identity Center?
Built-in identity center or 3rd party providers (e.g. microsoft AD)

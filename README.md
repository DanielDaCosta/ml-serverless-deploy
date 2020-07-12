# ml-production-deploy
Deploying Machine Learning models on AWS using Serverless Framework

# Details

The input data will be stored in a S3 bucket, in our case the csv file. 

The model file will also be stored inside a S3 bucket. Since the model file can be quite large (>90Mb), we will need to load it during AWS Lambda inference execution from Amazon S3. You can observe that the model downloading was placed outside of the handler function. This was done in order to take advantage of AWS Lambda container reuse. Any code executed outside of the handler method will be invoked only once upon container creation and kept in memory across calls to the same Lambda container, making subsequent calls to Lambda faster.


# Usage

In this repository will be using Python3.
```
serverless create --template aws-python3
```
Deployment

```
serverless deploy
```
# AWS: Serverless Application Model(SAM)
Simple sam application with basic integration with Api Gateway and Dynamo DB.

## Commands

### Creating a s3 bucket
```
aws s3 mb s3://ashwani-sam
```

### Packaging Cloudformation
```
aws cloudformation package --s3-bucket ashwani-sam --template-file template.yaml --output-template-file target/template-generated.yaml
```

### Deploying to Cloudformation
```
aws cloudformation deploy --template-file target/template-generated.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM 
```

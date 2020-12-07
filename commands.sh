# Creating a s3 bucket
# aws s3 mb s3://ashwani-sam

# Package Cloudformation
aws cloudformation package --s3-bucket ashwani-sam --template-file template.yaml --output-template-file target/template-generated.yaml

# Deploy
aws cloudformation deploy --template-file target/template-generated.yaml --stack-name hello-world-sam --capabilities CAPABILITY_IAM 

# 01 - Function as a Service (FaaS)

## Overview
This folder contains resources, examples, and projects related to **Function as a Service (FaaS)** and **Serverless Computing** architectures.

## What is Function as a Service?
Function as a Service (FaaS) is a cloud computing service that allows developers to execute code in response to events without managing the underlying infrastructure. The cloud provider automatically manages the compute resources.

## Key Characteristics
- **Event-driven**: Functions execute in response to triggers
- **Stateless**: Each function execution is independent
- **Auto-scaling**: Automatically scales based on demand
- **Pay-per-use**: Only pay for actual execution time
- **No server management**: Cloud provider handles infrastructure

## Technologies Covered

### AWS Serverless
- **AWS Lambda**: Core serverless compute service
- **API Gateway**: RESTful API creation and management
- **DynamoDB**: NoSQL database for serverless applications
- **S3**: Object storage with event triggers
- **CloudWatch**: Monitoring and logging
- **SAM (Serverless Application Model)**: Infrastructure as code for serverless

### Azure Serverless
- **Azure Functions**: Microsoft's serverless compute platform
- **Logic Apps**: Workflow automation
- **Cosmos DB**: Multi-model database service
- **Event Grid**: Event routing service

### Google Cloud Serverless
- **Cloud Functions**: Google's serverless platform
- **Cloud Run**: Containerized serverless applications
- **Firestore**: NoSQL document database
- **Cloud Pub/Sub**: Messaging service

## Common Use Cases
1. **API Backends**: RESTful APIs without server management
2. **Data Processing**: ETL pipelines and data transformation
3. **Event Processing**: File uploads, database changes, IoT events
4. **Scheduled Tasks**: Cron jobs and periodic processing
5. **Real-time Applications**: Chat applications, notifications
6. **Microservices**: Small, focused business functions

## Project Structure
```
01-function-as-service/
├── aws-lambda/
│   ├── hello-world/
│   ├── api-gateway-integration/
│   ├── s3-event-processing/
│   └── dynamodb-crud/
├── azure-functions/
│   ├── http-trigger/
│   ├── timer-trigger/
│   └── blob-trigger/
├── google-cloud-functions/
│   ├── http-functions/
│   ├── pub-sub-functions/
│   └── storage-functions/
├── frameworks/
│   ├── serverless-framework/
│   ├── sam-templates/
│   └── terraform-serverless/
└── examples/
    ├── simple-crud-api/
    ├── image-processing/
    └── real-time-chat/
```

## Learning Path
1. **Week 1**: Serverless concepts and AWS Lambda basics
2. **Week 2**: API Gateway integration and DynamoDB
3. **Week 3**: Event-driven architectures and S3 triggers
4. **Week 4**: Advanced patterns and multi-cloud serverless
5. **Week 5**: Serverless frameworks and deployment automation

## Benefits of Serverless
- ✅ **Reduced operational overhead**
- ✅ **Automatic scaling**
- ✅ **Cost-effective for variable workloads**
- ✅ **Faster time to market**
- ✅ **Built-in high availability**

## Challenges to Consider
- ⚠️ **Cold start latency**
- ⚠️ **Vendor lock-in**
- ⚠️ **Limited execution time**
- ⚠️ **Debugging complexity**
- ⚠️ **State management challenges**

## Getting Started
1. Set up AWS account with Lambda access
2. Install AWS CLI and SAM CLI
3. Create your first "Hello World" function
4. Deploy using infrastructure as code
5. Monitor with CloudWatch

## Resources
- [AWS Lambda Documentation](https://docs.aws.amazon.com/lambda/)
- [Serverless Framework](https://www.serverless.com/)
- [AWS SAM Documentation](https://docs.aws.amazon.com/serverless-application-model/)
- [Serverless Patterns](https://serverlessland.com/patterns)

---
*This folder is part of the Cloud Career Roadmap: Zero to Hero Job Ready program*
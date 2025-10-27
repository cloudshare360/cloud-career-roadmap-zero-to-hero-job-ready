# 🔵 Azure Functions Implementation Guide
*Master Azure Serverless for Immediate Job Opportunities*

## 🎯 Quick Start Setup (15 minutes)

### **Prerequisites Installation**
```bash
# Install Azure CLI
curl -sL https://aka.ms/InstallAzureCLIDeb | sudo bash

# Install Azure Functions Core Tools
npm install -g azure-functions-core-tools@4 --unsafe-perm true

# Install Azure Extensions for VS Code
code --install-extension ms-azuretools.vscode-azurefunctions

# Login to Azure
az login
```

### **Create Your First Azure Function**
```bash
# Create new function app
func init MyAzureFunctionApp --typescript
cd MyAzureFunctionApp

# Create HTTP trigger function
func new --name HttpTriggerFunction --template "HTTP trigger" --authlevel "anonymous"

# Run locally
func start
```

## 🚀 Core Azure Functions Patterns

### **1. HTTP Trigger with TypeScript**
```typescript
// HttpTriggerFunction/index.ts
import { AzureFunction, Context, HttpRequest } from "@azure/functions";

interface RequestBody {
    name?: string;
    email?: string;
}

interface ResponseBody {
    message: string;
    timestamp: string;
    requestId: string;
}

const httpTrigger: AzureFunction = async (context: Context, req: HttpRequest): Promise<void> => {
    context.log('HTTP trigger function processed a request.');

    // Input validation
    const { name, email }: RequestBody = req.body || {};
    
    if (!name || !email) {
        context.res = {
            status: 400,
            body: {
                error: "Name and email are required",
                code: "INVALID_INPUT"
            }
        };
        return;
    }

    // Business logic
    const response: ResponseBody = {
        message: `Hello ${name}! Welcome to Azure Functions.`,
        timestamp: new Date().toISOString(),
        requestId: context.invocationId
    };

    // Success response
    context.res = {
        status: 200,
        headers: {
            "Content-Type": "application/json",
            "X-Request-ID": context.invocationId
        },
        body: response
    };
};

export default httpTrigger;
```

### **2. Cosmos DB Integration**
```typescript
// CosmosDBFunction/index.ts
import { AzureFunction, Context, HttpRequest } from "@azure/functions";
import { CosmosClient } from "@azure/cosmos";

const cosmosClient = new CosmosClient({
    endpoint: process.env.COSMOS_DB_ENDPOINT!,
    key: process.env.COSMOS_DB_KEY!
});

const database = cosmosClient.database("TodoDB");
const container = database.container("TodoItems");

interface TodoItem {
    id?: string;
    title: string;
    description: string;
    completed: boolean;
    createdAt: string;
}

const cosmosDBFunction: AzureFunction = async (context: Context, req: HttpRequest): Promise<void> => {
    const method = req.method?.toLowerCase();

    try {
        switch (method) {
            case 'post':
                await createTodoItem(context, req);
                break;
            case 'get':
                await getTodoItems(context, req);
                break;
            case 'put':
                await updateTodoItem(context, req);
                break;
            case 'delete':
                await deleteTodoItem(context, req);
                break;
            default:
                context.res = { status: 405, body: "Method not allowed" };
        }
    } catch (error) {
        context.log.error('Error:', error);
        context.res = {
            status: 500,
            body: { error: "Internal server error" }
        };
    }
};

async function createTodoItem(context: Context, req: HttpRequest) {
    const todoItem: TodoItem = {
        ...req.body,
        id: undefined, // Let Cosmos DB generate ID
        createdAt: new Date().toISOString()
    };

    const { resource: createdItem } = await container.items.create(todoItem);
    
    context.res = {
        status: 201,
        body: createdItem
    };
}

async function getTodoItems(context: Context, req: HttpRequest) {
    const { resources: items } = await container.items
        .query("SELECT * FROM c ORDER BY c.createdAt DESC")
        .fetchAll();

    context.res = {
        status: 200,
        body: items
    };
}

export default cosmosDBFunction;
```

### **3. Service Bus Queue Trigger**
```typescript
// ServiceBusFunction/index.ts
import { AzureFunction, Context } from "@azure/functions";

interface OrderMessage {
    orderId: string;
    customerId: string;
    items: Array<{
        productId: string;
        quantity: number;
        price: number;
    }>;
    totalAmount: number;
}

const serviceBusQueueTrigger: AzureFunction = async (context: Context, myQueueItem: OrderMessage): Promise<void> => {
    context.log('Service Bus queue trigger function processed message:', myQueueItem);

    try {
        // Validate order
        await validateOrder(myQueueItem);
        
        // Process payment
        const paymentResult = await processPayment(myQueueItem);
        
        // Update inventory
        await updateInventory(myQueueItem.items);
        
        // Send confirmation email
        await sendConfirmationEmail(myQueueItem.customerId, myQueueItem.orderId);
        
        context.log(`Order ${myQueueItem.orderId} processed successfully`);
        
    } catch (error) {
        context.log.error(`Error processing order ${myQueueItem.orderId}:`, error);
        
        // Send to dead letter queue or retry logic
        throw error; // This will trigger retry mechanism
    }
};

async function validateOrder(order: OrderMessage): Promise<void> {
    if (!order.orderId || !order.customerId || !order.items.length) {
        throw new Error("Invalid order data");
    }
    
    if (order.totalAmount <= 0) {
        throw new Error("Invalid order amount");
    }
}

async function processPayment(order: OrderMessage): Promise<{ success: boolean; transactionId: string }> {
    // Simulate payment processing
    return new Promise((resolve) => {
        setTimeout(() => {
            resolve({
                success: true,
                transactionId: `txn_${Date.now()}`
            });
        }, 1000);
    });
}

async function updateInventory(items: OrderMessage['items']): Promise<void> {
    // Update inventory in database
    for (const item of items) {
        // Simulate inventory update
        console.log(`Updating inventory for product ${item.productId}, quantity: ${item.quantity}`);
    }
}

async function sendConfirmationEmail(customerId: string, orderId: string): Promise<void> {
    // Send email using SendGrid, Azure Communication Services, etc.
    console.log(`Sending confirmation email for order ${orderId} to customer ${customerId}`);
}

export default serviceBusQueueTrigger;
```

### **4. Timer Trigger for Scheduled Tasks**
```typescript
// TimerFunction/index.ts
import { AzureFunction, Context } from "@azure/functions";
import { BlobServiceClient } from "@azure/storage-blob";
import { TableClient } from "@azure/data-tables";

interface BackupMetadata {
    partitionKey: string;
    rowKey: string;
    backupDate: string;
    status: 'started' | 'completed' | 'failed';
    recordCount?: number;
    fileSize?: number;
}

const timerTrigger: AzureFunction = async function (context: Context, myTimer: any): Promise<void> {
    const timeStamp = new Date().toISOString();
    
    if (myTimer.isPastDue) {
        context.log('Timer function is running late!');
    }
    
    context.log('Daily backup timer trigger function started at:', timeStamp);

    try {
        // Initialize Azure Storage clients
        const blobServiceClient = BlobServiceClient.fromConnectionString(
            process.env.AZURE_STORAGE_CONNECTION_STRING!
        );
        
        const tableClient = TableClient.fromConnectionString(
            process.env.AZURE_STORAGE_CONNECTION_STRING!,
            "BackupMetadata"
        );

        // Start backup process
        const backupId = `backup_${Date.now()}`;
        const backupMetadata: BackupMetadata = {
            partitionKey: "DailyBackup",
            rowKey: backupId,
            backupDate: timeStamp,
            status: 'started'
        };

        // Log backup start
        await tableClient.createEntity(backupMetadata);

        // Perform database backup
        const backupResult = await performDatabaseBackup(blobServiceClient, backupId);

        // Update backup metadata
        backupMetadata.status = 'completed';
        backupMetadata.recordCount = backupResult.recordCount;
        backupMetadata.fileSize = backupResult.fileSize;
        
        await tableClient.updateEntity(backupMetadata);

        context.log(`Backup ${backupId} completed successfully. Records: ${backupResult.recordCount}`);

    } catch (error) {
        context.log.error('Backup failed:', error);
        
        // Log error to monitoring system
        // You could also send alerts here
    }
};

async function performDatabaseBackup(blobServiceClient: BlobServiceClient, backupId: string) {
    // Simulate database backup
    const containerClient = blobServiceClient.getContainerClient("backups");
    
    // Ensure container exists
    await containerClient.createIfNotExists();
    
    // Create backup file
    const backupFileName = `${backupId}.json`;
    const blockBlobClient = containerClient.getBlockBlobClient(backupFileName);
    
    // Simulate data export (replace with actual database query)
    const mockData = {
        users: Array.from({ length: 1000 }, (_, i) => ({
            id: i + 1,
            name: `User ${i + 1}`,
            email: `user${i + 1}@example.com`
        })),
        timestamp: new Date().toISOString()
    };
    
    const backupData = JSON.stringify(mockData, null, 2);
    
    // Upload to blob storage
    await blockBlobClient.upload(backupData, Buffer.byteLength(backupData));
    
    return {
        recordCount: mockData.users.length,
        fileSize: Buffer.byteLength(backupData)
    };
}

export default timerTrigger;
```

## 📦 Application Settings & Configuration

### **local.settings.json**
```json
{
  "IsEncrypted": false,
  "Values": {
    "AzureWebJobsStorage": "UseDevelopmentStorage=true",
    "FUNCTIONS_WORKER_RUNTIME": "node",
    "COSMOS_DB_ENDPOINT": "https://your-cosmos-account.documents.azure.com:443/",
    "COSMOS_DB_KEY": "your-cosmos-primary-key",
    "AZURE_STORAGE_CONNECTION_STRING": "DefaultEndpointsProtocol=https;AccountName=your-storage-account;AccountKey=your-key;EndpointSuffix=core.windows.net",
    "ServiceBusConnection": "Endpoint=sb://your-servicebus.servicebus.windows.net/;SharedAccessKeyName=RootManageSharedAccessKey;SharedAccessKey=your-key"
  },
  "ConnectionStrings": {}
}
```

### **function.json Examples**

#### HTTP Trigger
```json
{
  "bindings": [
    {
      "authLevel": "anonymous",
      "type": "httpTrigger",
      "direction": "in",
      "name": "req",
      "methods": ["get", "post", "put", "delete"]
    },
    {
      "type": "http",
      "direction": "out",
      "name": "res"
    }
  ],
  "scriptFile": "../dist/HttpTriggerFunction/index.js"
}
```

#### Service Bus Queue Trigger
```json
{
  "bindings": [
    {
      "name": "myQueueItem",
      "type": "serviceBusTrigger",
      "direction": "in",
      "queueName": "order-processing",
      "connection": "ServiceBusConnection"
    }
  ],
  "scriptFile": "../dist/ServiceBusFunction/index.js"
}
```

#### Timer Trigger (Daily at 2 AM)
```json
{
  "bindings": [
    {
      "name": "myTimer",
      "type": "timerTrigger",
      "direction": "in",
      "schedule": "0 0 2 * * *"
    }
  ],
  "scriptFile": "../dist/TimerFunction/index.js"
}
```

## 🚀 Deployment & DevOps

### **Azure DevOps Pipeline**
```yaml
# azure-pipelines.yml
trigger:
- main

pool:
  vmImage: 'ubuntu-latest'

variables:
  azureSubscription: 'your-service-connection'
  functionAppName: 'your-function-app-name'
  resourceGroupName: 'your-resource-group'

stages:
- stage: Build
  jobs:
  - job: BuildJob
    steps:
    - task: NodeTool@0
      inputs:
        versionSpec: '18.x'
      displayName: 'Install Node.js'

    - script: |
        npm install
        npm run build
        npm prune --production
      displayName: 'npm install, build and prune'

    - task: ArchiveFiles@2
      inputs:
        rootFolderOrFile: '$(System.DefaultWorkingDirectory)'
        includeRootFolder: false
        archiveType: 'zip'
        archiveFile: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip'
        replaceExistingArchive: true

    - task: PublishBuildArtifacts@1
      inputs:
        PathtoPublish: '$(Build.ArtifactStagingDirectory)/$(Build.BuildId).zip'
        ArtifactName: 'drop'

- stage: Deploy
  dependsOn: Build
  jobs:
  - deployment: DeployJob
    environment: 'production'
    strategy:
      runOnce:
        deploy:
          steps:
          - task: AzureFunctionApp@1
            inputs:
              azureSubscription: '$(azureSubscription)'
              appType: 'functionApp'
              appName: '$(functionAppName)'
              resourceGroupName: '$(resourceGroupName)'
              package: '$(Pipeline.Workspace)/drop/$(Build.BuildId).zip'
```

### **Infrastructure as Code with Bicep**
```bicep
// main.bicep
param functionAppName string
param location string = resourceGroup().location
param storageAccountName string
param appServicePlanName string

// Storage Account
resource storageAccount 'Microsoft.Storage/storageAccounts@2021-09-01' = {
  name: storageAccountName
  location: location
  sku: {
    name: 'Standard_LRS'
  }
  kind: 'StorageV2'
}

// App Service Plan
resource appServicePlan 'Microsoft.Web/serverfarms@2021-03-01' = {
  name: appServicePlanName
  location: location
  sku: {
    name: 'Y1'
    tier: 'Dynamic'
  }
  properties: {
    reserved: true
  }
}

// Function App
resource functionApp 'Microsoft.Web/sites@2021-03-01' = {
  name: functionAppName
  location: location
  kind: 'functionapp,linux'
  properties: {
    serverFarmId: appServicePlan.id
    siteConfig: {
      appSettings: [
        {
          name: 'AzureWebJobsStorage'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'WEBSITE_CONTENTAZUREFILECONNECTIONSTRING'
          value: 'DefaultEndpointsProtocol=https;AccountName=${storageAccount.name};EndpointSuffix=${environment().suffixes.storage};AccountKey=${storageAccount.listKeys().keys[0].value}'
        }
        {
          name: 'FUNCTIONS_EXTENSION_VERSION'
          value: '~4'
        }
        {
          name: 'FUNCTIONS_WORKER_RUNTIME'
          value: 'node'
        }
        {
          name: 'WEBSITE_NODE_DEFAULT_VERSION'
          value: '~18'
        }
      ]
      linuxFxVersion: 'NODE|18'
    }
  }
}

output functionAppName string = functionApp.name
output functionAppUrl string = 'https://${functionApp.properties.defaultHostName}'
```

## 🎯 Job Interview Preparation

### **Key Azure Functions Concepts to Master**
1. **Trigger Types**: HTTP, Timer, Service Bus, Event Hub, Cosmos DB
2. **Bindings**: Input/Output bindings for various services
3. **Durable Functions**: Stateful functions and orchestrations
4. **Security**: Authentication, authorization, managed identity
5. **Monitoring**: Application Insights, custom metrics
6. **Performance**: Cold starts, scaling, memory optimization

### **Common Interview Questions & Answers**

**Q: How do you handle cold starts in Azure Functions?**
```
A: Several strategies:
1. Use Premium Plan for pre-warmed instances
2. Implement connection pooling for databases
3. Minimize dependencies and package size
4. Use singleton pattern for expensive objects
5. Consider Durable Functions for long-running processes
```

**Q: How do you implement error handling and retry logic?**
```
A: 
1. Built-in retry policies for triggers
2. Dead letter queues for poison messages
3. Try-catch blocks with structured logging
4. Circuit breaker pattern for external services
5. Application Insights for monitoring and alerting
```

### **Azure Functions Salary Expectations**
- **Junior Azure Functions Developer**: $75K-95K
- **Senior Azure Functions Developer**: $100K-130K
- **Azure Serverless Architect**: $130K-160K
- **Multi-cloud Serverless Expert**: $150K-180K

---

**Next Steps**: Practice with the provided code examples, deploy to Azure, and add these projects to your portfolio. Focus on the patterns that are most relevant to your target job roles!
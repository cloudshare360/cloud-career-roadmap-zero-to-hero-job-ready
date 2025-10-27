# Conversation 05: Infrastructure as Code with Terraform

## Metadata
- **Date**: 2025-10-24
- **Platform**: Qwen AI
- **Topic Category**: Infrastructure as Code
- **Difficulty Level**: Intermediate to Advanced
- **Duration**: 40 minutes
- **Conversation Index**: 05

## Question/Query
I keep hearing about Infrastructure as Code and Terraform specifically. I understand the concept but I'm not sure how to get started practically. Can you show me how to create real AWS infrastructure with Terraform? What are the best practices I should follow from the beginning?

## AI Response/Solution
Infrastructure as Code (IaC) is a game-changer for managing cloud resources. Let me walk you through Terraform with practical examples and best practices.

**What is Infrastructure as Code?**
Instead of clicking through AWS console to create resources, you write code that describes your infrastructure. This code can be versioned, tested, and automated.

**Terraform Basics - Complete Example:**

**1. Project Structure:**
```
terraform-project/
├── main.tf
├── variables.tf
├── outputs.tf
├── terraform.tfvars
└── modules/
    └── vpc/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

**2. Provider Configuration (main.tf):**
```hcl
terraform {
  required_version = ">= 1.0"
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "dev/terraform.tfstate"
    region = "us-west-2"
  }
}

provider "aws" {
  region = var.aws_region
  
  default_tags {
    tags = {
      Environment = var.environment
      Project     = var.project_name
      ManagedBy   = "Terraform"
    }
  }
}
```

**3. Variables (variables.tf):**
```hcl
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "environment" {
  description = "Environment name"
  type        = string
  validation {
    condition = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}

variable "project_name" {
  description = "Name of the project"
  type        = string
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}
```

**4. Main Infrastructure (main.tf continued):**
```hcl
# Data sources
data "aws_availability_zones" "available" {
  state = "available"
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true

  tags = {
    Name = "${var.project_name}-${var.environment}-vpc"
  }
}

# Internet Gateway
resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id

  tags = {
    Name = "${var.project_name}-${var.environment}-igw"
  }
}

# Public Subnets
resource "aws_subnet" "public" {
  count = 2

  vpc_id                  = aws_vpc.main.id
  cidr_block              = "10.0.${count.index + 1}.0/24"
  availability_zone       = data.aws_availability_zones.available.names[count.index]
  map_public_ip_on_launch = true

  tags = {
    Name = "${var.project_name}-${var.environment}-public-${count.index + 1}"
    Type = "Public"
  }
}

# Route Table for Public Subnets
resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id

  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }

  tags = {
    Name = "${var.project_name}-${var.environment}-public-rt"
  }
}

# Route Table Associations
resource "aws_route_table_association" "public" {
  count = length(aws_subnet.public)

  subnet_id      = aws_subnet.public[count.index].id
  route_table_id = aws_route_table.public.id
}

# Security Group for Web Servers
resource "aws_security_group" "web" {
  name_prefix = "${var.project_name}-${var.environment}-web"
  vpc_id      = aws_vpc.main.id

  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 443
    to_port     = 443
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }

  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.vpc_cidr]
  }

  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }

  tags = {
    Name = "${var.project_name}-${var.environment}-web-sg"
  }
}

# Launch Template
resource "aws_launch_template" "web" {
  name_prefix   = "${var.project_name}-${var.environment}-"
  image_id      = "ami-0c02fb55956c7d316" # Amazon Linux 2
  instance_type = "t3.micro"

  vpc_security_group_ids = [aws_security_group.web.id]

  user_data = base64encode(<<-EOF
              #!/bin/bash
              yum update -y
              yum install -y httpd
              systemctl start httpd
              systemctl enable httpd
              echo "<h1>Hello from ${var.environment}</h1>" > /var/www/html/index.html
              EOF
  )

  tag_specifications {
    resource_type = "instance"
    tags = {
      Name = "${var.project_name}-${var.environment}-web"
    }
  }
}

# Auto Scaling Group
resource "aws_autoscaling_group" "web" {
  name                = "${var.project_name}-${var.environment}-asg"
  vpc_zone_identifier = aws_subnet.public[*].id
  target_group_arns   = [aws_lb_target_group.web.arn]
  health_check_type   = "ELB"
  min_size            = 1
  max_size            = 3
  desired_capacity    = 2

  launch_template {
    id      = aws_launch_template.web.id
    version = "$Latest"
  }

  tag {
    key                 = "Name"
    value               = "${var.project_name}-${var.environment}-asg"
    propagate_at_launch = false
  }
}

# Application Load Balancer
resource "aws_lb" "web" {
  name               = "${var.project_name}-${var.environment}-alb"
  internal           = false
  load_balancer_type = "application"
  security_groups    = [aws_security_group.web.id]
  subnets            = aws_subnet.public[*].id
}

# Target Group
resource "aws_lb_target_group" "web" {
  name     = "${var.project_name}-${var.environment}-tg"
  port     = 80
  protocol = "HTTP"
  vpc_id   = aws_vpc.main.id

  health_check {
    enabled             = true
    healthy_threshold   = 2
    unhealthy_threshold = 2
    timeout             = 5
    interval            = 30
    path                = "/"
    matcher             = "200"
  }
}

# Load Balancer Listener
resource "aws_lb_listener" "web" {
  load_balancer_arn = aws_lb.web.arn
  port              = "80"
  protocol          = "HTTP"

  default_action {
    type             = "forward"
    target_group_arn = aws_lb_target_group.web.arn
  }
}
```

**5. Outputs (outputs.tf):**
```hcl
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "load_balancer_dns" {
  description = "DNS name of the load balancer"
  value       = aws_lb.web.dns_name
}

output "public_subnet_ids" {
  description = "IDs of the public subnets"
  value       = aws_subnet.public[*].id
}
```

**6. Environment Variables (terraform.tfvars):**
```hcl
aws_region   = "us-west-2"
environment  = "dev"
project_name = "my-web-app"
vpc_cidr     = "10.0.0.0/16"
```

**Essential Commands:**
```bash
# Initialize Terraform
terraform init

# Plan changes
terraform plan

# Apply changes
terraform apply

# Destroy infrastructure
terraform destroy

# Format code
terraform fmt

# Validate configuration
terraform validate
```

**Terraform Best Practices:**

**1. State Management:**
- Always use remote state (S3 + DynamoDB for locking)
- Never commit state files to version control
- Use separate state files for different environments

**2. Code Organization:**
- Use modules for reusable components
- Separate environments with different tfvars files
- Keep resource definitions logical and grouped

**3. Security:**
- Use IAM roles instead of access keys when possible
- Implement least privilege principle
- Store secrets in AWS Secrets Manager, not in code

**4. Versioning:**
- Pin provider versions
- Use semantic versioning for modules
- Tag all releases

**5. Testing:**
- Use `terraform plan` before every apply
- Implement automated testing with tools like Terratest
- Use `terraform validate` and `terraform fmt` in CI/CD

## Key Takeaways
- Infrastructure as Code makes infrastructure reproducible and versionable
- Terraform state is critical - always use remote state in production
- Start simple and gradually add complexity
- Modules promote reusability and maintainability
- Always run `terraform plan` before applying changes
- Use consistent naming conventions and tagging strategies
- Infrastructure changes should go through the same review process as code

## Action Items
- [ ] Install Terraform CLI and configure AWS credentials
- [ ] Create first simple Terraform configuration (VPC + EC2)
- [ ] Set up remote state storage with S3 backend
- [ ] Practice with terraform plan/apply/destroy cycle
- [ ] Create reusable modules for common infrastructure patterns
- [ ] Integrate Terraform with CI/CD pipeline
- [ ] Study Terraform state management and import capabilities
- [ ] Learn about terraform workspaces for environment management

## Related Topics
- Terraform Cloud vs. self-managed state
- Alternative IaC tools (CloudFormation, Pulumi, CDK)
- GitOps workflows with infrastructure
- Terraform testing strategies and tools
- Multi-cloud infrastructure with Terraform
- Infrastructure security scanning and compliance

## Follow-up Questions
- How do I manage secrets and sensitive data in Terraform?
- What's the best way to structure Terraform projects for multiple environments?
- How do I handle Terraform state conflicts in team environments?
- What are the pros and cons of Terraform vs CloudFormation?

## Tags
`#terraform` `#infrastructure-as-code` `#iac` `#aws` `#automation` `#devops` `#cloud-infrastructure`
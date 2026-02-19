# LocalStack + Terraform Infrastructure Project

A production-grade Infrastructure-as-Code (IaC) project demonstrating modular Terraform design patterns with LocalStack for local AWS simulation. This project provisions S3, SQS, and DynamoDB resources and includes a Python application layer to validate infrastructure functionality.

## 🎯 Project Goals

- Learn Terraform fundamentals (providers, resources, modules, state management)
- Build reusable infrastructure modules following DRY principles
- Implement production best practices (tagging, variables, outputs)
- Integrate application code with provisioned infrastructure
- Practice local development workflows without incurring cloud costs

## 🏗️ Architecture
```
┌─────────────────────────────────────────┐
│         Python Application              │
│  (Reads Terraform outputs dynamically)  │
└──────────────┬──────────────────────────┘
               │
               ▼
┌─────────────────────────────────────────┐
│          LocalStack (Port 4566)         │
│  ┌─────────┐  ┌─────────┐  ┌─────────┐ │
│  │   S3    │  │   SQS   │  │DynamoDB │ │
│  │ Bucket  │  │  Queue  │  │  Table  │ │
│  └─────────┘  └─────────┘  └─────────┘ │
└─────────────────────────────────────────┘
               ▲
               │
┌──────────────┴──────────────────────────┐
│         Terraform Modules               │
│  modules/s3  modules/sqs  modules/dyndb │
└─────────────────────────────────────────┘
```

## 📁 Project Structure
```
terraform-localstack-project/
├── main.tf              # Root module orchestration
├── variables.tf         # Input variables
├── outputs.tf           # Infrastructure outputs
├── app.py               # Python application (tests infrastructure)
├── .gitignore           # Git ignore rules
│
└── modules/             # Reusable Terraform modules
    ├── s3/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    ├── sqs/
    │   ├── main.tf
    │   ├── variables.tf
    │   └── outputs.tf
    └── dynamodb/
        ├── main.tf
        ├── variables.tf
        └── outputs.tf
```

## 🚀 Getting Started

### Prerequisites

- **Docker Desktop** (for running LocalStack)
- **Terraform** (v1.14+)
- **AWS CLI** (v2.x)
- **Python** (v3.12+)
- **Git**

### Installation

1. **Clone the repository:**
```bash
   git clone https://github.com/yosephguta/terraform-localstack-project.git
   cd terraform-localstack-project
```

2. **Start LocalStack:**
```bash
   docker run -d \
     --name localstack \
     -p 4566:4566 \
     -e SERVICES=s3,sqs,dynamodb \
     localstack/localstack:latest
```

3. **Configure AWS CLI for LocalStack:**
```bash
   aws configure
   # Access Key: test
   # Secret Key: test
   # Region: us-east-1
   # Output: json
```

4. **Initialize Terraform:**
```bash
   terraform init
```

5. **Deploy infrastructure:**
```bash
   terraform apply
```

6. **Install Python dependencies:**
```bash
   pip install boto3
```

7. **Run the application:**
```bash
   python app.py
```

## 🛠️ Key Features

### 1. Modular Infrastructure
Each AWS service (S3, SQS, DynamoDB) is encapsulated in a reusable module with:
- Input variables for customization
- Outputs for integration with other modules
- Consistent tagging strategy

### 2. Dynamic Configuration
The Python application reads infrastructure details directly from Terraform outputs:
```python
BUCKET_NAME = get_terraform_output('s3_bucket_name')
QUEUE_URL = get_terraform_output('sqs_queue_url')
TABLE_NAME = get_terraform_output('dynamodb_table_name')
```

### 3. Production Best Practices
- **Resource tagging** for cost tracking and ownership
- **Variable-driven configuration** (no hardcoded values)
- **Force destroy enabled** for easy dev environment cleanup
- **Path-style S3 URLs** for LocalStack compatibility

### 4. Application Integration
Python script demonstrates full CRUD operations:
- Upload files to S3
- Send/receive messages via SQS
- Write/read data from DynamoDB

## 📊 What I Learned

### Technical Skills
- Terraform module design patterns
- State management and drift detection
- AWS SDK (boto3) integration
- Docker containerization basics
- Infrastructure testing strategies

### Key Takeaways
1. **Modules are functions for infrastructure** - Reusable, testable, composable
2. **State is the source of truth** - Must stay in sync with reality
3. **Tags are critical** - Enable cost tracking and resource management
4. **LocalStack limitations** - Some AWS features aren't fully emulated
5. **Idempotency matters** - `terraform apply` should be safe to re-run

## 🐛 Troubleshooting

### LocalStack Connection Errors
```bash
# Check if LocalStack is running
docker ps

# Verify health endpoint
curl http://localhost:4566/_localstack/health
```

### State Drift Issues
```bash
# Refresh state to sync with reality
terraform apply -refresh-only

# Nuclear option: destroy and recreate
terraform destroy && terraform apply
```

### Python Module Errors
```bash
# Ensure boto3 is installed
pip install boto3

# Verify Terraform outputs exist
terraform output
```

## 🔮 Future Enhancements

- [ ] Add Lambda functions for event-driven processing
- [ ] Implement remote state backend (S3 + DynamoDB locking)
- [ ] Add input validation with custom Terraform conditions
- [ ] Create CI/CD pipeline with GitHub Actions
- [ ] Add Terraform Cloud integration
- [ ] Implement multi-environment support (dev/staging/prod)
- [ ] Add comprehensive error handling in Python app

## 📚 Resources

- [Terraform Documentation](https://www.terraform.io/docs)
- [LocalStack Documentation](https://docs.localstack.cloud)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS CLI Reference](https://awscli.amazonaws.com/v2/documentation/api/latest/index.html)

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

## 🤝 Contributing

This is a personal learning project, but feedback and suggestions are welcome! Feel free to open an issue or submit a pull review. I will appreciate it.

---

**Built with ☕ and a lot of trial and error as part of my DevOps learning journey.**
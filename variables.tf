variable "project_name" {
  description = "Name of the project (used for resource naming)"
  type        = string
  default     = "terraform-localstack"
}

variable "environment" {
  description = "Environment (dev, staging, prod)"
  type        = string
  default     = "dev"
}

variable "s3_bucket_name" {
  description = "Name of the S3 bucket"
  type        = string
  default     = "my-terraform-bucket"
}

variable "sqs_queue_name" {
  description = "Name of the SQS queue"
  type        = string
  default     = "my-terraform-queue"
}

variable "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  type        = string
  default     = "my-terraform-table"
}

variable "dynamodb_hash_key" {
  description = "Hash key for DynamoDB table"
  type        = string
  default     = "id"
}
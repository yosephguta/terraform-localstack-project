provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_requesting_account_id  = true
  skip_metadata_api_check     = true
  s3_use_path_style           = true

  endpoints {
    s3       = "http://localhost:4566"
    sqs      = "http://localhost:4566"
    dynamodb = "http://localhost:4566"
  }
}

locals {
  common_tags = {
    Project     = var.project_name
    Environment = var.environment
    ManagedBy   = "Terraform"
    Owner       = "DevOps Team"
  }
}

module "my_bucket" {
  source      = "./modules/s3"
  bucket_name = var.s3_bucket_name
  tags        = local.common_tags
}

module "my_queue" {
  source     = "./modules/sqs"
  queue_name = var.sqs_queue_name
  tags       = local.common_tags
}

module "my_table" {
  source        = "./modules/dynamodb"
  table_name    = var.dynamodb_table_name
  hash_key_name = var.dynamodb_hash_key
  tags          = local.common_tags
}
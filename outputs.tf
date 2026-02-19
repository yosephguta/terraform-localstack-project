output "s3_bucket_name" {
  description = "Name of the S3 bucket"
  value       = module.my_bucket.bucket_name
}

output "sqs_queue_url" {
  description = "URL of the SQS queue"
  value       = module.my_queue.queue_url
}

output "dynamodb_table_name" {
  description = "Name of the DynamoDB table"
  value       = module.my_table.table_name
}
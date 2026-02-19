output "queue_name" {
  description = "The name of the SQS Queue"
  value       = aws_sqs_queue.this.name
}

output "queue_arn" {
  description = "The ARN of the SQS Queue"
  value       = aws_sqs_queue.this.arn
}

output "queue_url" {
  description = "The URL of the SQS Queue"
  value       = aws_sqs_queue.this.url
}
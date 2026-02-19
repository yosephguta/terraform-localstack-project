output "table_name" {
  description = "The name of the dynamoDB table"
  value       = aws_dynamodb_table.this.name
}

output "table_arn" {
  description = "The ARN of the dynamodb"
  value       = aws_dynamodb_table.this.arn
}
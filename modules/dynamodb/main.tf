resource "aws_dynamodb_table" "this" {
  name = var.table_name
  billing_mode = "PAY_PER_REQUEST"
  tags = var.tags
  hash_key = var.hash_key_name

    attribute {
    name = var.hash_key_name
    type = "S"
}

}


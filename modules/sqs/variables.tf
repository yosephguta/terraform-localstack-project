variable "queue_name" {
  description = "Name of SQS queue"
  type = string
}

variable "tags" {
  description = "Tags to apply to the Item"
  type        = map(string)
  default     = {}
}

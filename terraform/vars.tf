variable "flask_env" {}

variable "oauth_client_id" {
    sensitive = true
}
variable "oauth_client_secret" {
    sensitive = true
}
variable "admin_id" {
    sensitive = true
}

variable "tasks_db_name" {
    default = "tasks_db"
}

variable "tasks_collection_name" {
    default = "tasks_collection"
}

variable "prefix" {
    description = "The prefix used for all resources in this environment"
}

variable "flask_app" {
    default = "todo_app/app"
}

variable "secret_key" {
    sensitive = true
}

# The "flask_env" variable is left empty, so you can decide the Flask environment you want to use. 
# The OAuth client ID and secret, admin ID, and secret key are marked as sensitive, 
# which means Terraform will mask their values in its output and logs.
# The default values for "tasks_db_name" and "tasks_collection_name" are set to "tasks_db" and "tasks_collection" respectively. 
# The "prefix" variable is used to prefix all resources in your environment, which helps in unique resource naming and easy management. 
# The "flask_app" variable is set to "todo_app/app" as the default value.

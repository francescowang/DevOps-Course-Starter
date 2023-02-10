# specifies the Azure provider and the version required by the Terraform configuration
terraform {
    required_providers {
    azurerm = {
        source  = "hashicorp/azurerm"
        version = ">= 3.8"
    }
}
    backend "azurerm" {
    resource_group_name  = "KPMG21_FrancescoWang_ProjectExercise"
    storage_account_name = "tfstatemodule12"
    container_name       = "tfstate"
    key                  = "terraform.tfstate"
}
}

# sets up the Azure provider and enables some optional features.
provider "azurerm" {
    features {}
}

# retrieves information about the resource group specified in the name variable.
data "azurerm_resource_group" "main" {
    name = "KPMG21_FrancescoWang_ProjectExercise"
}

# creates a storage account with the specified name and configuration, 
# including the resource group, location, account tier, and account replication type.
resource "azurerm_storage_account" "tfstate" {
    name                     = "tfstatemodule12"
    resource_group_name      = data.azurerm_resource_group.main.name
    location                 = data.azurerm_resource_group.main.location
    account_tier             = "Standard"
    account_replication_type = "LRS"
}

# creates a storage container within the storage account.
resource "azurerm_storage_container" "tfstate" {
    name                  = "tfstate"
    storage_account_name  = azurerm_storage_account.tfstate.name
    container_access_type = "blob"
}
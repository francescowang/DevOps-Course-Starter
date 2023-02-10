# creates a CosmosDB account with the specified name, location, resource group, offer type, kind, and version.
resource "azurerm_cosmosdb_account" "db_account" {
    name                 = "${var.prefix}-exercise-12-cosmosdb-account"
    location             = data.azurerm_resource_group.main.location
    resource_group_name  = data.azurerm_resource_group.main.name
    offer_type           = "Standard"
    kind                 = "MongoDB"
    mongo_server_version = 4.2

# enables serverless and MongoDB capabilities.
    capabilities {
        name = "EnableServerless"
}
    capabilities {
        name = "EnableMongo"
}

# sets the consistency level, maximum interval in seconds, and maximum staleness prefix.
    consistency_policy {
        consistency_level       = "BoundedStaleness"
        max_interval_in_seconds = 300
        max_staleness_prefix    = 100000
}

# sets the location of the database and the priority for failover.
    geo_location {
        location          = "uksouth"
        failover_priority = 0
}
}

# creates a MongoDB database within the CosmosDB account. 
# variables are populated from the values defined in the CosmosDB account block. 
resource "azurerm_cosmosdb_mongo_database" "db" {
    name                = "${var.prefix}-exercise-12-cosmosdb"
    resource_group_name = azurerm_cosmosdb_account.db_account.resource_group_name
    account_name        = azurerm_cosmosdb_account.db_account.name

# ensures that the database will not be destroyed by Terraform.
    lifecycle {
        prevent_destroy = true
}
}

# Once the Terraform configuration is applied, the specified CosmosDB account and MongoDB database will be created in the Azure cloud.
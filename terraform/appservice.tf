# creates resources in Azure to host a Linux web app.

# defines the underlying infrastructure for hosting the web app.

# The service plan is named <var.prefix>.prefix-exercise_12_asp, 
# with a location and resource group specified by the data.azurerm_resource_group data source. 
# The OS type is set to "Linux" and the plan is using the "B1" pricing tier.

resource "azurerm_service_plan" "main" {
    name                = "${var.prefix}-exercise_12_asp"
    location            = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    os_type             = "Linux"
    sku_name            = "B1"
}

# An Azure Linux Web App (azurerm_linux_web_app) named prefix-exercise-12-app, 
# with the same location and resource group as the service plan, 
# and using the service plan ID for its hosting infrastructure. 
# The web app's settings include several environment variables for the application's configuration, 
# such as the Docker registry server URL, the connection string to the CosmosDB database,
# and several other OAuth credentials and keys required by the application. 
# The site configuration specifies the Docker image (francescowang/to-do-app) to be used to host the web app, with the latest tag.

resource "azurerm_linux_web_app" "main" {
    name                = "${var.prefix}-exercise-12-app"
    location            = data.azurerm_resource_group.main.location
    resource_group_name = data.azurerm_resource_group.main.name
    service_plan_id     = azurerm_service_plan.main.id

    app_settings = {
        "DOCKER_REGISTRY_SERVER_URL" = "https://index.docker.io"
        "CLUSTER_CONNECTION_STRING"  = azurerm_cosmosdb_account.db_account.connection_strings[0]
        "ADMIN_ID"                   = var.admin_id
        "CLIENT_ID"                  = var.oauth_client_id
        "CLIENT_SECRET"              = var.oauth_client_secret
        "FLASK_APP"                  = var.flask_app
        "FLASK_ENV"                  = var.flask_env
        "SECRET_KEY"                 = var.secret_key
        "TASKS_COLLECTION_NAME"      = var.tasks_collection_name
        "TASKS_DB_NAME"              = var.tasks_db_name
}

    site_config {
        application_stack {
        docker_image     = "francescowang/to-do-app"
        docker_image_tag = "latest"
    }
}
}
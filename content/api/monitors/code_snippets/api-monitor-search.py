from datadog import initialize, api

options = {
	'api_key': '<YOUR_API_KEY>',
	'app_key': '<YOUR_APP_KEY>'
}

initialize(**options)

# Search monitors
api.Monitor.search()

# Examples of possible query parameters:
# api.Monitor.search(query="id:7100311")
# api.Monitor.search(query="title:foo metric:system.core.idle status:Alert")

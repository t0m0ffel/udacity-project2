import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://ff178600-01a7-4e22-8dc2-8eb264f41e97.southcentralus.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "rQkHHpTt8LLEtMstMvkvCclr8yyAjJ1G"

# Two sets of data to score, so we get two results back
data = {
  "Inputs": {
    "data": [
      {
        "dataType": "example_value",
        "dataSubtype": "example_value",
        "dateTime": "2000-01-01T00:00:00.000Z",
        "category": "example_value",
        "subcategory": "example_value",
        "status": "example_value",
        "address": "example_value",
        "latitude": 0,
        "longitude": 0,
        "extendedProperties": "example_value"
      }
    ]
  },
  "GlobalParameters": {
    "method": "predict"
  }
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())

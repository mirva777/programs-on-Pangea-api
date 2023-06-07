import requests

# Set your Pangea API credentials
access_key = "YOUR_ACCESS_KEY"
secret_key = "YOUR_SECRET_KEY"

# Create the request headers
headers = {
    "X-Pangea-Access-Key": access_key,
    "X-Pangea-Secret-Key": secret_key,
}

# Make the request to the Pangea API
url = "https://api.pangea.cloud/v1/users"
response = requests.post(url, headers=headers)

# Check the response status code
if response.status_code == 201:
    # The request was successful, print the user ID
    user_id = response.json()["id"]
    print(f"User created with ID {user_id}")
else:
    # The request failed, print the error message
    print(response.json()["error"])

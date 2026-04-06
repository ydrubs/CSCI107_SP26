"""
Exercise 2.1 - API Calls

Go to the API directory on the API Ninja website (make sure you have an account and API key)

    https://api-ninjas.com/api

    Step 1: Choose an API that seems interesting from API Ninja

    STEP 2: Use the code template below and fill in the api_url based on the documentation of your chosen API
            and what you learned in class. Make sure to structure the URL to return the parameters you want.
            Also, make sure you use your API key to return a successful result.

    STEP 3: Parse the return to only display the data you want

    STEP 3: Remove the API key in the code for security, then turn it in.

"""
import requests
import json


# --- PRACTICE -- MODIFY THE URL BELOW
# --- Structure and make a few of your own API calls below by modifying the api_url
api_url_1 = pass
api_url_2 = pass
api_url_3 = pass


response = requests.get(api_url_1, headers={'X-Api-Key': 'YOUR KEY HERE'}) #Replace with YOUR OWN API key


if response.status_code == requests.codes.ok:
    json_data = json.loads(response.text)  # Use JSON to convert data to a Python list

else:
    print("Error:", response.status_code, response.text) #...or if an error occurs, return error code

print(json_data)

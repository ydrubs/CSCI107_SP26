"""
In this lesson we look at how to use API key's in order to get a response

API keys are used to do things like:
    1) Validate a user
    2) Enforce limits on number of server calls
    3) Decide how to respond
    4) Charge money (if implemented)

When we send an API request, the server resieves the URL we request along with an API key.
The API key is then validated (or not) and a response is given back.
"""

"""
Example 4

In the following example, we use the APIninja website to request and parse a quote using an API key.
We need an API key in order to get back a successful response

We can see how to structure an API call from the API ninja tutorial here:
    https://api-ninjas.com/examples/basic-web-app
    
In this example format the URL to add the data that we want (category for the quote)
and send it to the server along with our API key

"""
# import requests
# import json


# --- From the documentation we see we can (optionally) specifiy a category
# categories = ["wisdom", "philosophy", "life", "truth", "inspirational", "relationships",
#         "love", "faith", "humor", "success", "courage", "happiness", "art", "writing",
#         "fear", "nature", "time", "freedom", "death", "leadership"]


pass # Get the index of the category to pass into the URL

# --- # Make the API call as per the documentation
# api_url = 'https://api.api-ninjas.com/v2/randomquotes?categories={}'......PASS......

# --- Make sure to paste the correct key provided to you by the website!
# response = requests.get(api_url, headers={'X-Api-Key': 'YOUR KEY HERE'}) #Replace with YOUR OWN API key


# if response.status_code == requests.codes.ok:
#     json_data = json.loads(response.text)  # Use JSON to convert data to a Python list
#
# else:
#     print("Error:", response.status_code, response.text) #...or if an error occurs, return error code
#
# print(json_data)


# --- Your TASK: Use the json_data to parse and display just the quote like we did in the previous lesson



"""
Example 5 Structuring an API call

    Let's take a look at the documentation for the API Ninja S&P500 API:

        - https://api-ninjas.com/api/sp500

    We can see the general endpoint structure like this: 

        - https://api.api-ninjas.com/v1/sp500?

    We can then add the parameters that we desire: 

        Examples:
        # Single parameter

            https://api.api-ninjas.com/v1/sp500?ticker=AAPL

        # Multiple parameters

            https://api.api-ninjas.com/v1/sp500?sector=Energy&limit=5


    Important:
        - Do NOT use multiple '?' characters.
          Incorrect: ?limit=1?sector=Energy
          Correct:   ?limit=1&sector=Energy

        - Sector values must match API-expected strings exactly (case-sensitive).

    Authentication:
        - Requires header: 'X-Api-Key': YOUR_API_KEY

"""
# import requests
# import json
#
# # --- PRACTICE
# # --- Structure and make a few of your own API calls below by modifying the api_url
# api_url = "https://api.api-ninjas.com/v1/sp500?"
#
#
# response = requests.get(api_url, headers={
#     'X-Api-Key': 'YOUR KEY HERE'})  # Replace YOUR OWN API key
#
# if response.status_code == requests.codes.ok:
#     json_data = json.loads(response.text)  # Use JSON to convert data to a Python list
#
# else:
#     print("Error:", response.status_code, response.text)  # ...or if an error occurs, return error code
#
# print(json_data)



"""
Example 6

In this example we use NASA's astronomy picture of the day to display an image
for the date specific.

We can see the structure of the API call from the website: https://api.nasa.gov/

In this case the query parameters are passed with the request
"""
import requests
import json

url = 'https://api.nasa.gov/planetary/apod'

# api_key = 'DEMO_KEY' #Replace with YOUR KEY to run (Demo_key has limited API calls)
# api_key = 'PASTE YOUR KEY HERE'
date = 'YYYY-MM-DD'

# querystring = {'api_key': api_key, 'date': date}

# In the previous examples, we directly called the 'get' request through a method. Here, we specify the type of request when making the API call.
pass

# if response.status_code == requests.codes.ok:
#     response = json.loads(response.text)
# else:
#     print("Error:", response.status_code, response.text)  # ...or if an error occurs, return error code
#
# print(response)



# --- After examining the data in the response and understanding its type, we want to pull out the image linked in the response and display it.


# --- We will open a web browser to show the image. We can also design a GUI with Tkinter or another library to display the image there instead.


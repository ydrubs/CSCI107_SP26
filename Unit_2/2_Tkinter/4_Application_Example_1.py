# --- import necessary packages
pass


#Define Root window
pass



#Define fonts and colors
root_color = '#FEFAE0'
quad1_color = '#90A583'
quad2_color = '#9D8420'
quad3_color = '#94B9AF'


#Functions
# def get_quote():
#     """
#     We copy and paste this from the API call lesson. We don't need to change anything in terms of how
#     the quote is returned
#
#     We only need to add a line to impose the text that gets returned to the label in quadrent 3
#     using quote.congif()
#     """
#     categories = ["wisdom", "philosophy", "life", "truth", "inspirational", "relationships",
#                   "love", "faith", "humor", "success", "courage", "happiness", "art", "writing",
#                   "fear", "nature", "time", "freedom", "death", "leadership"]
#
#     category = random.choice(categories)
#     api_url = 'https://api.api-ninjas.com/v2/randomquotes?categories={}'.format(category)
#     response = requests.get(api_url, headers={'X-Api-Key': 'XV998L7AgFsNM5BqkHJfHQ==bzm6P81GbHpGuflR'})
#
#     if response.status_code == requests.codes.ok:
#         json_data = json.loads(response.text)  # Use JSON to convert data to a Python list
#
#         quote_text = json_data[0]['quote'] # Thos parses the response to include just the quote
#         print(quote_text)
#
#         # --- Sets the content of label (text_place_holder) defined below to the text stored in quote_text
#         pass
#
#     else:
#         print("Error:", response.status_code, response.text)


# def get_fact():
#     """
#     This is another API that returns a random fact from API ninja
#
#     The call to the API only needs a website - no extra parameters: https://api-ninjas.com/api/facts#v1-facts
#
#     We use json to parse just as we did before
#     """
#     api_url = "https://api.api-ninjas.com/v1/facts"
#
#     response = requests.get(
#         api_url,
#         headers={"X-Api-Key": "XV998L7AgFsNM5BqkHJfHQ==bzm6P81GbHpGuflR"}
#     )
#
#     if response.status_code == requests.codes.ok:
#         json_data = response.json()   # convert response to Python list
#
#         fact = json_data[0]["fact"]   # extract fact from list
#
#         # --- As in the previous function, we set the text stored in the fact variable above to the label we created
#         pass
#
#     else:
#         print("Error:", response.status_code, response.text)

# Create a frame that will hold the other frames (optional but better control of background window)
pass

# --- Top left quadrant
pass

# --- Top right quadrant
pass

# --- Bottom section
pass

# Keep all the frames from resizing around widgets
pass

# --- Buttons to call API and process response
pass

# --- Label to display text that is generated
pass


#Run main window
# root.mainloop()




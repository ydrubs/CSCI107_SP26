# --- import necessary packages
import tkinter as tk
import json
import requests
import random


#Define Root window
root = tk.Tk()
root.title("Layout Experiment 1")
height = '475'
width = '475'
root.geometry(height + 'x' + width)
root.resizable()



#Define fonts and colors
root_color = '#FEFAE0'
quad1_color = '#90A583'
quad2_color = '#9D8420'
quad3_color = '#94B9AF'


#Functions
def get_quote():
    """
    We copy and paste this from the API call lesson. We don't need to change anything in terms of how
    the quote is returned

    We only need to add a line to impose the text that gets returned to the label in quadrent 3
    using quote.congif()
    """
    categories = ["wisdom", "philosophy", "life", "truth", "inspirational", "relationships",
                  "love", "faith", "humor", "success", "courage", "happiness", "art", "writing",
                  "fear", "nature", "time", "freedom", "death", "leadership"]

    category = random.choice(categories)
    api_url = 'https://api.api-ninjas.com/v2/randomquotes?categories={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': 'XV998L7AgFsNM5BqkHJfHQ==bzm6P81GbHpGuflR'})

    if response.status_code == requests.codes.ok:
        json_data = json.loads(response.text)  # Use JSON to convert data to a Python list

        quote_text = json_data[0]['quote'] # Thos parses the response to include just the quote
        print(quote_text)

        # --- Sets the content of label (text_place_holder) defined below to the text stored in quote_text
        text_place_holder.config(text=quote_text, font=('Engravers MT', 12), wraplength=430)

    else:
        print("Error:", response.status_code, response.text)


def get_fact():
    """
    This is another API that returns a random fact from API ninja

    The call to the API only needs a website - no extra parameters: https://api-ninjas.com/api/facts#v1-facts

    We use json to parse just as we did before
    """
    api_url = "https://api.api-ninjas.com/v1/facts"

    response = requests.get(
        api_url,
        headers={"X-Api-Key": "XV998L7AgFsNM5BqkHJfHQ==bzm6P81GbHpGuflR"}
    )

    if response.status_code == requests.codes.ok:
        json_data = response.json()   # convert response to Python list

        fact = json_data[0]["fact"]   # extract fact from list

        # --- As in the previous function, we set the text stored in the fact variable above to the label we created
        text_place_holder.config(text=fact, font=('Engravers MT', 12), wraplength=430)

    else:
        print("Error:", response.status_code, response.text)

# Create a frame that will hold the other frames (optional but better control of background window)
wrapper_frame = tk.Frame(root, height='200', width='200', bg=root_color)
wrapper_frame.pack()

# --- Top left quadrant
quad1 = tk.Frame(wrapper_frame, bg=quad1_color, height=int(height)/2.25, width=int(width)/2.25)
quad1.grid(row=0, column=0, padx=5, pady=5)

# --- Top right quadrant
quad2 = tk.Frame(wrapper_frame, bg=quad2_color, height=int(height)/2.25, width=int(width)/2.25)
quad2.grid(row=0, column=1, padx=5, pady=5)

# --- Bottom section
quad3 = tk.Frame(wrapper_frame, height=int(height)/2, width=int(width)-40, bg=quad3_color)
quad3.grid(row=1, column=0, padx=5, pady=5, columnspan=2)

# Keep all the frames from resizing around widgets
quad1.pack_propagate(False)
quad2.pack_propagate(False)
quad3.pack_propagate(False)

# --- Buttons to call API and process response
tk.Button(quad1, text='Get Quote', font=('Arial', 12), command=get_quote).pack(pady=60)
tk.Button(quad2, text='Get Random Fact', font=('Arial', 12), command=get_fact).pack(pady=60)

# --- Label to display text that is generated
text_place_holder = tk.Label(quad3, bg=quad3_color)
text_place_holder.pack(ipady=60, expand=True)


#Run main window
root.mainloop()




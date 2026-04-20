import tkinter as tk

root = tk.Tk() # Create a simple root window
root.title("Button demo")


# =========================
# ALL BUTTON BEHAVIOR EXAMPLE
# =========================
def on_click():
    print("Button clicked!")

button = tk.Button(
    root,

    # --- Text & Command
    text="Click Me",
    command=on_click,

    # --- Font & Colors
    font=("Arial", 14, "bold"),
    fg="white",  # text color
    bg="blue",  # background color
    activeforeground="yellow",  # text color when clicked
    activebackground="red",  # background when clicked

    # --- Size & Padding
    width=15,  # width in text units
    height=2,  # height in text units
    padx=10,  # internal horizontal padding
    pady=5,  # internal vertical padding

    # --- Border & Style
    bd=3,  # border width
    relief="raised",  # border style (flat, raised, sunken, ridge, groove)

    # --- Alignment
    anchor="center",  # position of text inside button

    # --- State
    state="normal",  # normal, disabled

    # --- Cursor
    cursor="hand2",  # mouse cursor on hover

    # --- Wrap text
    wraplength=150  # wrap long text
)

button.pack(pady=20)

################################################################################################################
# Basic Button
pass
# button1.pack()


# --- Button with Callback Command
# --- A callback command triggers a function defined by 'command' when the button is pressed

pass

pass
# button2.pack()

# Button with Font Styling
pass
# button3.pack()

# Button with Background and Foreground Colors
pass
# button4.pack()

# Button with Padding
# button5 = tk.Button(root, text="Button with Padding", padx=10, pady=10)
# button5.pack()

################################################################################################################
"""Entry Boxes"""

# Basic Entry Box
pass
# entry1.pack()

# Entry with Default Text
pass
# entry2.pack()

# Entry with Font Styling
# entry3 = tk.Entry(root, font=("Arial", 20, "bold"))
# entry3.pack()

# Entry with Background and Foreground Colors
# entry4 = tk.Entry(root, bg="yellow", fg="red")
# entry4.pack()

# Entry with Width Specified
# entry5 = tk.Entry(root, width=50)
# entry5.pack()

"""Password entry box"""
# Password prompt frame
pass

# Password label
pass

# Password entry box
pass


pass

# Submit button
# submit_button = tk.Button(password_frame, text="Submit", command=submit_password)

"""
- use columnspan to make a widget span across multiple columns in the grid

- use sticky to control how the widget stretches and aligns within its grid cell
  (e.g., 'n', 's', 'e', 'w', 'ns', 'ew', 'nsew')
  'ew' means it will stretch in the left-right direction across both columns
"""
pass


################################################################################################################
"""
Radio Buttons (Radiobutton)

Radiobuttons allow the user to select ONE option from a group.

To make multiple radiobuttons work together, they must share the same
variable. In Tkinter, we use a special variable type such as tk.IntVar()
to store the selected value.

- tk.IntVar():
    Stores the value of the selected option

- variable:
    Links each radiobutton to the shared variable

- value:
    The number assigned to each option (what gets stored when selected)
    
- command:
    The function that triggers when the radio button is selected

Key Idea:
    When a radiobutton is selected, its value is stored in the IntVar.
    We can then use .get() to retrieve that value and act on it.
"""
pass


root.mainloop()
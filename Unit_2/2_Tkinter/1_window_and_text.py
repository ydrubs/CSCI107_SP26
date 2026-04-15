import tkinter as tk

# --- Some text we will use in our code
t1 = 'We set sail on this new sea because there is new knowledge to be gained'
t2 = 'Its conquest deserves the best of all mankind'
t3 = 'We choose to go to the moon.'
t4 = 'We choose to go to the moon in this decade and do the other things'
t5 = "Well, space is there, and we're going to climb it"


"""
Create and configure the main application window (root window) using Tkinter.

The root window is the primary window of a Tkinter GUI application. It acts as
the container for all other widgets (buttons, labels, frames, etc.) and must be
created before adding any GUI components.

--------------------------------------------------------------------------------

When you call tk.Tk(), Python creates an instance of the Tk class, which:
- Initializes the underlying Tcl/Tk interpreter (the engine that runs the GUI)
- Creates the main window that appears on the screen
- Acts as the parent (container) for all widgets in the application

Only one root window should be created per application. Additional windows,
if needed, are created using Toplevel instead.

All widgets (buttons, labels, frames, etc.) are typically placed inside this
root window or within containers that belong to it.
"""

pass #Define the root window
pass #Give the window screen a title

# --- Set the size of the window
# --- We can use addition for the x,y offset to determine the location of the window when the application is run
pass

pass #Don't allow window resizing (default is 1,1)

#Limit resize dimensions if resizing allowed
pass


color1 = 'teal' # Use color definitions: https://cs111.wellesley.edu/archive/cs111_fall14/public_html/labs/lab12/tkintercolor.html
color2 = '#11AABB' # Use a Hex Value #RRGGBB
pass # Define root window color

"""
Note:
There are many additional methods available for customizing the root window.
Try researching (or asking AI about) methods such as:
- attributes()
- iconbitmap()
- lift()

Experiment with them to see how they change the window behavior.
"""

##########################################################################################

"""
Create and display Label widgets in a Tkinter GUI.

A Label is a widget used to display text or images on the screen. Labels are
non-interactive, meaning they are typically used for showing information rather
than receiving user input.

Each Label must have a parent container (in this case, the root window) and can
be customized with various options such as:
    - text: the string displayed in the label
    - font: controls the font type, size, and style (e.g., bold)
    - bg (background): sets the background color of the label
    - fg (foreground): sets the text color

Labels are positioned in the window using a geometry manager such as pack().
The pack() method places widgets in the next available space and can be adjusted
with additional options:
    - pady / padx: external spacing around the widget
    - ipady / ipadx: internal spacing inside the widget
    - anchor: aligns the widget within its allocated space (e.g., 'w' for left)
    - fill: allows the widget to expand in a direction ('x', 'y', or 'both')

This example demonstrates how to create multiple labels with different styling
options and layout configurations.
"""

##Create text widgets(labels)
pass #Create a text widget in the root window
pass # Place widget in the window using the pack layout manager

pass
pass #give it top and bottom padding

pass #Change font, font-size, bold, and color
pass

pass
pass #Add only padding, below, add internal padding (inside the text widget), align-left

pass
pass #Fill up all widget space in x-direction add some padding


"""
Common Label Parameters (Tkinter)

Text & Appearance:
------------------
text:
    The text displayed on the label.

font:
    Defines the font type, size, and style.
    Format: (font_name, size, style)
    Example: ("Arial", 14, "bold")

fg (foreground):
    The color of the text.

bg (background):
    The background color of the label.


Spacing & Layout:
------------------
padx, pady:
    External padding (space outside the widget).

ipadx, ipady:
    Internal padding (space inside the widget).


Borders:
------------------
bd or borderwidth:
    Width of the border.

relief:
    Style of the border.
    Options: FLAT, RAISED, SUNKEN, RIDGE, GROOVE, SOLID


Text Positioning:
------------------
anchor:
    Position of text inside the label.
    Options: N, NE, E, SE, S, SW, W, NW, CENTER

justify:
    Alignment of multi-line text.
    Options: LEFT, RIGHT, CENTER

wraplength:
    Maximum line width (in pixels) before text wraps to the next line.
"""

label = tk.Label(root,
                 text="Hello, Tkinter!",
                 font=("Arial", 20, "bold"),
                 bg="yellow",
                 fg="red",
                 padx=10,
                 pady=10,
                 relief="solid",
                 bd=2,
                 anchor="nw",
                 justify="center",
                 wraplength=100)
label.pack()

##########################################################################################
"""
Start the Tkinter event loop.

The mainloop() method tells the program to begin listening for events such as
button clicks, key presses, and window updates. It keeps the GUI running and
responsive to user interaction.

Once mainloop() is called:
- The window is displayed on the screen
- The program waits for user input (events)
- The GUI continues running until the window is closed



This should be the last line of a Tkinter program, as it blocks further code
execution until the application is exited.
"""
pass



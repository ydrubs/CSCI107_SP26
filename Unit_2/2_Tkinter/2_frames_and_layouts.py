import tkinter as tk

root = tk.Tk()
root.geometry('500x500')  # Set the size of the root window



# --- color pallete (https://coolors.co)
color1 = '#F7F7F2'
color2 = '#E4E6C3'
color3 = '#899878'
color4 = '#222725'
color5 = '#121113'

"""
Parameters:

- side='left' → positions the widget on the left side of its parent container
- fill='y' → allows the widget to expand vertically (top to bottom) to fill available space
"""
# --- Sidebar
sidebar = tk.Frame(root, width=80, bg=color3)
sidebar.pack(side='left', fill='y')


"""
Parameters:

-  fill='both' → allows the widget to expand horizontally AND vertically to fill available space
-  expand=True → allows the widget to grow and take up extra space if the window is resized
"""
# --- Main frame
main_frame = tk.Frame(root, bg=color5)
main_frame.pack(fill='both', expand=True)


"""
NOTE:
The order of pack() matters.

If main_frame is packed BEFORE the sidebar, it will take up all available space first.
This leaves no room for the sidebar, causing it to appear compressed or not visible.

This happens because:
- fill='both' allows the widget to take up available space
- expand=True allows it to claim extra space

Widgets packed later only get the remaining space.
"""
frame1 = tk.Frame(main_frame, bg=color1, width=200, height=200)
frame1.grid(row=0, column=0)

frame2 = tk.Frame(main_frame, bg=color2, width=200, height=200)
frame2.grid(row=0, column=1)



frame3 = tk.Frame(main_frame, bg=color4, width=200, height=200)
frame3.grid(row=1, column=1, sticky='ns')

# Create a sidebar for frame 4
frame4 = tk.Frame(main_frame, bg='blue') # We don't need to specify width because of the sticky parameter (see below)
frame4.grid(row=1, column=0, sticky='nsew')

#Create a footer that spans across both columns
frame5 = tk.Frame(main_frame, bg='tan', height=50)
frame5.grid(row=2, column=0, columnspan=2, sticky='ew')

"""
Grid Behavior: sticky and rowconfigure

sticky:
    Controls how a widget stretches inside its grid cell.
    - 'n' → top
    - 's' → bottom
    - 'ns' → fill vertically (top to bottom)
    - 'ew' → fill horizontally (left to right)
    - 'nsew' → fill entire cell

rowconfigure(weight):
    Controls how extra space is distributed in the grid.

    - weight=0 (default) → row does not grow
    - weight=1 → row can grow and take extra space

Key Idea:
    - sticky controls how the widget stretches
    - weight controls whether the row/column can grow

Both are needed for a widget to fully expand.
"""
main_frame.grid_rowconfigure(1, weight = 1)
# main_frame.grid_rowconfigure(0, weight=2) # Allow for a 2:1 ratio for rows a and 2


"""
Using Nested Frames and the place() Geometry Manager

This example demonstrates how frames can be placed inside other frames
(nested layout) and positioned precisely using the place() method.

Nested Frames:
    Each child_frame is created inside a parent frame (frame1, frame2, frame3).
    This allows you to organize a GUI into sections and sub-sections.

place() Geometry Manager:
    The place() method positions widgets using relative coordinates
    within the parent container.

Parameters:

- relx:
    Horizontal position as a fraction of the parent (0.0 = left, 1.0 = right)

- rely:
    Vertical position as a fraction of the parent (0.0 = top, 1.0 = bottom)

- anchor (default = 'nw'):
    Determines which part of the widget is placed at the (relx, rely) position

    Common options:
    - 'nw' → top-left corner (default)
    - 'center' → center of the widget

Key Idea:
    relx and rely define WHERE the widget is placed
    anchor defines WHICH PART of the widget is placed at that position

    Changing the anchor can cause parts of the widget to move or even
    extend outside the visible area of the parent.
"""
child_frame = tk.Frame(frame1, bg='grey', width=50, height=50)
child_frame.place(relx=0, rely=0)

child_frame2 = tk.Frame(frame2, bg='white', width=50, height=50)
child_frame2.place(relx=0.5, rely=0.5, anchor='center')

child_frame3 = tk.Frame(frame3, bg='white', width=50, height=50)
child_frame3.place(relx=0.5, rely=0, relwidth=0.1, relheight=0.5)

# --- Create a sidebar for frame 4
child_frame4 = tk.Frame(frame4, bg='red', width=40, height=30)
child_frame4.pack(side='right', fill='y')


# --- Create text widgets inside frames
text_frame1 = tk.Label(frame1, text='hi')
text_frame1.place(relx=0.5, rely=0.5, anchor='center')


"""
pack_propagate() with pack()

By default, a frame using pack() resizes to fit its contents.

pack_propagate(False):
    Keeps the frame at its specified width and height,
    ignoring the size of its child widgets.

Key Idea:
    pack() controls widget placement
    pack_propagate() controls whether the frame resizes to fit its contents
    
Observe: If we comment out the pack_propagate command below we will see that the child frame 
         gets resized to fit the text. 
"""

# --- Example of creating a label nested inside a child frame
text_child_frame1 = tk.Label(child_frame, text="Hi", fg='black', bg="pink")
text_child_frame1.pack(padx=5, pady=5)
child_frame.pack_propagate(False) # Try commenting this out to see the difference


"""
Student Challenge 
    Use grid to create 4 equal sized squares inside of child_frame2 (see image on whiteboard of what this should look like)
"""
tk.Label(frame2, text ='some text').place(relx=0.5, rely=0.25, anchor='center')

inner_child_frame2_1 = tk.Frame(child_frame2, bg='yellow', height=20, width=20)
inner_child_frame2_1.grid(row=0, column=0)

inner_child_frame2_2 = tk.Frame(child_frame2, bg='green', height=20, width=20)
inner_child_frame2_2.grid(row=1, column=0)


root.mainloop()


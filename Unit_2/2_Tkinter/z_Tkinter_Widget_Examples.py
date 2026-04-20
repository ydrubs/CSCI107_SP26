import tkinter as tk

root = tk.Tk()
root.title("Tkinter Widget Grid Demo")
root.geometry("800x600")

# ==================================================
# MAIN FRAME
# ==================================================
main_frame = tk.Frame(root)
main_frame.pack(fill="both", expand=True)

# --- Make the 4x2 grid expand evenly
for r in range(4):
    main_frame.grid_rowconfigure(r, weight=1)

for c in range(2):
    main_frame.grid_columnconfigure(c, weight=1)

# ==================================================
# FRAME 1 - LABEL
# ==================================================
frame1 = tk.Frame(main_frame, bg="lightblue", bd=2, relief="solid")
frame1.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)

tk.Label(frame1, text="This is a Label", font=("Arial", 14, "bold"),
         bg="lightblue").place(relx=0.5, rely=0.5, anchor="center")

# ==================================================
# FRAME 2 - BUTTON
# ==================================================
frame2 = tk.Frame(main_frame, bg="lightgreen", bd=2, relief="solid")
frame2.grid(row=0, column=1, sticky="nsew", padx=5, pady=5)

tk.Button(frame2, text="Click Me").place(relx=0.5, rely=0.5, anchor="center")

# ==================================================
# FRAME 3 - ENTRY
# ==================================================
frame3 = tk.Frame(main_frame, bg="lightyellow", bd=2, relief="solid")
frame3.grid(row=1, column=0, sticky="nsew", padx=5, pady=5)

tk.Entry(frame3, width=20).place(relx=0.5, rely=0.5, anchor="center")

# ==================================================
# FRAME 4 - CHECKBUTTON
# ==================================================
frame4 = tk.Frame(main_frame, bg="lightpink", bd=2, relief="solid")
frame4.grid(row=1, column=1, sticky="nsew", padx=5, pady=5)

check_var = tk.IntVar()
tk.Checkbutton(frame4, text="Check Me", variable=check_var,
               bg="lightpink").place(relx=0.5, rely=0.5, anchor="center")

# ==================================================
# FRAME 5 - RADIOBUTTONS
# ==================================================
frame5 = tk.Frame(main_frame, bg="lavender", bd=2, relief="solid")
frame5.grid(row=2, column=0, sticky="nsew", padx=5, pady=5)

radio_var = tk.IntVar()

radio_container = tk.Frame(frame5, bg="lavender")
radio_container.place(relx=0.5, rely=0.5, anchor="center")

tk.Radiobutton(radio_container, text="Option 1", variable=radio_var,
               value=1, bg="lavender").pack(anchor="w")
tk.Radiobutton(radio_container, text="Option 2", variable=radio_var,
               value=2, bg="lavender").pack(anchor="w")

# ==================================================
# FRAME 6 - OPTION MENU
# ==================================================
frame6 = tk.Frame(main_frame, bg="peachpuff", bd=2, relief="solid")
frame6.grid(row=2, column=1, sticky="nsew", padx=5, pady=5)

menu_var = tk.StringVar(value="Choose")

tk.OptionMenu(frame6, menu_var, "Choice 1", "Choice 2", "Choice 3")\
    .place(relx=0.5, rely=0.5, anchor="center")

# ==================================================
# FRAME 7 - SCALE
# ==================================================
frame7 = tk.Frame(main_frame, bg="lightcoral", bd=2, relief="solid")
frame7.grid(row=3, column=0, sticky="nsew", padx=5, pady=5)

tk.Scale(frame7, from_=0, to=100, orient="horizontal",
         bg="lightcoral").place(relx=0.5, rely=0.5, anchor="center")

# ==================================================
# FRAME 8 - LISTBOX (REVISED)
# ==================================================
frame8 = tk.Frame(main_frame, bg="lightcyan", bd=2, relief="solid")
frame8.grid(row=3, column=1, sticky="nsew", padx=5, pady=5)

listbox = tk.Listbox(frame8, height=6, width=20)
listbox.place(relx=0.5, rely=0.5, anchor="center")

# Add items
for item in ["Item 1", "Item 2", "Item 3", "Item 4"]:
    listbox.insert(tk.END, item)

root.mainloop()
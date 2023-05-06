import tkinter as tk
#from tkinter import ttk
import ttkbootstrap as ttk

# main window
window = ttk.Window(themename = "superhero")
window.geometry("600x400")
window.title("A Coffee Machine")

# frame
frame = ttk.Frame(window)
frame.pack()

# Frame1 widgets
widget_frame = ttk.LabelFrame(frame, text = "Choose Your Drink",)
widget_frame.grid(row=0, column=0, padx=20, pady=10)

# Choose drink
drink_type = ["Americano", "Esspresso", "Latte", "Cappucino"]

drink_name = ttk.Combobox(widget_frame, values=drink_type,)
drink_name.current(0)
drink_name.grid(row=1, column=0, sticky="ew", padx=5, pady=(0, 5))

# Number of Drinks
num_of_drinks_spinbox = ttk.Spinbox(widget_frame, from_=1, to=10, )
num_of_drinks_spinbox.grid(row=2,column=0, sticky="ew", padx=5, pady=5)
num_of_drinks_spinbox.insert(0, "How many drinks?")
num_of_drinks_spinbox.bind("<FocusIn>", lambda clear: num_of_drinks_spinbox.delete("0", "end"))


# How do you like it?
drink_temp = ["Hot", "Kinda Warm", "Warm"]

temp = ttk.Combobox(widget_frame, values=drink_temp)
temp.current(0)
temp.grid(row=3, column=0, sticky="ew", padx=5, pady=5)

# Separater
separater = ttk.Separator(widget_frame)
separater.grid(row=4, column=0, padx=(20,10), pady=10, sticky="ew")





# main window run
window.mainloop()
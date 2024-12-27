from tkinter import Tk, Label

# Create the main application window
root = Tk()

# Create a label widget with the text "Hello, World!"
label = Label(root, text="Hello, World!")

# Place the label in the window using the pack geometry manager
label.pack()

# Start the Tkinter event loop
root.mainloop()
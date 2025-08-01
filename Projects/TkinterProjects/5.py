import tkinter as tk

root = tk.Tk()
root.title("This is label")
root.geometry("700x700")

top_frame = tk.Frame(root)
top_frame.pack(fill=tk.X, padx=10, pady=5)

label = tk.Label(top_frame, text="This is a label")
label.pack(side=tk.LEFT)

button = tk.Button(top_frame, text="Click Me")
button.pack(side=tk.RIGHT)

input_field = tk.Entry(root)
input_field.pack(fill=tk.X, padx=10, pady=5)

textarea = tk.Text(root, height=5)
textarea.pack(fill=tk.X, padx=10, pady=5)

bottom_frame = tk.Frame(root)
bottom_frame.pack(fill=tk.X, padx=10, pady=5)

checkbox = tk.Checkbutton(bottom_frame, text="Check me")
checkbox.pack(side=tk.LEFT)

radio_frame = tk.Frame(bottom_frame)
radio_frame.pack(side=tk.RIGHT)

radio_btn1 = tk.Radiobutton(radio_frame, text="Option 1", value=1)
radio_btn1.pack(anchor=tk.W)

radio_btn2 = tk.Radiobutton(radio_frame, text="Option 2", value=2)
radio_btn2.pack(anchor=tk.W)

root.mainloop()
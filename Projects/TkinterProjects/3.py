import tkinter as tk

def on_click_button():
    label.config(text="Button clicked!")
    
root = tk.Tk()
root.title("Simple GUI with Button")

label = tk.Label(root, text="Hello, Tkinter!", font=("Arial", 14))
label.pack(pady=20)

button = tk.Button(root, text="Click Me", command=on_click_button)
button.pack(pady=10)

root.geometry("300x200")
root.mainloop()
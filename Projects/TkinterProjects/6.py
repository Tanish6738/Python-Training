import tkinter as tk

root = tk.Tk()
root.title("Fahrenheit to Celsius Converter")
root.geometry("400x250")

title_label = tk.Label(root, text="Temperature Converter", font=("Arial", 16, "bold"))
title_label.pack(pady=20)

input_label = tk.Label(root, text="Enter temperature in Fahrenheit:", font=("Arial", 10))
input_label.pack(pady=5)

fahrenheit_entry = tk.Entry(root, font=("Arial", 12), width=20)
fahrenheit_entry.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12, "bold"), fg="blue")
result_label.pack(pady=10)

error_label = tk.Label(root, text="", font=("Arial", 10), fg="red")
error_label.pack(pady=5)

def convert_temperature():
        error_label.config(text="")
        
        fahrenheit = float(fahrenheit_entry.get())
        
        celsius = (fahrenheit - 32) * 5/9
        
        result_label.config(text=f"{fahrenheit}°F = {celsius:.2f}°C")
        
convert_button = tk.Button(root, text="Convert to Celsius", command=convert_temperature, 
                          font=("Arial", 10), bg="lightblue")
convert_button.pack(pady=15)

root.bind('<Return>', lambda event: convert_temperature())

fahrenheit_entry.focus()

# Start the GUI event loop
root.mainloop()
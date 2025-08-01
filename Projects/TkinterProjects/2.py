import tkinter as tk

root = tk.Tk()

Frame_top = tk.Frame(root)
Frame_Bottom = tk.Frame(root)


Frame_top.pack(side=tk.TOP, fill=tk.BOTH, expand=True)
Frame_Bottom.pack(side=tk.BOTTOM, fill=tk.BOTH , expand=True)

label1 = tk.Label(Frame_top, text="label 1", bg="lightblue", font=("Arial", 14))
label2 = tk.Label(Frame_top, text="label 2", bg="lightblue", font=("Arial", 14))
label3 = tk.Label(Frame_Bottom, text="label 3", bg="lightblue", font=("Arial", 14))
label4 = tk.Label(Frame_Bottom, text="label 4", bg="lightblue", font=("Arial", 14))

label1.pack(side=tk.LEFT)
label2.pack(side=tk.RIGHT)
label3.grid(row=0, column=0)
label4.grid(row=0, column=1)


root.geometry("300x200")
root.title("Simple GUI with Frames")

root.mainloop()

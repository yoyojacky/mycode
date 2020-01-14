import Tkinter as tk
def mycommand():
    print("press me!")

root = tk.Tk()
w = tk.Button(root,bd=3, text="Setup", bg="red", fg="black", command=mycommand)
w.pack()

root.mainloop()

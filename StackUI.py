import tkinter as tk
from tkinter import messagebox
import os,ctypes
import webbrowser
from PIL import Image, ImageTk

dll_path = os.path.join(os.path.dirname(__file__), "Stack.dll")

try:
    sta = ctypes.CDLL(r"C:\Dfolder\Coding\StackUI\Stack.dll")
except OSError:
    messagebox.showerror("Error", "Stack.dll not found. Please ensure it's in the same directory.")
    exit()

sta.push.argtypes = [ctypes.c_int]
sta.push.restype = None

sta.pop.argtypes = []
sta.pop.restype = ctypes.c_int

sta.get_stack.argtypes = [ctypes.POINTER(ctypes.c_int)]
sta.get_stack.restype = ctypes.POINTER(ctypes.c_int)

scr = tk.Tk()
scr.title("Visual Representation of Stack")
scr.geometry("350x450")
scr.configure(bg="#343f3e")

entry = tk.Entry(scr, width=20)
entry.place(x=25, y=15)
entry.bind("<Return>", lambda event: Push())

stack_label = tk.Label(scr, text="Stack Contents:", bg="#343f3e", fg="white",font = ("Arial", 12,"bold"))
stack_label.place(x=18, y=100)

stack_display = tk.Text(scr, height=16, width=35, state=tk.DISABLED, bg="#505a5b", fg="#000000",font = ("Arial", 12,"bold"))
stack_display.place(x=20, y=125)

def update_display():
    size = ctypes.c_int(0)
    stack_ptr = sta.get_stack(ctypes.byref(size))

    stack_contents = []
    if size.value > 0:
        for i in range(size.value):
            stack_contents.append(stack_ptr[i])

    stack_display.configure(state=tk.NORMAL)
    stack_display.delete("1.0", tk.END)

    if stack_contents:
        display_text = "\n".join(map(str, reversed(stack_contents)))
        stack_display.insert(tk.END, display_text)
    else:
        stack_display.insert(tk.END, "Stack is empty.")

    stack_display.configure(state=tk.DISABLED)

def Push():
    value_str = entry.get()
    if value_str.isdigit():
        value = int(value_str)
        sta.push(value)
        update_display()
        entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Invalid Input", "Please enter a valid integer!")

def Pop():
    result = sta.pop()
    if result != -1:
        messagebox.showinfo("Action", f"Popped value: {result}")
        update_display()
    else:
        messagebox.showinfo("Action", "Stack underflow.")

def Clear():
    global sta
    while sta.pop() != -1:
        pass
    update_display()
    messagebox.showinfo("Action", "Stack cleared.")

def Web():
    webbrowser.open("https://dsa-visualizer-delta.vercel.app/visualizer/stack")

try:
    img = Image.open("C:/Dfolder/Coding/StackUI/w.png")
    rimg = img.resize((39,39))
    web_img = ImageTk.PhotoImage(rimg)
except FileNotFoundError:
    messagebox.showerror("Error", "w.png not found. Please check the file path.")
    web_img = None

push_button = tk.Button(scr, text="Push", command=Push, bg="#505a5b", fg="#ffffff", width=7, height=1,font = ("Arial", 10,"bold"))
push_button.place(x=90, y=45)

pop_button = tk.Button(scr, text="Pop", command=Pop, bg="#505a5b", fg="#ffffff", width=7, height=1,font = ("Arial", 10,"bold"))
pop_button.place(x=25, y=45)

clear_button = tk.Button(scr, text="Clear", command=Clear, bg="#ff0000", fg="#000000", width= 15, height=1,font = ("Arial", 10,"bold"))
clear_button.place(x=25, y=76)

if web_img:
    web_button = tk.Button(scr, image=web_img, command=Web, bg="#505a5b", width=40, height=27)
    web_button.place(x= 295, y= 6)
else:
    web_button = tk.Button(scr, text="Web", command=Web, bg="#505a5b", fg="#000000", width=40, height=25)
    web_button.place(x= 295, y= 6)

update_display()
scr.mainloop()
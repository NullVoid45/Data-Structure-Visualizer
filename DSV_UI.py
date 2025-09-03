import tkinter as tk
from tkinter import messagebox
import os,ctypes
import webbrowser
from PIL import Image, ImageTk

dll_path = os.path.join(os.path.dirname(__file__), "Stack.dll")

try:
    sta = ctypes.CDLL(r"C:\Dfolder\Coding\DataStructures\DSV.dll")
except OSError:
    messagebox.showerror("Error", "Stack.dll not found. Please ensure it's in the same directory.")
    exit()

def open_stack_visualizer(parent):
    sta.push.argtypes = [ctypes.c_int]
    sta.push.restype = ctypes.c_int 

    sta.pop.argtypes = []
    sta.pop.restype = ctypes.c_int

    sta.get_stack.argtypes = [ctypes.POINTER(ctypes.c_int)]
    sta.get_stack.restype = ctypes.POINTER(ctypes.c_int)

    scr = tk.Toplevel(parent)
    scr.title("Visual Representation of Stack")
    scr.geometry("350x450")
    scr.configure(bg="#343f3e")

    entry = tk.Entry(scr, width=20)
    entry.place(x=25, y=15)
    entry.bind("<Return>", lambda event: Push())

    stack_label = tk.Label(scr, text="Stack Contents:", bg="#343f3e", fg="white",font = ("Arial", 12,"bold"))
    stack_label.place(x=18, y=100)

    stack_display = tk.Text(scr, height=10, width=20, state=tk.DISABLED, bg="#505a5b", fg="#000000",font = ("Arial", 20,"bold"))
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
            result = sta.push(value)
            if result == -1:
                messagebox.showinfo("Action", "Stack Overflow")
            elif result == 0:
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
        img = Image.open("C:\Dfolder\Coding\DataStructures\w.png")
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
        web_button.image = web_img
        web_button.place(x= 295, y= 6)
    else:
        web_button = tk.Button(scr, text="Web", command=Web, bg="#505a5b", fg="#000000", width=40, height=25)
        web_button.place(x= 295, y= 6)

    update_display()

def open_queue_visualizer(root):
    print("\n")

def open_linkedlist_visualizer(root):
    print("\n")

def main_screen():
    root = tk.Tk()
    root.title("Data Structures Visualizer")
    root.geometry("500x600")
    root.configure(bg="#191919")
    
    label = tk.Label(root, text="Visualizers", bg="#36363f", fg="#fcfcf3", font=("Arial", 38, "bold"))
    label.pack(pady=40)

    Stack_button = tk.Button(root,text="Stack Visualizer", command= lambda: open_stack_visualizer(root),bg="#505a5b", width = 19, height = 3,fg="#ffffff",font=("Arial", 13, "bold"))
    Stack_button.pack(pady=20)
    
    Queue_button = tk.Button(root,text ="Queue Visualizer", command = lambda: open_queue_visualizer(root),bg="#505a5b", width = 19, height = 3,fg="#ffffff",font=("Arial", 13, "bold"))
    Queue_button.pack(pady=20)
    
    Linkedlist_button = tk.Button(root,text="Linked List Visualizer", command = lambda: open_linkedlist_visualizer(root),bg="#505a5b", width = 19, height = 3,fg="#ffffff",font=("Arial", 13, "bold"))
    Linkedlist_button.pack(pady=20)    
    root.mainloop()

if __name__ == "__main__":
    main_screen()
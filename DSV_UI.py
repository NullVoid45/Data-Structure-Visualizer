import tkinter as tk
from tkinter import messagebox
import os,ctypes
import webbrowser
from PIL import Image, ImageTk

try:
    dll_path = os.path.join(os.path.dirname(__file__), "DSV.dll")
    c = ctypes.CDLL(dll_path)
except OSError:
    messagebox.showerror("⚠️Error", "DSV.dll not found. Please ensure it's in the same directory.")
    exit()

def open_stack_visualizer(parent):
    c.push.argtypes = [ctypes.c_int]
    c.push.restype = ctypes.c_int 

    c.pop.argtypes = []
    c.pop.restype = ctypes.c_int

    c.get_stack.argtypes = [ctypes.POINTER(ctypes.c_int)]
    c.get_stack.restype = ctypes.POINTER(ctypes.c_int)

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
        stack_ptr = c.get_stack(ctypes.byref(size))

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
            result = c.push(value)
            if result == -1:
                messagebox.showinfo("Action", "Stack Overflow")
            elif result == 0:
                update_display()
                entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Invalid Input", "Please enter a valid integer!")

    def Pop():
        result = c.pop()
        if result != -1:
            messagebox.showinfo("Action", f"Popped value: {result}")
            update_display()
        else:
            messagebox.showinfo("Action", "Stack underflow.")

    def Clear():
        #global c
        while c.pop() != -1:
            pass
        update_display()
        messagebox.showinfo("Action", "Stack cleared.")

    def Web():
        webbrowser.open("https://dsa-visualizer-delta.vercel.app/visualizer/stack")

    try:
        img_path = os.path.join(os.path.dirname(__file__), "w.png")
        img = Image.open(img_path)
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

def open_queue_visualizer(parent):
    messagebox.showinfo("⚠️Caution", "Work in progress.")
    pass

def open_linkedlist_visualizer(parent):
    
    messagebox.showinfo("⚠️Caution", "Work in progress.")
    
    c.SLL_ins_beg.argtypes = [ctypes.c_int]
    c.SLL_ins_beg.restype = ctypes.c_int

    c.SLL_ins_end.argtypes = [ctypes.c_int]
    c.SLL_ins_end.restype = ctypes.c_int 

    c.SLL_ins_pos.argtypes = [ctypes.c_int]
    c.SLL_ins_pos.restype = ctypes.c_int
    
    c.SLL_del_beg.argtypes = []
    c.SLL_del_beg.restype = ctypes.c_int
    
    c.SLL_del_end.argtypes = []
    c.SLL_del_end.restype = ctypes.c_int

    c.SLL_del_pos.argtypes = [ctypes.c_int]
    c.SLL_del_pos.restype = ctypes.c_int
    
    LLscr = tk.Toplevel(parent)
    LLscr.title("Visual Representation of Linked List")
    LLscr.geometry("800x600")
    LLscr.configure(bg="#343f3e")
    
    entryLL = tk.Entry(LLscr, width=20, font = ("Arial",15))
    entryLL.place(x = 0, y = 60)
    entryLL.bind("<Return>", lambda event: INSERT())

    def button_color(x):
        L = [SLL_button,DLL_button,CLL_button]
        if x in L:
            x.config(bg = "#06cf0d",fg = "#000000")
            L.remove(x)
            L[0].config(bg = "#505a5b",fg = "#FFFFFF")
            L[1].config(bg = "#505a5b",fg = "#FFFFFF")
        return x

    def SLL():
        button_color(SLL_button)
        value_str = entryLL.get()
        pos_str = entryLL.get() # add the fecility to get pos from entryLL
        if value_str.isdigit():
            value = int(value_str)
            mode = Insert_paradigm_var.get()

            if mode == "Beginning":
                result = c.SLL_ins_beg(value)
                # add update_display()

            elif mode == "Position":
                if pos_str.isdigit():
                    pos = int(pos_str)
                    result = c.SLL_ins_pos(value, pos)
                    if result == 1:
                        messagebox.showinfo("Action", f"Inserted {value} at position {pos}") #later change remove this and just put update_display()

            else:
                result = c.SLL_ins_end(value)
                # add update_display()

            try:
                messagebox.showinfo("Action", f"Inserted (mode={mode}): {value}")
            except Exception:
                messagebox.showinfo("Action", f"Insert attempted (mode={mode}).")
        
        # Make an if else ladder for Delete from, if for Beginning, elif for pos, else for end

    def DLL():
        button_color(DLL_button)
        mode = Insert_paradigm_var.get()
        if mode == "Beginning":
            # Insert at beginning for DLL
            pass
        elif mode == "Position":
            # Insert at position for DLL
            pass
        else:
            # Insert at end for DLL
            pass
    
    def CLL():
        button_color(CLL_button)
        mode = Insert_paradigm_var.get()
        if mode == "Beginning":
            # Insert at beginning for CLL
            pass
        elif mode == "Position":
            # Insert at position for CLL
            pass
        else:
            # Insert at end for CLL
            pass
    
    SLL_button = tk.Button(LLscr, text ="SLL", command = SLL,bg = "#505a5b", width = 6,height = 2,fg="#ffffff",font=("Arial", 10, "bold"))
    SLL_button.place(x = 4,y = 5)
    
    DLL_button = tk.Button(LLscr, text ="DLL", command = DLL,bg = "#505a5b", width = 6,height = 2,fg="#ffffff",font=("Arial", 10, "bold"))
    DLL_button.place(x = 84,y = 5)
    
    CLL_button = tk.Button(LLscr, text ="CLL", command = CLL,bg = "#505a5b", width = 6,height = 2,fg="#ffffff",font=("Arial", 10, "bold"))
    CLL_button.place(x = 164,y = 5)

    Insert_paradigm_var = tk.StringVar(LLscr)
    Insert_paradigm_var.set("Insert at")
    insert_options = ["Insert at","Beginning", "Position", "End"]
    Insert_paradigm_menu = tk.OptionMenu(LLscr, Insert_paradigm_var, *insert_options)
    Insert_paradigm_menu.config(font=("Arial", 15, "bold"), bg="#505a5b", fg = "#FFFFFF")
    Insert_paradigm_menu.place(x=250, y=7)
    
    Delete_paradigm_var = tk.StringVar(LLscr)
    Delete_paradigm_var.set("Delete from")
    delete_options = ["Delete from","Beginning", "Position", "End"]
    Delete_paradigm_menu = tk.OptionMenu(LLscr, Delete_paradigm_var, *delete_options)
    Delete_paradigm_menu.config(font=("Arial", 15, "bold"), bg = "#505a5b", fg = "#FFFFFF")
    Delete_paradigm_menu.place(x = 390, y = 7)

    def INSERT(event=None):
        mode = Insert_paradigm_var.get()

        sll_active = SLL_button.cget("bg") == "#06cf0d"
        dll_active = DLL_button.cget("bg") == "#06cf0d"
        cll_active = CLL_button.cget("bg") == "#06cf0d"

        if sll_active:
            target = "SLL"
        elif dll_active:
            target = "DLL"
        elif cll_active:
            target = "CLL"
        else:
            target = "SLL"
            
        if target == "SLL":
            SLL()
        elif target == "DLL":
            DLL()
        else:
            CLL()
    #Make a function called INSERT(), then put conditional statements that says if ins_beg: return 1 elif ins_end: return 2 so on and so forth
    #replace c.ins_beg() with INSERT()

def main_screen():
    root = tk.Tk()
    root.title("Data Structures Visualizer")
    root.geometry("600x600")
    root.configure(bg="#191919")
    
    label = tk.Label(root, text="Visualizers", bg="#36363f", fg="#fcfcf3", font=("Arial", 38, "bold"))
    label.pack(pady=40)

    Stack_button = tk.Button(root,text="Stack", command= lambda: open_stack_visualizer(root),bg="#505a5b", width = 23, height = 3,fg="#ffffff",font=("Arial", 15, "bold"))
    Stack_button.pack(pady=20)
    
    Queue_button = tk.Button(root,text ="Queue", command = lambda: open_queue_visualizer(root),bg="#505a5b", width = 23, height = 3,fg="#ffffff",font=("Arial", 15, "bold"))
    Queue_button.pack(pady=20)
    
    Linkedlist_button = tk.Button(root,text="Linked List", command = lambda: open_linkedlist_visualizer(root),bg="#505a5b", width = 23, height = 3,fg="#ffffff",font=("Arial", 15, "bold"))
    Linkedlist_button.pack(pady=20)    
    root.mainloop()

if __name__ == "__main__":
    main_screen()

#Make it so when you open Stack or any other visualizer the home screen closes itself, provide an option in the visualizers to be able to
#go back to the home screen
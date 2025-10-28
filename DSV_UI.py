import customtkinter as ctk
from tkinter import messagebox
import os, ctypes
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

    stack_scr = ctk.CTkToplevel(parent)
    stack_scr.title("Visual Representation of Stack")
    stack_scr.geometry("355x469")
    stack_scr.configure(bg="#191919")

    entry = ctk.CTkEntry(stack_scr,placeholder_text="Enter a Value", width=200, font = ("",15))
    entry.place(x=4, y=5)
    entry.bind("<Return>", lambda event: Push())

    stack_label = ctk.CTkLabel(stack_scr, text="Stack Contents:", text_color="white", font=("Arial", 16, "bold"))
    stack_label.place(x=4, y=101)

    stack_display = ctk.CTkTextbox(stack_scr, height=340, width=345, state="disabled", fg_color="#505a5b", text_color="#000000", font=("Arial", 26, "bold"))
    stack_display.place(x=5, y=125)

    def update_display():
        size = ctypes.c_int(0)
        stack_ptr = c.get_stack(ctypes.byref(size))

        stack_contents = []
        if size.value > 0:
            for i in range(size.value):
                stack_contents.append(stack_ptr[i])

        stack_display.configure(state="normal")
        stack_display.delete("1.0", "end")

        if stack_contents:
            display_text = "\n".join(map(str, reversed(stack_contents)))
            stack_display.insert("end", display_text)
        else:
            stack_display.insert("end", "Stack is empty.")

        stack_display.configure(state="disabled")

    def Push():
        value_str = entry.get()
        if value_str.isdigit():
            value = int(value_str)
            result = c.push(value)
            if result == -1:
                messagebox.showinfo("Action", "Stack Overflow")
            elif result == 0:
                update_display()
                entry.delete(0, "end")
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
        while c.pop() != -1:
            pass
        update_display()
        messagebox.showinfo("Action", "Stack cleared.")

    def Web():
        webbrowser.open("https://dsa-visualizer-delta.vercel.app/visualizer/stack")

    try:
        img_path = os.path.join(os.path.dirname(__file__), "w.png")
        img = Image.open(img_path)
        rimg = img.resize((30,30))
        web_img = ImageTk.PhotoImage(rimg)
    except FileNotFoundError:
        messagebox.showerror("Error", "w.png not found. Please check the file path.")
        web_img = None

    push_button = ctk.CTkButton(stack_scr, text="Push", command=Push, fg_color="#505a5b", text_color="#ffffff", width=99, height=30, font=("Arial", 12, "bold"))
    push_button.place(x=105, y=40)

    pop_button = ctk.CTkButton(stack_scr, text="Pop", command=Pop, fg_color="#505a5b", text_color="#ffffff", width=99, height=30, font=("Arial", 12, "bold"))
    pop_button.place(x=4, y=40)

    clear_button = ctk.CTkButton(stack_scr, text="Clear", command=Clear, fg_color="#ff0000", text_color="#000000", width=198, height=30, font=("Arial", 12, "bold"))
    clear_button.place(x=4, y=75)

    if web_img:
        web_button = ctk.CTkButton(stack_scr, image=web_img, command=Web, fg_color="#505a5b", width=40, height=27, text="")
        web_button.image = web_img
        web_button.place(x=295, y=6)
    else:
        web_button = ctk.CTkButton(stack_scr, text="Web", command=Web, fg_color="#505a5b", text_color="#000000", width=40, height=25)
        web_button.place(x=295, y=6)

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
    
    LLscr = ctk.CTkToplevel(parent)
    LLscr.title("Visual Representation of Linked List")
    LLscr.geometry("800x600")
    LLscr.configure(bg="#191919")

    entryLL = ctk.CTkEntry(LLscr, placeholder_text="Enter a value", font=("", 15), height=40, width=221)
    entryLL.place(x=4, y=55)
    entryLL.bind("<Return>", lambda event: INSERT())

    def ENTRY():
        if Insert_paradigm_var.get() == "Position":
            if entryLL.get() != "":
                val = entryLL.get()
                entryLL.delete(0, ctk.END)
                entryLL.configure(placeholder_text="Enter the position")
                pos = entryLL.get()
                return val, pos
        if Delete_paradigm_var.get() == "Position":
            entryLL.configure(placeholder_text="Enter the position")
            pos = entryLL.get()
            return val, pos

    def button_color(x):
        L = [SLL_button, DLL_button, CLL_button]
        if x in L:
            x.configure(fg_color="#06cf0d", text_color="#000000")
            L.remove(x)
            for b in L:
                b.configure(fg_color="#505a5b", text_color="#FFFFFF")

    def SLL():
        button_color(SLL_button)
        value_str, pos_str = ENTRY()
        entryLL.delete(0, ctk.END)
        if value_str.isdigit():
            value = int(value_str)
            mode = Insert_paradigm_var.get()
            if mode == "Beginning":
                c.SLL_ins_beg(value)
            elif mode == "Position":
                if pos_str.isdigit():
                    pos = int(pos_str)
                    result = c.SLL_ins_pos(value, pos)
                    if result == 1:
                        messagebox.showinfo("Action", f"Inserted {value} at position {pos}")
            elif mode == "End":
                c.SLL_ins_end(value)
            elif mode == "Insert at":
                messagebox.showwarning("Warning","Please specify where to Insert")

    def DLL():
        button_color(DLL_button)
        value_str, pos_str = ENTRY()
        entryLL.delete(0, ctk.END)
        mode = Insert_paradigm_var.get()
        if value_str.isdigit():
            value = int(value_str)
            if mode == "Beginning":
                c.DLL_ins_beg(value)
            elif mode == "Position":
                if pos_str.isdigit():
                    pos = int(pos_str)
                    result = c.DLL_ins_pos(value, pos)
                    if result == 1:
                        messagebox.showinfo("Action", f"Inserted {value} at position {pos}")
            elif mode == "End":
                result = c.DLL_ins_end(value)
                if result == 1:
                    messagebox.showinfo("Action", f"Inserted {value} at the end")
            else:
                messagebox.showwarning("Warning","Please specify where to Insert")

    def CLL():
        button_color(CLL_button)
        value_str, pos_str = ENTRY()
        entryLL.delete(0, ctk.END)
        if value_str.isdigit():
            value = int(value_str)
            mode = Insert_paradigm_var.get()
            if mode == "Beginning":
                c.CLL_ins_beg(value)
            elif mode == "Position":
                if pos_str.isdigit():
                    pos = int(pos_str)
                    result = c.CLL_ins_pos(value, pos)
                    if result == 1:
                        messagebox.showinfo("Action", f"Inserted {value} at position {pos}")
            elif mode == "End":
                c.CLL_ins_end(value)

    SLL_button = ctk.CTkButton(LLscr, text="SLL", command=SLL, fg_color="#505a5b", width=60, height=40, text_color="#ffffff", font=("Arial", 10, "bold"))
    SLL_button.place(x=4, y=5)

    DLL_button = ctk.CTkButton(LLscr, text="DLL", command=DLL, fg_color="#505a5b", width=60, height=40, text_color="#ffffff", font=("Arial", 10, "bold"))
    DLL_button.place(x=84, y=5)

    CLL_button = ctk.CTkButton(LLscr, text="CLL", command=CLL, fg_color="#505a5b", width=60, height=40, text_color="#ffffff", font=("Arial", 10, "bold"))
    CLL_button.place(x=164, y=5)

    Insert_paradigm_var = ctk.StringVar(value="Insert at")
    insert_options = ["Insert at","Beginning", "Position", "End"]
    Insert_paradigm_menu = ctk.CTkOptionMenu(LLscr, variable=Insert_paradigm_var, values=insert_options, fg_color="#505a5b", text_color="#FFFFFF", font=("Arial", 15, "bold"))
    Insert_paradigm_menu.place(x=250, y=7)
    
    Delete_paradigm_var = ctk.StringVar(value="Delete from")
    delete_options = ["Delete from","Beginning", "Position", "End"]
    Delete_paradigm_menu = ctk.CTkOptionMenu(LLscr, variable=Delete_paradigm_var, values=delete_options, fg_color="#505a5b", text_color="#FFFFFF", font=("Arial", 15, "bold"))
    Delete_paradigm_menu.place(x=400, y=7)

    insert_LL = ctk.CTkButton(LLscr, text="Insert",command= lambda: INSERT(), fg_color="#424242", width=107, height=40, text_color="#ffffff", font=("Arial", 20, "bold"))
    insert_LL.place(x=4, y=105)
    
    del_LL = ctk.CTkButton(LLscr, text = "Delete", fg_color= "#FF0000", width=107, height=40, text_color= "#ffffff", font =("Arial",20, "bold"))
    del_LL.place(x=117,y=105)

    def INSERT(event=None):
        mode = Insert_paradigm_var.get()
        sll_active = SLL_button.cget("fg_color") == "#06cf0d"
        dll_active = DLL_button.cget("fg_color") == "#06cf0d"
        cll_active = CLL_button.cget("fg_color") == "#06cf0d"

        if sll_active:
            SLL()
        elif dll_active:
            DLL()
        elif cll_active:
            CLL()
        else:
            SLL_button.configure(fg_color = "#06cf0d")
            SLL()
            # messagebox.showwarning("Warning", "Please select one of the Linked list types")

def main_screen():
    root = ctk.CTk()
    root.title("Data Structures Visualizer")
    root.geometry("600x600")
    root.configure(bg="#191919")
    
    label = ctk.CTkLabel(root, text="Visualizers", text_color="#fcfcf3", font=("Arial", 38, "bold"))
    label.pack(pady=40)

    Stack_button = ctk.CTkButton(root, text="Stack", command=lambda: open_stack_visualizer(root), fg_color="#505a5b", width=250, height=90, text_color="#ffffff", font=("Arial", 25, "bold"))
    Stack_button.pack(pady=20)
    
    Queue_button = ctk.CTkButton(root, text="Queue", command=lambda: open_queue_visualizer(root), fg_color="#505a5b", width=250, height=90, text_color="#ffffff", font=("Arial", 25, "bold"))
    Queue_button.pack(pady=20)
    
    Linkedlist_button = ctk.CTkButton(root, text="Linked List", command=lambda: open_linkedlist_visualizer(root), fg_color="#505a5b", width=250, height=90, text_color="#ffffff", font=("Arial", 25, "bold"))
    Linkedlist_button.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main_screen()
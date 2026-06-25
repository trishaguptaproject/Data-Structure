import tkinter as tk
from tkinter import messagebox

# Stack class to store items
class Stack:
    def __init__(self):
        self.items = []  # empty list to hold stack items

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Stack is empty!")
        return self.items[-1]

    def size(self):
        return len(self.items)


# Create stack object
stack = Stack()

# ── Button Functions ──

def push_item():
    item = entry.get().strip()
    if item == "":
        messagebox.showwarning("Oops!", "Please type something first.")
        return
    stack.push(item)
    entry.delete(0, tk.END)
    refresh_list()
    output.insert(tk.END, f'Pushed: "{item}"\n')

def pop_item():
    try:
        item = stack.pop()
        refresh_list()
        output.insert(tk.END, f'Popped: "{item}"\n')
    except IndexError:
        messagebox.showerror("Error", "Stack is empty! Nothing to pop.")

def peek_item():
    try:
        item = stack.peek()
        output.insert(tk.END, f'Top item: "{item}"\n')
    except IndexError:
        messagebox.showerror("Error", "Stack is empty! Nothing to peek.")

def check_empty():
    if stack.is_empty():
        output.insert(tk.END, "Stack is EMPTY.\n")
    else:
        output.insert(tk.END, f"Stack is NOT empty. Size = {stack.size()}\n")

def get_size():
    output.insert(tk.END, f"Stack size: {stack.size()}\n")

def clear_stack():
    stack.items.clear()
    refresh_list()
    output.insert(tk.END, "Stack cleared.\n")

def refresh_list():
    listbox.delete(0, tk.END)
    for i, item in enumerate(reversed(stack.items)):
        if i == 0:
            listbox.insert(tk.END, f"  {item}  <-- TOP")
        else:
            listbox.insert(tk.END, f"  {item}")
    size_label.config(text=f"Size: {stack.size()}")


# ── Color Palette (Black & White) ──
BG_MAIN    = "#FFFFFF"   # white background
BG_HEADER  = "#000000"   # black header
BG_INPUT   = "#F2F2F2"   # light grey for input/listbox/output
FG_PRIMARY = "#000000"   # black text
FG_LIGHT   = "#555555"   # dark grey for subtle labels
BTN_BG     = "#000000"   # black buttons
BTN_FG     = "#FFFFFF"   # white button text
BTN_ACT    = "#333333"   # dark grey on hover/active


# ── Window Setup ──
root = tk.Tk()
root.title("Stack Operations")
root.geometry("480x560")
root.configure(bg=BG_MAIN)

# Title
tk.Label(root, text="Stack Operations",
         font=("Arial", 16, "bold"),
         bg=BG_HEADER, fg=BTN_FG,
         pady=10).pack(fill="x")

# Input box
tk.Label(root, text="Enter item:",
         font=("Arial", 10),
         bg=BG_MAIN, fg=FG_PRIMARY).pack(pady=(12, 2))

entry = tk.Entry(root, width=28, font=("Arial", 12),
                 bg=BG_INPUT, fg=FG_PRIMARY,
                 insertbackground=FG_PRIMARY,
                 relief="solid", bd=1)
entry.pack()
entry.bind("<Return>", lambda e: push_item())  # press Enter = push

# Buttons
for (label, cmd) in [
    ("Push",        push_item),
    ("Pop",         pop_item),
    ("Peek",        peek_item),
    ("Is Empty?",   check_empty),
    ("Get Size",    get_size),
    ("Clear Stack", clear_stack),
]:
    tk.Button(root, text=label, width=14,
              bg=BTN_BG, fg=BTN_FG,
              activebackground=BTN_ACT, activeforeground=BTN_FG,
              relief="flat", bd=0,
              command=cmd).pack(pady=3)

# Stack display
tk.Label(root, text="Stack (top → bottom):",
         font=("Arial", 10),
         bg=BG_MAIN, fg=FG_PRIMARY).pack(pady=(10, 2))

listbox = tk.Listbox(root, width=38, height=6,
                     font=("Courier", 11),
                     bg=BG_INPUT, fg=FG_PRIMARY,
                     selectbackground="#000000",
                     selectforeground="#FFFFFF",
                     relief="solid", bd=1)
listbox.pack()

size_label = tk.Label(root, text="Size: 0",
                      font=("Arial", 9),
                      bg=BG_MAIN, fg=FG_LIGHT)
size_label.pack()

# Output log
tk.Label(root, text="Output:",
         font=("Arial", 10),
         bg=BG_MAIN, fg=FG_PRIMARY).pack(pady=(8, 2))

output = tk.Text(root, width=52, height=6,
                 font=("Arial", 10),
                 bg=BG_INPUT, fg=FG_PRIMARY,
                 insertbackground=FG_PRIMARY,
                 relief="solid", bd=1)
output.pack(padx=10, pady=(0, 10))

root.mainloop()

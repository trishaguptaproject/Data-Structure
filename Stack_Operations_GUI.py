import tkinter as tk
from tkinter import messagebox


stack = []


#STACK OPERATIONS

def push():
    item = entry.get()

    if item == "":
        messagebox.showerror("Error", "Enter an element")
        return

    stack.append(item)
    entry.delete(0, tk.END)
    show_stack()
    messagebox.showinfo("Push", item + " inserted into stack")


def pop():
    if len(stack) == 0:
        messagebox.showerror("Error", "Stack Underflow")
    else:
        item = stack.pop()
        show_stack()
        messagebox.showinfo("Pop", "Deleted element: " + item)


def peek():
    if len(stack) == 0:
        messagebox.showerror("Error", "Stack is Empty")
    else:
        messagebox.showinfo("Peek", "Top element: " + stack[-1])


def show_stack():
    listbox.delete(0, tk.END)

    for i in range(len(stack)-1, -1, -1):
        listbox.insert(tk.END, stack[i])


# DELIMITER MATCHING 

def delimiter_matching():

    exp = entry.get()

    s = []

    pairs = {
        ')':'(',
        '}':'{',
        ']':'['
    }

    for ch in exp:

        if ch in "({[":
            s.append(ch)

        elif ch in ")}]":

            if len(s)==0 or s.pop()!=pairs[ch]:
                messagebox.showinfo(
                    "Delimiter",
                    "Expression is Not Balanced"
                )
                return


    if len(s)==0:
        messagebox.showinfo(
            "Delimiter",
            "Expression is Balanced"
        )
    else:
        messagebox.showinfo(
            "Delimiter",
            "Expression is Not Balanced"
        )


# PREFIX TO POSTFIX

def prefix_postfix():

    exp = entry.get()

    s=[]

    operators="+-*/^"


    for ch in exp[::-1]:

        if ch==" ":
            continue

        if ch not in operators:
            s.append(ch)

        else:

            a=s.pop()
            b=s.pop()

            s.append(a+b+ch)


    messagebox.showinfo(
        "Prefix to Postfix",
        s.pop()
    )


# PREFIX EVALUATION 

def evaluate_prefix():

    exp = entry.get()

    s=[]

    operators="+-*/"


    for ch in exp[::-1]:

        if ch==" ":
            continue


        if ch.isdigit():

            s.append(int(ch))


        else:

            a=s.pop()
            b=s.pop()


            if ch=='+':
                s.append(a+b)

            elif ch=='-':
                s.append(a-b)

            elif ch=='*':
                s.append(a*b)

            elif ch=='/':
                s.append(a/b)


    messagebox.showinfo(
        "Prefix Evaluation",
        "Result = "+str(s.pop())
    )

# GUI 

window = tk.Tk()

window.title("Stack Implementation Using List")
window.geometry("450x550")
window.config(bg="lightblue")

title = tk.Label(
    window,
    text="STACK OPERATIONS",
    font=("Arial",18,"bold"),
    bg="lightblue"
)

title.pack(pady=10)

entry = tk.Entry(
    window,
    width=35,
    font=("Arial",12)
)

entry.pack(pady=10)

btn1=tk.Button(
    window,
    text="Push",
    width=20,
    command=push
)

btn1.pack(pady=5)

btn2=tk.Button(
    window,
    text="Pop",
    width=20,
    command=pop
)

btn2.pack(pady=5)

btn3=tk.Button(
    window,
    text="Peek",
    width=20,
    command=peek
)

btn3.pack(pady=5)

btn4=tk.Button(
    window,
    text="Display Stack",
    width=20,
    command=show_stack
)

btn4.pack(pady=5)

btn5=tk.Button(
    window,
    text="Delimiter Matching",
    width=20,
    command=delimiter_matching
)

btn5.pack(pady=5)

btn6=tk.Button(
    window,
    text="Prefix To Postfix",
    width=20,
    command=prefix_postfix
)

btn6.pack(pady=5)

btn7=tk.Button(
    window,
    text="Evaluate Prefix",
    width=20,
    command=evaluate_prefix
)

btn7.pack(pady=5)

listbox=tk.Listbox(
    window,
    width=25,
    height=8,
    font=("Arial",12)
)

listbox.pack(pady=15)

exit_btn=tk.Button(
    window,
    text="Exit",
    width=20,
    command=window.destroy
)

exit_btn.pack(pady=5)

window.mainloop()

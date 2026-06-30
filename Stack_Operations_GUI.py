# STACK IMPLEMENTATION GUI USING TKINTER

from tkinter import *


stack = []


# Push
def push():
    item = entry.get()

    if item:
        stack.append(item)
        result.config(text=item + " inserted")
        entry.delete(0, END)
        show_stack()


# Pop
def pop():
    if stack == []:
        result.config(text="Stack Underflow")
    else:
        result.config(text="Deleted: " + stack.pop())
        show_stack()


# Peek
def peek():
    if stack == []:
        result.config(text="Stack Empty")
    else:
        result.config(text="Top: " + stack[-1])


# Display
def show_stack():
    if stack == []:
        stack_box.config(text="Stack Empty")
    else:
        stack_box.config(text="\n".join(stack[::-1]))


# Delimiter Matching
def delimiter():

    exp = entry.get()
    s = []

    pair = {')':'(', '}':'{', ']':'['}

    for ch in exp:
        if ch in "({[":
            s.append(ch)

        elif ch in ")}]":
            if s == [] or s.pop() != pair[ch]:
                result.config(text="Not Balanced")
                return

    if s == []:
        result.config(text="Balanced")
    else:
        result.config(text="Not Balanced")


# Prefix to Postfix

def prefix_postfix():

    exp = entry.get()
    s = []

    op = "+-*/^"

    for ch in exp[::-1]:

        if ch not in op:
            s.append(ch)

        else:
            a = s.pop()
            b = s.pop()
            s.append(a+b+ch)

    result.config(text="Postfix: "+s[0])


# Prefix Evaluation

def evaluate():

    exp = entry.get()
    s = []

    try:
        for ch in exp[::-1]:

            if ch == " ":
                continue

            if ch.isdigit():
                s.append(int(ch))

            elif ch in "+-*/":

                if len(s) < 2:
                    result.config(text="Invalid Prefix Expression")
                    return

                a = s.pop()
                b = s.pop()

                if ch == '+':
                    s.append(a + b)

                elif ch == '-':
                    s.append(a - b)

                elif ch == '*':
                    s.append(a * b)

                elif ch == '/':
                    s.append(a / b)

            else:
                result.config(text="Invalid Character")
                return


        if len(s) == 1:
            result.config(text="Answer: " + str(s[0]))
        else:
            result.config(text="Invalid Prefix Expression")


    except:
        result.config(text="Invalid Prefix Expression")


# GUI Window

root = Tk()

root.title("Stack Operations")
root.geometry("400x500")


title = Label(root,
              text="STACK IMPLEMENTATION",
              font=("Arial",16,"bold"))

title.pack(pady=10)


entry = Entry(root,font=("Arial",14))
entry.pack(pady=10)


Button(root,text="Push",
       width=20,
       command=push).pack(pady=5)


Button(root,text="Pop",
       width=20,
       command=pop).pack(pady=5)


Button(root,text="Peek",
       width=20,
       command=peek).pack(pady=5)


Button(root,text="Display Stack",
       width=20,
       command=show_stack).pack(pady=5)


Button(root,text="Delimiter Matching",
       width=20,
       command=delimiter).pack(pady=5)


Button(root,text="Prefix To Postfix",
       width=20,
       command=prefix_postfix).pack(pady=5)


Button(root,text="Evaluate Prefix",
       width=20,
       command=evaluate).pack(pady=5)



stack_box = Label(root,
                  text="Stack Empty",
                  bg="lightblue",
                  width=20,
                  height=5)

stack_box.pack(pady=10)



result = Label(root,
               text="Result",
               fg="green",
               font=("Arial",12))

result.pack(pady=10)



root.mainloop()

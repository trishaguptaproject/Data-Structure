import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node


    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head

        while temp.next:
            temp = temp.next

        temp.next = new_node


    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head

        for i in range(position - 1):
            if temp is None:
                raise IndexError("Position out of bounds")

            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    def delete_node_by_value(self, value):

        temp = self.head

        if temp is not None and temp.data == value:
            self.head = temp.next
            return True


        prev = None

        while temp:

            if temp.data == value:
                break

            prev = temp
            temp = temp.next


        if temp is None:
            return False


        prev.next = temp.next
        return True



    def delete_node_by_index(self, position):

        if self.head is None:
            return False


        temp = self.head


        if position == 0:
            self.head = temp.next
            return True


        for i in range(position - 1):

            if temp is None:
                return False

            temp = temp.next


        if temp.next is None:
            return False


        temp.next = temp.next.next
        return True



    def display(self):

        result = []

        temp = self.head

        while temp:
            result.append(str(temp.data))
            temp = temp.next


        return " -> ".join(result)



#  GUI 


linked_list = LinkedList()


def insert_beginning():

    try:
        data = int(entry_data.get())

        linked_list.insert_at_beginning(data)

        show_list()

    except:
        messagebox.showerror("Error", "Enter valid data")



def insert_end():

    try:
        data = int(entry_data.get())

        linked_list.insert_at_end(data)

        show_list()

    except:
        messagebox.showerror("Error", "Enter valid data")



def insert_position():

    try:
        data = int(entry_data.get())
        pos = int(entry_position.get())

        linked_list.insert_at_position(data, pos)

        show_list()

    except:
        messagebox.showerror("Error", "Invalid position")



def delete_value():

    try:

        value = int(entry_data.get())

        if linked_list.delete_node_by_value(value):
            show_list()
        else:
            messagebox.showinfo("Result", "Value not found")

    except:
        messagebox.showerror("Error", "Enter valid value")



def delete_index():

    try:

        pos = int(entry_position.get())

        if linked_list.delete_node_by_index(pos):
            show_list()

        else:
            messagebox.showinfo("Result", "Invalid index")

    except:
        messagebox.showerror("Error", "Enter valid index")



def show_list():

    output.delete(1.0, tk.END)

    value = linked_list.display()

    if value == "":
        output.insert(tk.END, "Linked List is empty")

    else:
        output.insert(tk.END, value)



# Window

window = tk.Tk()

window.title("Singly Linked List Operations")

window.geometry("450x500")


title = tk.Label(
    window,
    text="Singly Linked List GUI",
    font=("Arial", 16, "bold")
)

title.pack(pady=10)



# Data Entry

tk.Label(window, text="Enter Data").pack()

entry_data = tk.Entry(window)

entry_data.pack()



tk.Label(window, text="Enter Position / Index").pack()

entry_position = tk.Entry(window)

entry_position.pack()



# Buttons


tk.Button(
    window,
    text="Insert Beginning",
    width=20,
    command=insert_beginning
).pack(pady=5)



tk.Button(
    window,
    text="Insert End",
    width=20,
    command=insert_end
).pack(pady=5)



tk.Button(
    window,
    text="Insert Position",
    width=20,
    command=insert_position
).pack(pady=5)



tk.Button(
    window,
    text="Delete Value",
    width=20,
    command=delete_value
).pack(pady=5)



tk.Button(
    window,
    text="Delete Index",
    width=20,
    command=delete_index
).pack(pady=5)



tk.Button(
    window,
    text="Display List",
    width=20,
    command=show_list
).pack(pady=5)



# Output box

output = tk.Text(
    window,
    height=8,
    width=40
)

output.pack(pady=10)



window.mainloop()

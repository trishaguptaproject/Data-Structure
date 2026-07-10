import tkinter as tk
from tkinter import messagebox


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self):
        self.head = None


    def insert_at_beginning(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):

        new_node = Node(data)

        if self.head is None:
            self.head = new_node

        else:
            temp = self.head

            while temp.next:
                temp = temp.next

            temp.next = new_node
            new_node.prev = temp

    def insert_at_position(self, data, position):

        if position == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)

        temp = self.head

        for i in range(position):

            if temp is None:
                raise IndexError("Invalid position")

            temp = temp.next

        if temp is None:
            raise IndexError("Invalid position")

        new_node.next = temp
        new_node.prev = temp.prev

        if temp.prev:
            temp.prev.next = new_node

        temp.prev = new_node

    def delete_node_at_beginning(self):

        if self.head is None:
            return False


        if self.head.next is None:
            self.head = None

        else:
            self.head = self.head.next
            self.head.prev = None

        return True

    def delete_node_at_end(self):

        if self.head is None:
            return False


        if self.head.next is None:
            self.head = None

        else:

            temp = self.head

            while temp.next:
                temp = temp.next


            temp.prev.next = None

        return True

    def delete_node_at_position(self, position):

        if self.head is None:
            return False


        temp = self.head

        for i in range(position):

            if temp is None:
                return False

            temp = temp.next

        if temp is None:
            return False

        if temp.prev:
            temp.prev.next = temp.next

        if temp.next:
            temp.next.prev = temp.prev


        return True

    def display_list(self):

        result = []

        temp = self.head


        while temp:

            result.append(str(temp.data))

            temp = temp.next


        return " <-> ".join(result)

    def search_node(self, key):

        temp = self.head

        while temp:

            if temp.data == key:
                return True

            temp = temp.next
        return False

    def length_of_list(self):

        count = 0

        temp = self.head

        while temp:

            count += 1

            temp = temp.next
        return count
# GUI 

linked_list = DoublyLinkedList()

def get_data():

    try:
        return int(entry_data.get())

    except:
        messagebox.showerror("Error", "Enter a valid number")

        return None

def insert_beginning():

    data = get_data()

    if data is not None:

        linked_list.insert_at_beginning(data)

        display()

def insert_end():

    data = get_data()

    if data is not None:

        linked_list.insert_at_end(data)

        display()

def insert_position():

    data = get_data()

    try:

        pos = int(entry_position.get())

        linked_list.insert_at_position(data, pos)

        display()

    except:

        messagebox.showerror("Error", "Invalid position")

def delete_beginning():

    linked_list.delete_node_at_beginning()

    display()
def delete_end():

    linked_list.delete_node_at_end()

    display()
def delete_position():

    try:

        pos = int(entry_position.get())

        linked_list.delete_node_at_position(pos)

        display()
    except:

        messagebox.showerror("Error", "Invalid position")
def search():

    data = get_data()

    if linked_list.search_node(data):

        messagebox.showinfo("Search", "Node Found")
    else:

        messagebox.showinfo("Search", "Node Not Found")

def length():

    messagebox.showinfo(
        "Length",
        "Length of list: " + str(linked_list.length_of_list())
    )

def display():

    output.delete(1.0, tk.END)

    value = linked_list.display_list()

    if value == "":

        output.insert(tk.END, "List is empty")

    else:

        output.insert(tk.END, value)

# Window

window = tk.Tk()

window.title("Doubly Linked List GUI")

window.geometry("500x600")

title = tk.Label(
    window,
    text="Doubly Linked List Operations",
    font=("Arial",16,"bold")
)

title.pack(pady=10)

tk.Label(window,text="Enter Data").pack()

entry_data = tk.Entry(window)

entry_data.pack()

tk.Label(window,text="Enter Position / Index").pack()

entry_position = tk.Entry(window)

entry_position.pack()

tk.Button(window,text="Insert Beginning",
          width=25,
          command=insert_beginning).pack(pady=5)
tk.Button(window,text="Insert End",
          width=25,
          command=insert_end).pack(pady=5)
tk.Button(window,text="Insert Position",
          width=25,
          command=insert_position).pack(pady=5)
tk.Button(window,text="Delete Beginning",
          width=25,
          command=delete_beginning).pack(pady=5)
tk.Button(window,text="Delete End",
          width=25,
          command=delete_end).pack(pady=5)
tk.Button(window,text="Delete Position",
          width=25,
          command=delete_position).pack(pady=5)
tk.Button(window,text="Search Node",
          width=25,
          command=search).pack(pady=5)
tk.Button(window,text="Find Length",
          width=25,
          command=length).pack(pady=5)
tk.Button(window,text="Display List",
          width=25,
          command=display).pack(pady=5)

output = tk.Text(
    window,
    height=8,
    width=45
)

output.pack(pady=15)

window.mainloop()

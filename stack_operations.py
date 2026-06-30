import os
import time
from termcolor import colored, cprint


class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    # Push operation
    def push(self, item):
        self.items.append(item)
        print(colored(f"'{item}' has been pushed onto the stack.", "green"))
        self.animate_insert(item)

    # Pop operation
    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from an empty stack")

        item = self.items.pop()
        print(colored(f"'{item}' has been popped from the stack.", "red"))
        self.animate_delete(item)
        return item

    # Peek operation
    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from an empty stack")
        return self.items[-1]

    def size(self):
        return len(self.items)

    def traverse(self):
        if self.is_empty():
            raise IndexError("Cannot traverse an empty stack")
        return " <- ".join(reversed(self.items))

    def __str__(self):
        if self.items:
            return " <- ".join(reversed(self.items))
        return "Stack is empty"

    def animate_insert(self, item):
        for _ in range(3):
            self.clear_screen()
            print(colored(f"Pushing {item}...", "yellow"))
            time.sleep(0.3)

    def animate_delete(self, item):
        for _ in range(3):
            self.clear_screen()
            print(colored(f"Popping {item}...", "magenta"))
            time.sleep(0.3)

    @staticmethod
    def clear_screen():
        os.system("cls" if os.name == "nt" else "clear")


def stack_operations():
    stack = Stack()

    cprint("Welcome to the Interactive Stack Operations Program!", "cyan", attrs=["bold"])

    while True:
        print("\nCurrent Stack:", colored(str(stack), "blue"))

        print(colored("1. Push an item", "yellow"))
        print(colored("2. Pop an item", "yellow"))
        print(colored("3. Peek at the top item", "yellow"))
        print(colored("4. Check if stack is empty", "yellow"))
        print(colored("5. Get stack size", "yellow"))
        print(colored("6. Traverse stack", "yellow"))
        print(colored("7. Quit", "yellow"))

        try:
            choice = int(input(colored("Choose an option (1-7): ", "green")))
        except ValueError:
            cprint("Please enter a valid number.", "red")
            continue

        if choice == 1:
            item = input(colored("Enter item: ", "green"))
            stack.push(item)

        elif choice == 2:
            try:
                removed = stack.pop()
                cprint(f"Popped Item: {removed}", "blue")
            except IndexError as e:
                cprint(e, "red")

        elif choice == 3:
            try:
                cprint("Top Item: " + stack.peek(), "blue")
            except IndexError as e:
                cprint(e, "red")

        elif choice == 4:
            cprint("Stack Empty? " + ("Yes" if stack.is_empty() else "No"), "blue")

        elif choice == 5:
            cprint("Stack Size: " + str(stack.size()), "blue")

        elif choice == 6:
            try:
                cprint("Stack Contents: " + stack.traverse(), "blue")
            except IndexError as e:
                cprint(e, "red")

        elif choice == 7:
            cprint("Goodbye!", "cyan", attrs=["bold"])
            break

        else:
            cprint("Invalid Choice.", "red")


if __name__ == "__main__":
    stack_operations()

# STACK IMPLEMENTATION USING LIST

stack = []

# Push Operation
def push():
    item = input("Enter element to push: ")
    stack.append(item)
    print(item, "inserted into stack.")

# Pop Operation
def pop():
    if len(stack) == 0:
        print("Stack Underflow")
    else:
        print("Deleted element:", stack.pop())

# Peek Operation
def peek():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Top element is:", stack[-1])

# Traversal Operation
def display():
    if len(stack) == 0:
        print("Stack is Empty")
    else:
        print("Stack Elements:")
        for i in range(len(stack)-1, -1, -1):
            print(stack[i])

# DELIMITER MATCHING

def delimiter_matching():
    expression = input("Enter expression: ")

    s = []
    pairs = {')':'(', '}':'{', ']':'['}

    balanced = True

    for ch in expression:
        if ch in "({[":
            s.append(ch)
        elif ch in ")}]":
            if len(s) == 0 or s.pop() != pairs[ch]:
                balanced = False
                break

    if balanced and len(s) == 0:
        print("Expression is Balanced")
    else:
        print("Expression is Not Balanced")

# PREFIX TO POSTFIX CONVERSION

def prefix_to_postfix():
    prefix = input("Enter Prefix Expression: ")

    stack = []

    operators = "+-*/^"

    for ch in prefix[::-1]:
        if ch == " ":
            continue

        if ch not in operators:
            stack.append(ch)
        else:
            op1 = stack.pop()
            op2 = stack.pop()
            temp = op1 + op2 + ch
            stack.append(temp)

    print("Postfix Expression:", stack.pop())

# PREFIX EXPRESSION EVALUATION

def evaluate_prefix():
    expression = input("Enter Prefix Expression (single digits): ")

    stack = []

    operators = "+-*/"

    for ch in expression[::-1]:

        if ch == " ":
            continue

        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()

            if ch == '+':
                stack.append(a + b)
            elif ch == '-':
                stack.append(a - b)
            elif ch == '*':
                stack.append(a * b)
            elif ch == '/':
                stack.append(a / b)

    print("Result =", stack.pop())

# MENU

while True:

    print("\n===== STACK MENU =====")
    print("1. Push")
    print("2. Pop")
    print("3. Peek")
    print("4. Display")
    print("5. Delimiter Matching")
    print("6. Prefix to Postfix")
    print("7. Evaluate Prefix")
    print("8. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        push()

    elif choice == 2:
        pop()

    elif choice == 3:
        peek()

    elif choice == 4:
        display()

    elif choice == 5:
        delimiter_matching()

    elif choice == 6:
        prefix_to_postfix()

    elif choice == 7:
        evaluate_prefix()

    elif choice == 8:
        print("Program Ended.")
        break

    else:
        print("Invalid Choice")

import time

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
                raise IndexError("Position out of bounds.")

            temp = temp.next

        new_node.next = temp.next
        temp.next = new_node


    def delete_node_by_value(self, value):
        temp = self.head

        if temp is not None:
            if temp.data == value:
                self.head = temp.next
                return

        prev = None

        while temp is not None:
            if temp.data == value:
                break

            prev = temp
            temp = temp.next

        if temp is None:
            print("Value not found.")
            return

        prev.next = temp.next


    def delete_node_by_index(self, position):

        if self.head is None:
            print("Linked List is empty.")
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            return

        for i in range(position - 1):

            if temp is None:
                raise IndexError("Position out of bounds.")

            temp = temp.next


        if temp.next is None:
            raise IndexError("Position out of bounds.")

        temp.next = temp.next.next


    def display_list(self):

        temp = self.head

        if temp is None:
            print("Linked List is empty.")
            return

        print("Linked List:")

        while temp:
            print(temp.data, end=" ")

            temp = temp.next

        print()



def display_menu():

    print("\n===== Singly Linked List Operations =====")
    print("1. Insert at beginning")
    print("2. Insert at end")
    print("3. Insert at position")
    print("4. Delete node by value")
    print("5. Delete node by index")
    print("6. Display the list")
    print("7. Exit")



def main():

    linked_list = LinkedList()

    while True:

        display_menu()

        try:

            choice = int(input("Enter your choice: "))


            if choice == 1:

                data = int(input("Enter data: "))

                linked_list.insert_at_beginning(data)

                print("Node inserted at beginning.")


            elif choice == 2:

                data = int(input("Enter data: "))

                linked_list.insert_at_end(data)

                print("Node inserted at end.")


            elif choice == 3:

                data = int(input("Enter data: "))

                position = int(input("Enter position (0-indexed): "))

                linked_list.insert_at_position(data, position)

                print("Node inserted successfully.")


            elif choice == 4:

                value = int(input("Enter value to delete: "))

                linked_list.delete_node_by_value(value)

                print("Delete operation completed.")


            elif choice == 5:

                position = int(input("Enter index to delete: "))

                linked_list.delete_node_by_index(position)

                print("Node deleted successfully.")


            elif choice == 6:

                linked_list.display_list()


            elif choice == 7:

                print("Exiting program...")

                break


            else:

                print("Invalid choice.")


        except ValueError:

            print("Please enter a valid number.")


        except IndexError as e:

            print(e)


        except Exception as e:

            print("Error:", e)


        time.sleep(1)



if __name__ == "__main__":
    main()

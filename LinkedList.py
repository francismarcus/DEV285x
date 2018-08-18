class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        current = self.head
        count = 0
        while current:
            count += 1
            current = current.next
        return count

    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            else:
                current = current.next
        print("Not found.")
        return

    def delete(self, data):
        current = self.head
        previous = None

        if not current:
            if current.data == data:
                self.head = current.next
                return

        while current:
            if current.data == data:
                previous.next = current.next
                return
            else:
                previous = current
                current = current.next
        return

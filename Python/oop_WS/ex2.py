# Approved by: Or

class Node():
    """ Class of nodes """
    def __init__(self, value):
        self.value = value
        self.next = None


class Linked_List():
    """ Class of linked nodes """
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0


    def push(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1


    def pop(self):
        if self.is_empty():
            print("List is empty, can't pop.")
            return None
        pop_node = self.head
        self.head = pop_node.next
        pop_node = None
        self.length -= 1


    def Head(self):
        if self.is_empty():
             print("List is empty, no head.")
             return None
        return self.head.value


    def len(self):
        return self.length


    def is_empty(self):
        return self.length == 0


if __name__ == "__main__":
    lst = Linked_List()  
    print("----- Trying to pop from empty list -----")
    lst.pop()
    print(f"List empty? {lst.is_empty()}")
    print("----- Pushing first node into list -----")
    lst.push(5)
    print(f"First node: {lst.Head()}")
    print(f"List length: {lst.len()}")
    print(f"List empty? {lst.is_empty()}")
    print("----- Pushing second node into list -----")
    lst.push(10)
    print(f"First node: {lst.Head()}")
    print(f"List length: {lst.len()}")
    print(f"List empty? {lst.is_empty()}")
    print("----- Poping second node from list -----")
    lst.pop()
    print(f"First node: {lst.Head()}")
    print(f"List length: {lst.len()}")
    print(f"List empty? {lst.is_empty()}")
    print("----- Poping first node from list -----")
    lst.pop()
    print(f"First node: {lst.Head()}")
    print(f"List length: {lst.len()}")
    print(f"List empty? {lst.is_empty()}")
    print("----- Poping from empty list -----")
    lst.pop()
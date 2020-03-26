class Node:

    def __init__(self, data):
        self.data = data
        self.next = None
        self.before = None


class MyList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            self.tail = self.head
            self.length = 1
        else:
            self.tail.before = self.head
            self.tail.next = new_node
            new_node.before = self.tail
            self.tail = new_node
            self.length += 1

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head.before = new_node
        self.head = new_node
        self.length += 1

    def traverse_to_index(self, index):
        count = 0
        current_node = self.head
        while not count == index:
            current_node = current_node.next
            count += 1
        return current_node

    def insert(self, index, data):
        new_node = Node(data)
        if index >= self.length:
            self.append(data)
            return
        else:
            insert_after = self.traverse_to_index(index - 1)
            insert_before = insert_after.next
            insert_after.next = new_node
            new_node.before = insert_after
            insert_before.before = new_node
            new_node.next = insert_before
            self.length += 1

    def remove(self, index):
        if index == self.length - 1:
            self.tail = self.tail.before
            self.tail.next = None
            self.length -= 1
            return

        else:
            before_node = self.traverse_to_index(index - 1)
            node_to_remove = before_node.next
            after_node = node_to_remove.next
            # del(nodeToRemove)
            before_node.next = after_node
            after_node.before = before_node
            self.length -= 1

    def print_l(self):
        temp = self.head
        while temp is not None:
            print(temp.data, end=' ')
            temp = temp.next
        print()
        print('Length = ' + str(self.length))

    def reverse(self):
        prev = None
        self.tail = self.head
        while self.head is not None:
            temp = self.head
            self.head = self.head.next
            temp.next = prev
            prev = temp
        self.head = temp


l = MyList()
l.append(10)
l.append(5)
l.append(6)
l.insert(2, 99)
l.remove(2)

l.print_l()

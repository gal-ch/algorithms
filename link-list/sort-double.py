class DoublyLinkedListNode:

    def __init__(self, next=None, prev=None, data=None):
        self.next = next
        self.prev = prev
        self.data = data


def sortedInsert(head, data):
    courrnt = head
    node = DoublyLinkedListNode(data)
    if not courrnt.next:
        head.next = node
        node.prev = head
        return head
    while courrnt:
        if courrnt.data < data < courrnt.next.data or courrnt.data == data:
            node.next = courrnt.next
            courrnt.next.prev = node
            node.prev = courrnt
            courrnt.next = node
            return
        courrnt = courrnt.next
    if courrnt.data < data or courrnt.data == data:
        node.prev = courrnt
        courrnt.next = node
        return head

class LinkedList:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


a = LinkedList(1)
b = LinkedList(2, a)
c = LinkedList(3, b)
d = LinkedList(4, c)
e = LinkedList(5, d)
f = LinkedList(6, e)

curr = a
prev = None
next = a.next

while next != None:
    curr.next = prev
    prev = curr
    next = next.next

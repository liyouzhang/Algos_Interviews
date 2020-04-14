class Element(object):
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList(object):
    def __init__(self, head=None):
        self.head = head

    def append(self, new_element):
        current = self.head
        if self.head:
            while current.next:
                current = current.next
            current.next = new_element
        else:
            self.head = new_element

## ipython playaround
# e1 = Element(2)
# l1 = Linkedlist()
# l1.append(e1)
# e2 = Element(4)
# l1.append(e2)
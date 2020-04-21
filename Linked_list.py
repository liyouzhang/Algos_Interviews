"""The LinkedList code from before is provided below.
Add three functions to the LinkedList.
"get_position" returns the element at a certain position.
The "insert" function will add an element to a particular
spot in the list.
"delete" will delete the first element with that
particular value.
Then, use "Test Run" and "Submit" to run the test cases
at the bottom."""

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

    def get_position(self, position):
        """Get an element from a particular position.
        Assume the first position is "1".
        Return "None" if position is not in the list."""
        # use i as num of moves
        # when i < position, then i+1, and current point to next element
        # until i = position,  then return the element's value
        i = 1
        current = self.head
        if position < 1:
            return None #missed this edge case 
        while current and i < position:
            if current.next:
                current = current.next
                i += 1
            else:
                return None
        return current

# Test get_position(1)
# i = 1 
# current = Element(value=1,next=None)
# return current {1, None}

# Test get_position(2)
# i = 1 
# current = Element(value=1,next={2,3})
# i < 2, current.next is True
# current = Element(2, next = {3,4})
# i = 2
# return {2,3}

# Test get_position(5)
# i = 1 
# current = {1, {2,3}}
# while 1 < 5
# while current has next:
# current = {2,{3,4}}
# i = 2
# while 2 < 5
# current has next
# current = {3,{4, None}}
# i = 3
# while 3 < 5:
# current has next:
# current = {4, None}
# i = 4
# while 4 < 5:
# current doesn't have next:
# return None

    def insert(self, new_element, position):
        """Insert a new node at the given position.
        Assume the first position is "1".
        Inserting at position 3 means between
        the 2nd and 3rd elements."""
        # e.g. {1,{2,{3,{4,None}}}
        # add at postion 2 {1,None} means between 1st and 2nd element
        # {1,{1,{2,{3,{4,None}}}}

        # call get_position() to return the node n-1 and n 
        # for node n-1, change the next = element
        # for element.next, assign to node n
        prev_node = self.get_position(position-1)
        prev_node.next = new_element
        next_node = self.get_position(position)
        new_element.next = next_node

    def delete(self, value):
        """Delete the first node with a given value."""
        # [1,2,2,3,4]
        # delete(2) will mean [1,2,3,4]
        # {1,{2,{2,{3,{4,none}}}}}

        # iterate the nodes from beginning and use counter for indexing
        # if node.value = value
        # if yes, then fetch previous node and next node 
            # previous.next = next node 
        # if no, then move to next node 

        # edge cases:
        # when delete the first node, then there is no prev_node
            # then next node becomes the start
            # LinkedList.head = next node 
        # when delete the last node, then there is no next_node 
            # change prev node.next = None
        # what if the value is not in the linked list?
            #  the while loop will run forever
            #  need to know the length of the LL

        idx = 1
        current = self.get_position(idx)
        while current.value != value and current.next != None:
            if idx <= n:
                idx += 1
            else:
                return None
        if (idx - 1) == 0: #first node
            next_node = self.get_position(idx+1)
            self.head = next_node
        elif current.next == None: #last node
            prev_node = self.get_position(idx-1)
            prev_node.next = None
        else:
            prev_node = self.get_position(idx-1)
            next_node = self.get_position(idx+1)
            prev_node.next = next_node

# Test cases
# Set up some Elements
e1 = Element(1)
e2 = Element(2)
e3 = Element(3)
e4 = Element(4)

# Start setting up a LinkedList
ll = LinkedList(e1)
ll.append(e2)
ll.append(e3)

# Test get_position
# Should print 3
print ll.head.next.next.value
# Should also print 3
print ll.get_position(3).value

# Test insert
ll.insert(e4,3)
# Should print 4 now
print ll.get_position(3).value

# Test delete
ll.delete(1)
# Should print 2 now`
print ll.get_position(1).value
# Should print 4 now
print ll.get_position(2).value
# Should print 3 now
print ll.get_position(3).value
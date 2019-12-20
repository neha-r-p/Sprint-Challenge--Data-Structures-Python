from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #set current to item that is going to be added
        if self.current is None:
            self.current = self.storage.head
        # [5,8,7,3]
        #if ring buffer is full, overwrite the oldest node(head)
        if self.storage.length == self.capacity:
            self.current.value = item
            self.current = self.current.next
            return
        #if not add to tail
        self.storage.add_to_tail(item)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here
        #start at node from tail and append value to list until next is none
        node = self.storage.head
        while node:
            list_buffer_contents.append(node.value)
            node = node.next

        


        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

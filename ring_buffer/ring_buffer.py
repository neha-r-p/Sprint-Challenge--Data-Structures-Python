from doubly_linked_list import DoublyLinkedList


class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.current = None
        self.storage = DoublyLinkedList()

    def append(self, item):
        #set current to item that is going to be added
        self.current = item
        #if ring buffer is full, overwrite the oldest node(tail) and add to front
        if self.storage.length == self.capacity:
            self.storage.tail.value = self.current
            self.storage.move_to_front(self.storage.tail)
            return
        #if not add to head
        self.storage.add_to_head(self.current)


    def get(self):
        # Note:  This is the only [] allowed
        list_buffer_contents = []

        # TODO: Your code here

        return list_buffer_contents

# ----------------Stretch Goal-------------------


class ArrayRingBuffer:
    def __init__(self, capacity):
        pass

    def append(self, item):
        pass

    def get(self):
        pass

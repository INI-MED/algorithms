class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class Hashtable:
    def __init__(self, size):
        self.data = [Node()] * size
        self.size = size

    def hash_function(self, key, size):
        return key % size

    def put(self, key):
        hash_value = self.hash_function(key, self.size)
        if self.data[hash_value].data is None:
            self.data[hash_value].data = key
        else:
            temp = Node(key)
            p = self.data[hash_value]
            while p.next is not None:
                p = p.next
            p.next = temp

    def get(self, key):
        hash_value = self.hash_function(key, self.size)
        if self.data[hash_value].data == key:
            return True
        else:
            p = self.data[hash_value]
            while p is not None and p.data != key:
                p = p.next
            if p is not None and p.data == key:
                return True
        return False

    def delete(self, key):
        if not self.get(key):
            return 'Delete Error'
        hash_value = self.hash_function(key, self.size)
        if self.data[hash_value].data == key:
            self.data[hash_value].data = None
        else:
            p = self.data[hash_value]
            pre = None
            while p is not None and p.data != key:
                pre = p
                p = p.next
            if p is None:
                return 'Delete Error'
            else:
                pre.next = p.next

class BinarySearchTree:

    def __init__(self): 
        self.root = None
        self.size = 0 

    def length(self) -> int: 
        return self.size
    
    def __len__(self) -> int: 
        return self.size
    
    def __iter__(self): 
        return self.root.__iter__()

    def put(self, key, val) -> None: 
        if self.root: 
            self._put(key, val, self.root) 
        else: 
            self.root = TreeNode(key, val) 

        self.size += 1 

    def _put(self, key, val, curr_node) -> None: 
        if key < curr_node.key: 
            if curr_node.has_left_child(): 
                self._put(key, val, curr_node.left_child)
            else: 
                curr_node.left_child = TreeNode(key, val, parent=curr_node)
        else:
            if curr_node.has_right_child(): 
                self._put(key, val, curr_node.right_child) 
            else: 
                curr_node.right_child = TreeNode(key, val, parent=curr_node) 
    
    def __setitem__(self, k, v): 
        self.put(k, v)

    def get(self, key):
        if self.root: 
            res = self._get(key, self.root)
            if res: 
                return res.payload
            else: 
                return None
        else: 
            return None

    def _get(self, key, curr_node): 
        if not curr_node: 
            return None 
        elif curr_node.key == key: 
            return curr_node
        elif key < curr_node.key: 
            return self._get(key, curr_node.left_child)
        else: 
            return self._get(key, curr_node.right_child) 

    def __getitem__(self, key): 
        return self.get(key) 

    def __contains__(self, key) -> bool: 
        if self._get(key, self.root): 
            return True 
        return False 

    def delete(self, key): 
        if self.size > 1: 
            node_to_rmv = self._get(key, self.root) 
            if node_to_rmv:
                self._remove(node_to_rmv)
                self.size -= 1
            else:
                raise KeyError("Key not in the tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Key not in the tree")

    def __delitem__(self, key): 
        self.delete(key)

    @staticmethod
    def _remove(curr_node):
        if curr_node.is_leaf():
            if curr_node.is_left_child():
                curr_node.parent.left_child = None
            else:
                curr_node.parent.right_child = None
        elif curr_node.has_any_children():
            if curr_node.has_left_child():
                if curr_node.is_left_child():
                    curr_node.left_child.parent = curr_node.parent
                    curr_node.parent.left_child = curr_node.left_child
                elif curr_node.is_right_child():
                    curr_node.parent.right_child = curr_node.left_child
                    curr_node.left_child.parent = curr_node.parent
            else:
                curr_node.replace_node_data(curr_node.left_child.key, curr_node.left_child.payload,
                                            curr_node.left_child.left_child, curr_node.left_child.left_child)
        else:
            if curr_node.is_left_child():
                curr_node.right_child.parent = curr_node.parent
                curr_node.parent.left_child = curr_node.right_child
            elif curr_node.is_right_child():
                curr_node.right_child.parent = curr_node.parent
                curr_node.parent.right_child = curr_node.right_child
            else:
                curr_node.replace_node_data(curr_node.right_child.key, curr_node.right_child.payload,
                                            curr_node.right_child.left_child, curr_node.right_child.right_child)

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):

        succ = None
        if self.has_right_child():
            succ = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    succ = self.parent
                else:
                    self.parent.right_child = None
                    succ = self.parent.find_successor()
                    self.parent.right_child = self
        return succ

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current


class TreeNode: 

    def __init__(self, key, val, left=None, right=None, parent=None):
        self.key = key 
        self.payload = val
        self.left_child = left 
        self.right_child = right 
        self.parent = parent

    def has_left_child(self): 
        return self.left_child 
    
    def has_right_child(self): 
        return self.right_child 

    def is_left_child(self) -> bool: 
        return self.parent and self.parent.left_child == self

    def is_right_child(self) -> bool: 
        return self.parent and self.parent.right_child == self 

    def is_root(self):
        return self.parent

    def is_leaf(self) -> bool: 
        return not (self.right_child or self.left_child)
    
    def has_any_children(self) -> bool: 
        return self.right_child or self.left_child

    def replace_node_data(self, key, value, lc, rc) -> None:
        self.key = key 
        self.payload = value 
        self.left_child = lc 
        self.right_child = rc 
        if self.has_left_child():
            self.left_child.parent = self 
        if self.has_right_child(): 
            self.right_child.parent = self


if __name__ == '__main__':
    mytree = BinarySearchTree()
    mytree[3] = "red"
    mytree[4] = "blue"
    mytree[6] = "yellow"
    mytree[2] = "at"

    print(mytree[6])
    print(mytree[2])

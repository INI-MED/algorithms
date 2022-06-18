import time
from random import shuffle


class BinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self) -> str:
        return f"{self.val}"


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, val, parent=None):
        if parent is None:
            parent = self.root
        if parent is None:
            self.root = BinaryTreeNode(val)
            return
        elif val < parent.val:
            if parent.left is None:
                parent.left = BinaryTreeNode(val)
                return
            else:
                self.insert(val, parent.left)
        else:
            if parent.right is None:
                parent.right = BinaryTreeNode(val)
                return
            else:
                self.insert(val, parent.right)

    def find(self, val, node=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        elif val == node.val:
            return node
        elif val < node.val:
            if node.left is not None:
                left_rv = self.find(val, node.left)
                if left_rv is not None:
                    return left_rv
        elif val > node.val:
            if node.right is not None:
                right_rv = self.find(val, node.right)
                if right_rv is not None:
                    return right_rv
        return None


class SplayTree(BinaryTree):

    def find(self, val, node=None, p=None, g=None, gg=None):
        if node is None:
            node = self.root
        if node is None:
            return None
        elif val == node.val:
            if p is not None:
                if g is None:
                    self.rotate_up(node, p, g)
                elif g.left == p and p.left == node or g.right == p and p.right == node:
                    self.rotate_up(p, g, gg)
                    self.rotate_up(node, p, gg)
                else:
                    self.rotate_up(node, p, g)
                    self.rotate_up(node, g, gg)
            return node
        elif val < node.val:
            if node.left is not None:
                left_rv = self.find(val, node.left, node, p, g)
                if left_rv is not None:
                    return left_rv
        elif val > node.val:
            if node.right is not None:
                right_rv = self.find(val, node.right, node, p, g)
                if right_rv is not None:
                    return right_rv
        return None

    def rotate_up(self, node, parent, gp=None):
        if node == parent.left:
            parent.left = node.right
            node.right = parent
            if self.root == parent:
                self.root = node
        elif node == parent.right:
            parent.right = node.left
            node.left = parent
            if self.root == parent:
                self.root = node
        else:
            print("This is impossible")

            if gp is not None:
                if gp.right == parent:
                    gp.right = node
                elif gp.left == parent:
                    gp.left = node


def test_splay_tree(treesize=100000, iters=20000):
    """Just a simple test harness to demonstrate the speed of
    splay trees when a few items are searched for very frequently."""
    # Build a binary tree and a splay tree
    print("Building trees")
    bintree = BinaryTree()
    spltree = SplayTree()
    x = [i for i in range(0, treesize)]
    shuffle(x)
    for n in x:
        bintree.insert(n)
        spltree.insert(n)
    print("Done building")
    searches = x[-20:]

    # Search the splay tree 1000 times
    t1 = time.time()
    for i in range(0, iters):
        for n in searches:
            node = spltree.find(n)
            if node is None:
                print("ERROR: %d" % n)
    t2 = time.time()
    print("Searched for 20 items %dx in splay tree: %.1f sec" % (iters, t2 - t1))

    # Search the binary tree 1000 times
    t1 = time.time()
    for i in range(0, iters):
        for n in searches:
            node = bintree.find(n)
            if node is None:
                print("ERROR: %d" % n)
    t2 = time.time()
    print("Searched for 20 items %dx in binary tree: %.1f sec" % (iters, t2 - t1))


test_splay_tree()

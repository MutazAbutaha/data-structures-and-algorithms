from stack_queue import Node, Queue, Stack
import os

class Tnode:
    """
    Class representing a node in a binary tree.
    """

    def __init__(self, value):
        """
        Initialize a new instance of the Tnode class.

        Args:
            value: The value to be stored in the node.
        """
        self.value = value
        self.right = None
        self.left = None


class Tree:
    """
    Class representing a binary tree.
    """

    def __init__(self):
        """
        Initialize a new instance of the Tree class.
        """
        self.root = None

    def breadth_first(self):
        """
        Perform a breadth-first traversal of the binary tree.

        Returns:
            A list containing the values of the nodes in breadth-first order.
        """
        if not self.root:
            return self.root

        output = []
        queue = Queue()
        queue.enqueue(self.root)

        while not queue.is_empty():
            front = queue.dequeue()
            output.append(front.value)

            if front.left:
                queue.enqueue(front.left)
            if front.right:
                queue.enqueue(front.right)

        return output

    def pre_order(self):
        """
        Perform a pre-order traversal of the binary tree.

        Returns:
            A list containing the values of the nodes in pre-order.
        """
        output = []

        def _walk(root):
            output.append(root.value)
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def in_order(self):
        """
        Perform an in-order traversal of the binary tree.

        Returns:
            A list containing the values of the nodes in in-order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            output.append(root.value)
            if root.right:
                _walk(root.right)

        _walk(self.root)
        return output

    def post_order(self):
        """
        Perform a post-order traversal of the binary tree.

        Returns:
            A list containing the values of the nodes in post-order.
        """
        output = []

        def _walk(root):
            if root.left:
                _walk(root.left)
            if root.right:
                _walk(root.right)
            output.append(root.value)

        _walk(self.root)
        return output


class BinarySearchTree(Tree):
    """
    Class representing a binary search tree.
    """

    def __init__(self):
        """
        Initialize a new instance of the BinarySearchTree class.
        """
        super().__init__()

    def add(self, value):
        """
        Add a value to the binary search tree.

        Args:
            value: The value to be added.
        """
        if not self.root:
            self.root = Tnode(value)
            return

        def _add_node(node, value):
            if value < node.value:
                if node.left:
                    _add_node(node.left, value)
                else:
                    node.left = Tnode(value)
            elif value > node.value:
                if node.right:
                    _add_node(node.right, value)
                else:
                    node.right = Tnode(value)

        _add_node(self.root, value)

    def contains(self, value):
        """
        Check if the binary search tree contains a value.

        Args:
            value: The value to be checked.

        Returns:
            True if the value is found, False otherwise.
        """
        def _search(node, value):
            if not node:
                return False
            if node.value == value:
                return True
            if value < node.value:
                return _search(node.left, value)
            else:
                return _search(node.right, value)

        return _search(self.root, value)
    

    def get_max(self):
        """
        this function  Returns the maximum value of the given tree
        """
        node = self.root
        def __max(node):
            _max = 0
            if  node.value > _max :
                _max = node.value
                if node.left :
                    if node.left.value > _max :
                        _max = node.left.value
                        return __max(node.left)
                if node.right :
                    if node.right.value > _max :
                        _max = node.right.value
                        return __max(node.right)
            return _max
        return __max(node)
    
    def leafs_of_trees(self):
        node = self.root

        def num_of_leafs(node):
                counter = 0
            # if node.value :
                if  node.left is None and  node.right is None :
                    counter += 1
                elif node.left :
                    num_of_leafs(node.left)
                elif node.right :
                    num_of_leafs(node.right)
                return counter
        return num_of_leafs(node)
    

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.add(10)
    bst.add(20)
    bst.add(100)
    bst.add(15)
    bst.add(25)
    bst.add(5)
    print("breadth")
    print(bst.breadth_first())
    print("pre_order")
    print(bst.pre_order())
    print("in_order")
    print(bst.in_order())
    print("post_order")
    print(bst.post_order())

    print("Contains 20:", bst.contains(20))
    print("Contains 30:", bst.contains(30))
    print(bst.get_max())
    print(bst.leafs_of_trees())


#2
# class Tnode:
#     """
#     Class representing a node in a binary tree.
#     """

#     def __init__(self, value):
#         """
#         Initialize a new instance of the Tnode class.

#         Args:
#             value: The value to be stored in the node.
#         """
#         self.value = value
#         self.right = None
#         self.left = None


# class Tree:
#     """
#     Class representing a binary tree.
#     """

#     def __init__(self):
#         """
#         Initialize a new instance of the Tree class.
#         """
#         self.root = None

#     def breadth_first(self):
#         """
#         Perform a breadth-first traversal of the binary tree.

#         Returns:
#             A list containing the values of the nodes in breadth-first order.
#         """
#         if not self.root:
#             return self.root

#         output = []
#         queue = Queue()
#         queue.enqueue(self.root)

#         while not queue.is_empty():
#             front = queue.dequeue()
#             output.append(front.value)

#             if front.left:
#                 queue.enqueue(front.left)
#             if front.right:
#                 queue.enqueue(front.right)

#         return output

#     def pre_order(self):
#         """
#         Perform a pre-order traversal of the binary tree.

#         Returns:
#             A list containing the values of the nodes in pre-order.
#         """
#         output = []

#         def _walk(root):
#             output.append(root.value)
#             if root.left:
#                 _walk(root.left)
#             if root.right:
#                 _walk(root.right)

#         _walk(self.root)
#         return output

#     def in_order(self):
#         """
#         Perform an in-order traversal of the binary tree.

#         Returns:
#             A list containing the values of the nodes in in-order.
#         """
#         output = []

#         def _walk(root):
#             if root.left:
#                 _walk(root.left)
#             output.append(root.value)
#             if root.right:
#                 _walk(root.right)

#         _walk(self.root)
#         return output

#     def post_order(self):
#         """
#         Perform a post-order traversal of the binary tree.

#         Returns:
#             A list containing the values of the nodes in post-order.
#         """
#         output = []

#         def _walk(root):
#             if root.left:
#                 _walk(root.left)
#             if root.right:
#                 _walk(root.right)
#             output.append(root.value)

#         _walk(self.root)
#         return output


# class BinarySearchTree(Tree):
#     """
#     Class representing a binary search tree.
#     """

#     def __init__(self):
#         """
#         Initialize a new instance of the BinarySearchTree class.
#         """
#         super().__init__()

#     def add(self, value):
#         """
#         Add a value to the binary search tree.

#         Args:
#             value: The value to be added.
#         """
#         if not self.root:
#             self.root = Tnode(value)
#             return

#         def _add_node(node, value):
#             if value < node.value:
#                 if node.left:
#                     _add_node(node.left, value)
#                 else:
#                     node.left = Tnode(value)
#             elif value > node.value:
#                 if node.right:
#                     _add_node(node.right, value)
#                 else:
#                     node.right = Tnode(value)

#         _add_node(self.root, value)

#     def contains(self, value):
#         """
#         Check if the binary search tree contains a value.

#         Args:
#             value: The value to be checked.

#         Returns:
#             True if the value is found, False otherwise.
#         """
#         def _search(node, value):
#             if not node:
#                 return False
#             if node.value == value:
#                 return True
#             if value < node.value:
#                 return _search(node.left, value)
#             else:
#                 return _search(node.right, value)

#         return _search(self.root, value)

#     def get_max(self):
#         """
#         Returns the maximum value of the given tree.
#         """
#         node = self.root

#         def __max(node):
#             _max = node.value
#             if node.left:
#                 left_max = __max(node.left)
#                 _max = max(_max, left_max)
#             if node.right:
#                 right_max = __max(node.right)
#                 _max = max(_max, right_max)
#             return _max

#         return __max(node)

#     def count_files(self, directory):
#         count = 0
#         for root, dirs, files in os.walk(directory):
#             count += len(files)
#         return count

#     def compare_directories(self, directory1, directory2):
#         file_count1 = self.count_files(directory1)
#         file_count2 = self.count_files(directory2)
        
#         if file_count1 == file_count2:
#             print(True)
#         else:
#             print(False)


# if __name__ == "__main__":
#     bst = BinarySearchTree()
#     bst.add(10)
#     bst.add(20)
#     bst.add(100)
#     bst.add(15)
#     bst.add(25)
#     bst.add(5)
#     print("breadth")
#     print(bst.breadth_first())
#     print("pre_order")
#     print(bst.pre_order())
#     print("in_order")
#     print(bst.in_order())
#     print("post_order")
#     print(bst.post_order())

#     print("Contains 20:", bst.contains(20))
#     print("Contains 30:", bst.contains(30))
#     print(bst.get_max())

#     directory1 = '/path/to/directory1'
#     directory2 = '/path/to/directory2'
#     bst.compare_directories(directory1, directory2)

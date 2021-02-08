class BinTree:
    def __init__(self, root) -> None:
        self.root = root

    def equals(self, another_tree) -> bool:
        return self.in_order_traversal() == another_tree.in_order_traversal()

    def pre_order_traversal(self, print_nodes=False) -> list:
        def visit(root):

            # Visit this node
            visited.append(root.value)
            if print_nodes:
                print(root.value)

            # Visit left child of this node
            if root.left:
                visit(root.left)

            # Visit right child of this node
            if root.right:
                visit(root.right)
        
        visited = []
        visit(self.root)  # start at root of tree
        return visited

    def in_order_traversal(self, print_nodes=False) -> list:
        def visit(root):
            # Visit left child of this node
            if root.left:
                visit(root.left)

            # Visit this node
            visited.append(root.value)
            if print_nodes:
                print(root.value)

            # Visit right child of this node
            if root.right:
                visit(root.right)
        
        visited = []
        visit(self.root)  # start at root of tree
        return visited

    def post_order_traversal(self, print_nodes=False) -> list:
        def visit(root):
            # Visit left child of this node
            if root.left:
                visit(root.left)

            # Visit right child of this node
            if root.right:
                visit(root.right)

            # Visit this node
            visited.append(root.value)
            if print_nodes:
                print(root.value)
        
        visited = []
        visit(self.root)  # start at root of tree
        return visited

    def __str__(self) -> str:
        nodes_list = self.in_order_traversal()
        return str(nodes_list)
    
class Node:
    def __init__(self, value, left=None, right=None) -> None:
        self.value = value
        self.left = left
        self.right = right

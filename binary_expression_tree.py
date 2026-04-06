from stack import Stack


class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class BinaryExpressionTree:
    def __init__(self):
        self.root = None

    def is_operator(self, token):
        return token in ['+', '-', '*', '/']

    def build_tree(self, postfix_expression):
        stack = Stack()
        tokens = postfix_expression.split()

        for token in tokens:
            if token.replace('.', '', 1).isdigit():
                stack.push(Node(token))
            elif self.is_operator(token):
                if stack.size() < 2:
                    raise Exception("Error: Not enough operands")

                node = Node(token)
                node.right = stack.pop()
                node.left = stack.pop()
                stack.push(node)
            else:
                raise Exception(f"Error: Unsupported token '{token}'")

        if stack.size() != 1:
            raise Exception("Error: Invalid postfix expression")

        self.root = stack.pop()

    def evaluate(self):
        return self._evaluate_tree(self.root)

    def _evaluate_tree(self, node):
        if node.left is None and node.right is None:
            return float(node.value)

        x = self._evaluate_tree(node.left)
        y = self._evaluate_tree(node.right)

        if node.value == '+':
            return x + y
        elif node.value == '-':
            return x - y
        elif node.value == '*':
            return x * y
        elif node.value == '/':
            return x / y

    def inorder(self):
        return self._inorder(self.root)

    def _inorder(self, node):
        if node is None:
            return ""

        if node.left is None and node.right is None:
            return node.value

        return f"({self._inorder(node.left)} {node.value} {self._inorder(node.right)})"

    def postorder(self):
        return self._postorder(self.root).strip()

    def _postorder(self, node):
        if node is None:
            return ""

        return (
            self._postorder(node.left) +
            self._postorder(node.right) +
            node.value + " "
        )
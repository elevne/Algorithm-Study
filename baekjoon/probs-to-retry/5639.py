import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline


class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self) -> str:
        return f"[data={self.data}, left={self.left}, right={self.right}]"


nodes = []
while True:
    try:
        nodes.append(Node(int(input())))
    except:
        break


class Tree:
    def __init__(self) -> None:
        self.root = None

    def insert(self, node):
        if self.root is None:
            self.root = node
        else:
            root = self.root
            while True:
                # 작으면 left
                if root.data > node.data:
                    if root.left is None:
                        root.left = node
                        break
                    else:
                        root = root.left
                # 크면 right (같은 경우는 없음)
                else:
                    if root.right is None:
                        root.right = node
                        break
                    else:
                        root = root.right


def postorder(node):
    if node is None:
        return
    postorder(node.left)
    postorder(node.right)
    print(node.data)


tree = Tree()
for node in nodes:
    tree.insert(node)

postorder(tree.root)
class Node:
    def __init__(self,data,left_node,right_node):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

# 전위 순회 루트/왼/오
def pre_order(node):
    print(node.data, end='')
    if node.left_node != '.':
        pre_order(tree[node.left_node])
    if node.right_node != '.':
        pre_order(tree[node.right_node])

# 중위 순회
def in_order(node):
    if node.left_node != '.':
        in_order(tree[node.left_node])
    print(node.data, end='')
    if node.right_node != '.':
        in_order(tree[node.right_node])

# 후위 순회 
def post_order(node):
    if node.left_node != '.':
        post_order(tree[node.left_node])
    if node.right_node != '.':
        post_order(tree[node.right_node])
    print(node.data, end='')


n = int(input())
tree = {}
for i in range(n):
    root,left,right = map(str,input().split())
    tree[root] = Node(root,left,right)


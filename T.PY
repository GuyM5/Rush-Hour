path = []
def DFS(self , node):
    if not node:
        return
    path.append(node)
    #Pre Order
    self.DFS(self.leftSon(node))
    #In Order
    self.DFS(self.leftSon(node))
    #Post Order

queue = [1,2,3,4,5]
print(queue.pop(0))

node = 1
action = (1,2)

visited = {node , action}
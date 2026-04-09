class CNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

nodeA = CNode("Player A")
nodeB = CNode("Player B")
nodeC = CNode("Player D")
nodeA.next = nodeB
nodeB.next = nodeC
nodeC.next = nodeA

circular_list = CLinkedList()
circular_list.head = nodeA
circular_list.tail = nodeC

def printCircular(head):
    current = head
    while current != None:
        print(current.data, end=" -> ")
        if current.next == head:
            print("back to start")
            break
        current = current.next
        
def insertAfter(target_node, data):
    if target_node is None:
        return None
    new_node = CNode(data)
    new_node.next = target_node.next
    target_node.next = new_node
    return new_node

print("\n")
printCircular(circular_list.head)

insertAfter(nodeC, "Player C")
print("\n")
printCircular(circular_list.head)
class DNode:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
    
class DLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

nodeA = DNode("In the end")
nodeB = DNode("Disenchanted")
nodeC = DNode("A little piece of heaven")
nodeA.next = nodeB

nodeB.next = nodeC
nodeB.prev = nodeA
nodeC.prev = nodeB

Dlinked_list = DLinkedList()
Dlinked_list.head = nodeA
Dlinked_list.tail = nodeC

def printForward(head): 
    current = head
    while current != None:
        print(current.data, end=" ")
        if current.prev != None and current.next != None:
            print("<->", end=" ")
        else:
            print("->", end=" ")
        current = current.next
    print("None")

def printBackward(tail):
    current = tail
    while current != None:
        print(current.data, end=" ")
        if current.prev != None and current.next != None:
            print("<->", end=" ")
        else:
            print("->", end=" ")
        current = current.prev
    print("None")

def insertAtHead(Dlinked_list, data):
    new_node = DNode(data)
    new_node.next = Dlinked_list.head
    Dlinked_list.head.prev = new_node
    Dlinked_list.head = new_node

def insertAfter(target_node, data):
    if target_node == None:
        return
    new_node = DNode(data)
    new_node.next = target_node.next
    new_node.prev = target_node
    target_node.next.prev = new_node
    target_node.next = new_node

def deleteNode(target_node):
    if target_node is None:
        return
    target_node.prev.next = target_node.next
    target_node.next.prev = target_node.prev 

print("Forward And Backward")
printForward(Dlinked_list.head)
printBackward(Dlinked_list.tail)

print("\nInsert At Head")
insertAtHead(Dlinked_list, "American Idiot")
printForward(Dlinked_list.head)
printBackward(Dlinked_list.tail)

print("\nInsert After")
insertAfter(nodeB, "Drown")
printForward(Dlinked_list.head)
printBackward(Dlinked_list.tail)

print("\nDelete Node")
deleteNode(nodeB)
printForward(Dlinked_list.head)
printBackward(Dlinked_list.tail)
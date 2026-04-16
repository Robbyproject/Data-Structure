class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, data):
        self.items.append(data)
    def dequeue(self):
        if self.isEmpty():
            return "Queue kosong"
        return self.items.pop(0)
    def peek(self):
        if self.isEmpty():
            return "Queue kosong"
        return self.items[0]
    def isEmpty(self):
        return len(self.items) == 0
    def display(self):
        print(self.items)

class Stack:
    def __init__(self):
        self.items = []
    def push(self, data):
        self.items.append(data)
    def pop(self):
        if self.isEmpty():
            return "Stack kosong"
        return self.items.pop()
    def peek(self):
        if self.isEmpty():
            return "Stack kosong"
        return self.items[-1]
    def isEmpty(self):
        return len(self.items) == 0
    def display(self):
        print(self.items)

class RequestSystem:
    def __init__(self):
        self.waitingQueue = Queue()
        self.processedStack = Stack()
    def addRequest(self, request):
        self.waitingQueue.enqueue(request)
        print("Request Added")
    def processRequest(self):
        if not self.waitingQueue.isEmpty():
            processedRequest = self.waitingQueue.dequeue()
            self.processedStack.push(processedRequest)
            print("Request Processed")
    def undo(self):
        self.processedStack.pop()

mySystem = RequestSystem()

mySystem.addRequest("Request 1")
mySystem.addRequest("Request 2")
mySystem.addRequest("Request 3")
print(mySystem.waitingQueue.items)

print("KONDISI AWALA")
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)

print("PROSES PERTAMA")
mySystem.processRequest()
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)

print("PROSES KEDUA")
mySystem.processRequest()
mySystem.processRequest()
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)

print("PROSES KETIGA")
mySystem.processRequest()
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)

print("PROSES UNDO PERTAMA")
mySystem.undo()
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)

print("PROSES UNDO KEDUA")
mySystem.undo()
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)

print("PROSES UNDO KETIGA")
mySystem.undo()
print(mySystem.waitingQueue.items)
print(mySystem.processedStack.items)
# class Stack:
#     def __init__(self):
#         self.items = []
#     def push(self,data):
#         self.items.append(data)
#     def pop(self):
#         if self.is_empty():
#             return "Stack Kosong"
#         return self.itmes.pop()
#     def peek(self):
#         if self.is_empty():
#             return
#         return self.items[len(self.items) -1]
#     def isEmpty(self):
#         return self.items == []
#     def display(self):
#         for i in range(len(self.items)-1,-1,-1):
#             print(self.items[i])

class Stack:
    def __init__(self):
        self.item = []
    def push(self,item):
        self.item.append(item)
    def pop(self):
        if self.item == []:
            print("Empty pop")
        else:
            self.item.pop()
    def isEmpty(self):
        return self.item == []
    def peek(self):
        if self.isEmpty():
            return
        return self.item[len(self.item) -1]
    def display(self):
        print(self.item)

    def BlanceStack(self, string):
        stack = []
        for char in string:
            match char:
                case "(" | "[" | "{":
                    stack.append(char)
                case ")":
                    if not stack or stack.pop() != "(":
                        return False
                case "]":
                    if not stack or stack.pop() != "[":
                        return False
                case "}":
                    if not stack or stack.pop() != "{":
                        return False
        return len(stack) == 0


myStack = Stack()
myStack.push(10)
myStack.display()

myStack.push(20)
myStack.push(30)
myStack.display()

myStack.pop()
myStack.display()

myStack.isEmpty()
myStack.peek()
myStack.BlanceStack("[Ayam")
BStack = Stack()

input_user = "())"

print({input_user},{BStack.BlanceStack(input_user)})
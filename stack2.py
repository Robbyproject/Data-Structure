class BStack:
    def __init__(self,string):
        self.string = string
    def display(self):
        print(self.string)
    def checkBalancedParenthesis(self):
        if self.string is not None:
            tempStack = Stack()
            for char in self.value:
                if char == "(":
                    tempStack.push(char)
                elif char == ")":
                    if tempStack.isEmpty():
                        return False
                    else:
                        tempStack.pop()
                    if tempStack.isEmpty():
                        return True
                    else:
                        return False
                else:
                    print("Empty Expression")

CStack = BStack()

# class MyStructure:
#     def __init__(self):
#         self.data = []
#     def add(self, value):
#         self.data.append(value)
#     def remove(self):
#         if len(self.data) == 0:
#             return None
#         return self.data.pop(0)

# stuktur = MyStructure()
# print(MyStructure())

def is_palindrome(s):
    if len(s) <= 1:
        return True
    if s[0] != s[-1]:
        return False
    return is_palindrome(s[1:-1])
print(is_palindrome("radar"))
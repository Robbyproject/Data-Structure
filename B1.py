# def hitung_sesuatu(data):
#     total = 0
#     minimum = data[0]
#     for x in data:
#         total += x
#     for y in data:
#         if y < minimum:
#         minimum = y
#     return total, minimum

# print(hitung_sesuatu)

# data = [10,20,30,40,50,60]

# def misteri(data):
#     n = len(data)
#     for i in range(n):
#         for j in range(i + 1, n):
#             for k in range(j + 1, n):
#                 print(data[i], data[j], data[k])
# print(misteri(data))

n = [1,2,3,4,5,6]

def jejak(n):
    if n <= 0:
        return 0
    print("*" * n)
    return n + jejak(n - 2)

print(jejak(6))
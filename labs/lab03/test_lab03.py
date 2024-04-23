# def repeated(f, n):
#     if n == 0:
#         def identity(x):
#             return x
#         return identity
#     else:
#         return compose1(f, repeated(f, n-1))

# def compose1(f, g):
    
#     def h(x):
#         return f(g(x))
#     return h
    
# def f(x):
#     return x + 1

# repeated(f, 2)(5)


import lab03

# x = lab03.num_eights(88888888)
# print(x)

print(lab03.pingpong(1))
print(lab03.pingpong(2))
print(lab03.pingpong(3))
print(lab03.pingpong(4))
print(lab03.pingpong(5))
print(lab03.pingpong(6))
print(lab03.pingpong(7))
print(lab03.pingpong(8))
print(lab03.pingpong(9))
print(lab03.pingpong(10))
print(lab03.pingpong(11))
print(lab03.pingpong(12))
print(lab03.pingpong(13))

print()
print(lab03.pingpong(30))
print(lab03.pingpong(68))
print(lab03.pingpong(69))
print(lab03.pingpong(80))
print(lab03.pingpong(81))
print(lab03.pingpong(82))
print(lab03.pingpong(100))


# iterable - __iter__() or __getitem__()

# iterator - __next__()

# iteration -

def gen(n):
    for i in range(n):
        yield i


# g = gen(3)
# print(g)
# print(g.__next__())
# print(g.__next__())
# print(g.__next__())

# for i in g:
#     print(i)

h = "kushal"
ier = iter(h)
print(ier.__next__())
print(ier.__next__())

# print(iter(h))
# for c in h:
#     print(c)








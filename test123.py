

# for i in range(1,4,1):
#     for j in range(1,4,1):
#         k = i*j
#         print("{i} * {j} = {k}".format(i=i, j=j, k=k))

# import numpy
# book = []
# for i in range(1,10,1):
#     for j in range(1,10,1):
#         k = i*j
#         book.append("{j} * {i} = {k}".format(j=j, i=i, k=k)) 
# for a in range(0,81,9): 
#     print(book[a:a+9:1])

def split_list(lst,n):
    for a in range(0, len(lst), n):
        yield lst[a:a+n]

import numpy
book = []
for i in range(1,10,1):
    for j in range(1,10,1):
        k = i*j
        book.append("{k:2}".format(i=i, j=j, k=k))
n=9
newlst = list(split_list(book,n))
newnewlst = numpy.array(newlst)
print(newnewlst)

# for a in range(0,81,9):
#     book1 = book[a:a+9:1]
#     book2 = array([book2,book1])
#     print(book2)




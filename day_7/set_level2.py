A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}

print('================One====================')

A.union(B)
print(A.union(B))

print('================Two====================')

A.intersection(B)
print(A.intersection(B))

print('================Three====================')

A.issubset(B)
print(A.issubset(B))

print('================Four====================')

print(A.isdisjoint(B))


print('================Five====================')
union_ab =B. union(A)
union_ba = A.union(B)

joint_AB = union_ab.subset(

print('================Six====================')

print(A.isdisjoint(B))

print('================Seven====================')

del A
del B

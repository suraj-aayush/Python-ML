s1 = {1,2,34.4}
print(s1)

mix = {1,3,4,"qffsd", 8.0}
print(mix)

s2 = s1.union(mix)
print(s2)

s1.add(55)
print(s1)

print("new s1 is ")
print(s1)

print("s1 se remove 2")
s1.remove(2)
print(s1)

print("intersection")
print(s1.intersection(mix))

print("set diff")
print(s1.difference(mix))
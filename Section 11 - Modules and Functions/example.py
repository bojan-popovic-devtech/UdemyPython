import shelve

print(dir())
print()
for m in dir(shelve.Shelf):
    print(m)

help(shelve)
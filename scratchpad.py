MyList = ["b", "a", "a", "c", "b", "a", "c", 'a']
res = {}

for i in MyList:
    res[i] = MyList.count(i)

print(res)
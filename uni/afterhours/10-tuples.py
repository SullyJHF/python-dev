myList = [1, 2, 3]
myList.append(4)
print(myList)

myTuple = (1, 2, 3)
print(myTuple)

#can't do this!
#myTuple.append(4)

myList = list(myTuple)
myList.append(4)
print(myList)
print(myTuple)
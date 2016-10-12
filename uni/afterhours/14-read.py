f = open('14-test.txt', 'r') # opens file in read mode

print(f.readline())
print(f.readline())

print(f.read(1))
print(f.read())

f.close()

f2 = open('14-test.txt', 'r')

myList = []
for line in f2:
  myList.append(line)

f2.close()

print(myList)
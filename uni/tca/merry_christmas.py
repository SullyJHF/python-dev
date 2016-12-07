file = open('Words.txt', 'w')
file.write('Merry Christmas!')
file.close()

file = open('Words.txt', 'r')
print(file.read())
file.close()

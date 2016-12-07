with open('Words.txt', 'w') as write_file:
  write_file.write('Merry Christmas!')

with open('Words.txt', 'r') as read_file:
  text = read_file.read()
  print(text)

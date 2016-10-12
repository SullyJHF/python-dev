var1 = '1'

try:
  var1 = var1 + 1 # since var1 is a string 1 cannot be added to it
except:
  print(var1, "is not a number") # so we execute this

print(var1)


try:
  var2 = var1 + 1 # since var1 is a string 1 cannot be added to it
except:
  var2 = int(var1) + 1

print(var2)
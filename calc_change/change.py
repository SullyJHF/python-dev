coins = [200,100,50,20,10,5,2,1]
change = []

def calc_change (n):
  for x in coins:
    if(n - x >= 0):
      return [x] + calc_change(n - x)
  return []

print("input: 94 output:", calc_change(94))
print("input: 73 output:", calc_change(73))

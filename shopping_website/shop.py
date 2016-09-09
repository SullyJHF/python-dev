class Customer:
  def __init__(self, name, address):
    self.name = name
    self.address = address
    self.cards = []
    self.orders = []

  def __str__(self):
    return '{} lives at {}'.format(self.name, self.address)

  def create_order(self, card):
    if(len(card) != 16):
      print('invalid card details')
      return
    self.orders.append(Order())

  def add_card(self, card_number):
    self.cards.append(card_number)


class Item:
  def __init__(self, name, price):
    self.name = name
    self.price = price

class Order:
  def __init__(self):
    self.status = 'processing'
    self.items = []
    self.total = 0.0

  def add_item(self, item):
    self.items.append(item.name)
    self.total += item.price

  def checkout(self):
    self.status = 'completed'





fred = Customer('Fred', '123 Crescent Walkway')
fred.add_card('1479201859201121')
fred.create_order(fred.cards[0])

fred.orders[0].add_item(Item('Banana', 5.60))
fred.orders[0].add_item(Item('Kiwi', 6.90))
fred.orders[0].add_item(Item('Caleb\'s smelly sock', 943.76))
fred.orders[0].add_item(Item('B-rad Hover Board', 15899.99))

fred.orders[0].checkout()


print(fred.orders[0].status)
print(fred.orders[0].items)
print('${:.2f}'.format(fred.orders[0].total))

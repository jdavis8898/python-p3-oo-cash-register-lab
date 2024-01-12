#!/usr/bin/env python3
import ipdb

class CashRegister:
  
  def __init__(self, discount=0, total=0, items=None):

    self.total = total
    self.discount = discount

    if items is None:
      self.items = []
    else:
      self.items = items
  
  def add_item(self, item, price, quantity=1):

    counter = quantity
    self.last_price = price * quantity

    while counter > 0:
      self.items.append(item)
      counter -= 1

    self.total += (price * quantity)

  def apply_discount(self):

    if(self.discount > 0):
      self.total -= int(self.total * (self.discount * .01))
      print(f"After the discount, the total comes to ${self.total}.")
    
    else:
      print("There is no discount to apply.")

  def void_last_transaction(self):

    self.total -= self.last_price
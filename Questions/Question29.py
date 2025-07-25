# Shopping Cart Class

# Write a Python program to create a class representing a shopping cart. Include methods for adding and removing items, and calculating the total price.


class ShoppingCart:
    def __init__(self,cart):
        self.cart = cart

    def addItem(self,item,price):
        self.cart[item] = price

    def deleteItem(self,item):
        del self.cart[item]

    def displayCart(self) :
        for i in self.cart:
            print(f"{i} : {self.cart[i]}")

    def calculateTotalPrice(self):
        total = 0
        for i in self.cart:
            total = total + self.cart[i]

        print("Total Price is " , total)
    
obj = ShoppingCart({})

obj.addItem("tomato", 25)
obj.addItem("potato", 25)
# obj.deleteItem("tomato")
obj.displayCart()
obj.calculateTotalPrice()
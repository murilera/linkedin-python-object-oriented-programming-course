# definitions
## class: a blueprint for creating objects of a particular type
## methods: regular functions that are part of a class
## attributes: vartiables that hold data that are part of a class
## object: a specific instance of a class
## inheritance: means by which a class can inherit capabilities from another
## composition: means building ocmplex objects out of other objects


### definition_start
class Book:
    def __init__(self, title, author, pages, price):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = 'secret attr'
        
    def getprice(self):
        if hasattr(self, "_discount"):
            return self.price - (self.price * self._discount)
        else:
            return self.price
    
    def setdiscount(self, amount):
        self._discount = amount

b1 = Book("Brave", "Leo", 1225, 39.95)
b2 = Book("War", "JD", 234, 29.95)

print(b1)
print(b1.title)

print(b1.getprice())

b1.setdiscount(0.10)
print(b1.getprice())

# print(b1.__secret)
print(b1._Book__secret)

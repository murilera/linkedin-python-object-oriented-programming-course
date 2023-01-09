class Book:
    def __init__(self, title):
        self.title = title
        
class Newspaper:
    def __init__(self, name) -> None:
        self.name = name
        

b1 = Book("Catcher")
b2 = Book("Grapes")

n1 = Newspaper("Washington")
n2 = Newspaper("New York")

print(type(b1))
print(type(n1))

print(type(b1) == type(b2))
print(type(b1) == type(n2))

print(isinstance(b1, Book))
print(isinstance(n1, Newspaper))
print(isinstance(n2, object))
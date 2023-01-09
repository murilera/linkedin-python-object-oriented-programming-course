class Book:
    BOOK_TYPES = ("HARD", "PAPER", "EBOOK")
    
    __booklist = None
    
    @classmethod
    def getbooktypes(cls):
        return cls.BOOK_TYPES
    
    @staticmethod
    def getbooklist():
        if Book.__booklist is None:
            Book.__booklist = []
        return Book.__booklist
            
        
    def setTitle(self, newtitle):
        self.title = newtitle
    
    def __init__(self, title, booktype) -> None:
        self.title = title
        if (not booktype in Book.BOOK_TYPES):
            raise ValueError(f"{booktype} is not a valid book type")
        else:
            self.booktype = booktype
            
print("book types: ", Book.getbooktypes())

b1 = Book("title 1", "HARD")
# b2 = Book("title 2", "COMIC")
b2 = Book("title 2", "PAPER")


thebooks = Book.getbooklist()
thebooks.append(b1)
thebooks.append(b2)
print(thebooks)
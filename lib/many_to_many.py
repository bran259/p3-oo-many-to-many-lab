class Author:
    all = []
    def __init__(self, name):
        self.name = name
        Author.all.append(self)
    pass
    def contracts(self):
        "Returns a list of Contract objects related to this author."
        return [contract for contract in Contract.all if contract.author == self]
    
    def books(self):
        "Returns a list of related Books that the author has contracts with"
        return [contract.book for contract in self.contracts()]  
          
    def sign_contract(self, book, date, royalties):
        "Creates and returns a new Contract with this author and the given book."
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")

        return Contract(self, book, date, royalties)
    
    def total_royalties(self):
        "Return the sum of royalties from all the author's contracts."
        return sum(contract.royalties for contract in self.contracts())

class Book:
    all = []
    def __init__(self, title):
        self.title = title
        Book.all.append(self)

    def contracts(self):
        "returns a list of Contract objects related to this Book."
        return [contract for contract in Contract.all if contract.book == self] 

    def authors(self):
        "Returns a list of Authors who have written this Book."        
        return [contract.author for contract in self.contracts()]  
    pass
       


class Contract:
    pass
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an instance of Author")
        if not isinstance(book, Book):
            raise Exception("book must be an instance of Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an integer")
        
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
    
        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        "Returns a list of all Contract objects that have the matching date date."
        if not isinstance(date, str):
            raise Exception("date must be a string")
        return [contract for contract in cls.all if contract.date == date]
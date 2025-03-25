class book:
    def __init__(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price

    def apply_discount(self,percentage):
        
        discount = self.price * (percentage / 100)
        self.price -= discount
        return self.price
        
        
B1 = book("right girl","no one",500)
B2 = book("right boy","no one",200) 

print(B1.apply_discount(2))


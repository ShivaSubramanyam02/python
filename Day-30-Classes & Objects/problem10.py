class MovieTicket:
    def __init__(self, movie_name, price, seats_available):
        self.movie_name = movie_name
        self.price = price
        self.seats_available = seats_available
    
    def book_tickets(self,n):
        if n <= self.seats_available:
            self.seats_available -= n
            print(f"{n} ticket(s) successfully booked for {self.movie_name}.")
        else:
            print(f"Not enough seats available! Only {self.seats_available} seat(s) left.")
    def show_details(self):
        print(f"Movie: {self.movie_name}, Price: {self.price}, Seats Available: {self.seats_available}")

movie1 = MovieTicket("Avengers: Endgame", 250, 10)
movie2 = MovieTicket("Interstellar", 200, 5)

movie1.show_details()
movie1.book_tickets(3)
movie1.show_details()
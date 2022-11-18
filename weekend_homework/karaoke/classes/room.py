class Room:
    def __init__(self, room_number, guests, entry_price, capacity):
        self.guests = guests
        self.room_number = room_number
        self.entry_price = entry_price
        self.capacity = capacity
        self.songs = []

    def guest_buys_entry(self, entry, guest):
        self.guests += 1
        guest.reduce_cash(entry.entry_price)

    def guest_leaves(self, room):
        self.guests -= 1



        

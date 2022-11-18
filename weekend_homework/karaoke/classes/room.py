class Room:
    def __init__(self, room_number, guests, entry_price, capacity):
        self.guests = guests
        self.room_number = room_number
        self.entry_price = entry_price
        self.capacity = capacity
        self.songs = []

    def guest_buys_entry(self, room, guest):
        if room.guests - room.capacity:
            guest.reduce_cash(room.entry_price)
            self.guests += 1
        return self.too
    
 
    def guest_leaves(self):
        self.guests -= 1

    def song_amount(self):
        return len(self.songs)

    def add_song(self, song):
        self.songs.append(song)

    def too_many_people(self):
        return "Sorry there is no space"


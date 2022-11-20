import unittest
from classes.room import Room
from classes.song import Song
from classes.guest import Guest

class TestRoom(unittest.TestCase):
       def setUp(self):
        self.room_1 = Room(1, 12, 10, 20)
        self.room_2 = Room(2, 14, 10, 15)
        self.room_3 = Room(3, 20, 15, 20)
        self.song_1 = Song("Dreams", "Fleetwood Mac")
        self.song_2 = Song("Thriller", "Michael Jackson")
        self.song_3 = Song("Burning Love", "Elvis Presley")
        self.guest_1 = Guest("John", 200, "Brother")
        self.guest_3 = Guest("Sharon", 80, "Mr Brightside")
        self.guest_2 = Guest("Lucy", 50, "Thriller")

       def test_room_has_name(self):
              self.assertEqual(1, self.room_1.room_number)

       def test_room_has_capacity(self):
              self.assertEqual(15, self.room_2.capacity)

       def test_guest_buys_entry(self):
             self.room_1.guest_buys_entry(self.room_1, self.guest_1)
             self.assertEqual(190, self.guest_1.cash)
             self.assertEqual(13, self.room_1.guests)

       def test_guest_leaves(self):
              self.room_2.guest_leaves()
              self.assertEqual(13, self.room_2.guests)
       
       def test_add_song(self):
              self.room_3.add_song(self.song_1)
              self.assertEqual(1, self.room_3.song_amount())

       def test_not_enough_space(self):
            self.room_3.guest_buys_entry(self.room_3, self.guest_3)
            self.assertEqual("Sorry there is no space", self.room_3.too_many_people())


       def test_room_has_guests_fav_song(self):
        self.room_1.room_has_fav_song(self.guest_2, self.song_2)
        self.assertEqual(

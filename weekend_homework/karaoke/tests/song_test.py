import unittest
from classes.song import Song

class TestSong(unittest.TestCase):
    def setUp(self):
        self.song = Song("Thriller", "Michael Jackson")

    def test_song_has_name(self):
        self.assertEqual("Thriller", self.song.name)

    def test_song_has_artist(self):
        self.assertEqual("Michael Jackson", self.song.artist)

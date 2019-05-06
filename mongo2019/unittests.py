import unittest
from pymongo import MongoClient

from MongoDB import Film, Actor
client = MongoClient('localhost', 27017)
db = client.unittest_pymongo

class TestFilmMethods(unittest.TestCase):

    def test_get_nb_films(self):
        self.assertEqual(Film.get_nb_films(db), 450)

    def test_get_nb_actors(self):
        self.assertEqual(Actor.get_nb_actors(db), 18023)
        self.assertIsNotNone(Actor.get_nb_actors(db))
        o=Actor.get_nb_actors(db)
        self.assertIsInstance(o,int)

    def test_get_actors(self):

        film = Film('tt6674514')
        self.assertEqual(film.get_actors(db), [ " Kangaroo Dundee\n", " Terri Irwin\n", " Phil Wollen\n", " Tim Flannery\n", " Peter Singer\n" ])
        self.assertIsInstance(film.get_actors(db),list)

    def test_add_film(self):
        o=Actor('test')
        o.add_film('blabla')
        self.assertEqual(o.films[0],'blabla' )

    def test_actor_init(self):
        o=Actor('nico')
        o.add_film('spyderman')
        self.assertEqual(o.name,'nico')
        self.assertIsInstance(o,Actor)
        self.assertIsInstance(o.films,list)
        self.assertEqual(len(o.films), 1)

    def test_load_actor(self):
        client = MongoClient('localhost', 27017)
        db = client.unittest_pymongo
        self.assertEqual(db,client.unittest_pymongo)
        o = Actor('nicolas')
        o.add_film('wow')
        di={o.name:o.films}
        self.assertIsInstance(di,dict)
        self.assertIsNotNone(di)






if __name__ == '__main__':
    client = MongoClient('localhost', 27017)
    db = client.unittest_pymongo

    unittest.main()

    client.close()


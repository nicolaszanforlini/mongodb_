
from Scrapping import *
from pymongo import MongoClient
from MongoDB import Actor

client = MongoClient('localhost', 27017)
db = client.unittest_pymongo

def clean_actor(actor):
  actor_nettoye = actor.replace('\n','').replace('.','').strip()
  return actor_nettoye

def clean_title(title):
  title_nettoye = title.replace('\xa0','')
  return title_nettoye

dico_actor={}
for film in db.films.find():
    for actor in film.get('actors'):
      act=clean_actor(actor)
      if act not in dico_actor:
          dico_actor[act]=[]
      tit = film.get('title')
      titre = clean_title(tit)
      dico_actor[act].append(titre)

print(dico_actor)

for act,tit in dico_actor.items():
  o=Actor(act)
  for t in tit:
    o.add_film(t)
  o.load(db)

client.close()


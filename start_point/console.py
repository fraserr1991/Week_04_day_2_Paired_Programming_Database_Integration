# Use this file to test your repository functions 

import pdb
from models.album import Album
from models.artist import Artist

import repositories.artist_repository as artist_repository
import repositories.album_repository as album_repository

artist1 = Artist("Frightened Rabbit")
artist_repository.save(artist1)
print(artist1.__dict__)
artist2 = Artist("Eminem")
artist_repository.save(artist2)

artist_2 = artist_repository.select(1)
print(artist_2)

album_1 = album_repository.select(1)
print(album_1)

all_artists = artist_repository.select_all()

for artist in all_artists:
    print(artist.__dict__)

all_albums = album_repository.select_all()

for album in all_albums:
    print(album.__dict__)

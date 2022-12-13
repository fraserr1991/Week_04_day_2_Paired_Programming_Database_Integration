from db.run_sql import run_sql

from models.album import Album
from models.artist import Artist

def save(album):
    sql = "INSERT INTO albums (name, genre, artist) VALUES (%s, %s, %s) RETURNING *"
    values = [album.name, album.genre, album.artist]
    results = run_sql(sql, values)
    id = results[0]['id']
    album.id = id
    return album

def delete_all():
    sql = "DELETE FROM albums"
    run_sql(sql)

def get_albums_for_artist(artist):
    albums = []

    sql = "SELECT * FROM "

def select(id):
    sql = "SELECT * FROM albums WHERE id = %s"
    values = [id]
    results = run_sql(sql, values)
    return results

def select_all():
    albums = []

    sql = "SELECT * FROM albums"
    results = run_sql(sql)

    for row in results:
        album = Album(row['name'], row['genre'], row['artist'], row['id'])
        albums.append(album)
    return albums

# def save(artist):
#     sql = "INSERT INTO artists (name) VALUES (%s) RETURNING *"
#     values = [artist.name]
#     results = run_sql(sql, values)
#     id = results[0]['id']
#     artist.id = id
#     return artist
# Using the `console.py` file they would like to be able to:

# * Create and Save Artists
# * Create and Save Albums
# * Delete all Artists / Albums
# * Find Artists/Albums by their ID (`select`)
# * List All Artists/Albums (`select_all`)
import sqlite3
import datetime

CREATE_MOVIES_TABLE = """CREATE TABLE IF NOT EXISTS movies(
    title TEXT.
    release_timestamp REAL,
);"""
CREATE_WATCHED_TABLE = """CREATE TABLE IF NOT EXISTS watched(
    watcher TEXT.
    title TEXT,
);"""
INSERT_MOVIE = "INSERT INTO movie (title, release_timestamp, watched) VALUES (?, ?);"
DELETE_MOVIE = "DELETE FROM movies WHERE title = ?;"
SELECT_ALL_MOVIES = "SELECT * FROM movies;"
SELECT_WATCHED_MOVIES = "SELECT * FROM movies WHERE watched = ?;"
SET_MOVIE_WATCHED = "UPDATE movies SET watched = 'yes' WHERE title = ?;"
INSERT_WATCH_MOVIE = "SELECT * FROM watched WHERE watcher = ?;"

connected = sqlite3.connect("data.db")

def createTable():
    with connected:
        connected.execute(CREATE_MOVIES_TABLE)
        connected.execute(CREATE_WATCHED_TABLE)

def addMovie(title, release_timestamp):
    with connected:
        connected.execute(INSERT_MOVIE, (title, release_timestamp))

def userWatchedMovie(user, title):
    with connected:
        connected.execute(DELETE_MOVIE, (title,))
        connected.execute(INSERT_WATCH_MOVIE, (user, title))

def watchedMovie(title):
    with connected:
        connected.execute(SET_MOVIE_WATCHED, (title,))

def getMovies():
    with connected:
        cursor = connected.cursor()
        cursor.execute(SELECT_ALL_MOVIES)
        
        return cursor.fetchall()

def getWatched(user):
    with connected:
        cursor = connected.cursor()
        cursor.execute(SELECT_WATCHED_MOVIES, (user,))
        
        return cursor.fetchall()
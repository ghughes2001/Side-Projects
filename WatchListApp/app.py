import database
import datetime

menu = """Please select on of the following options:
- Type '1' to add movie
- Type '2' to view all movies
- Type '3' to view watched movie
- Type '5' to exit

YOUR SELECTION: """

print(menu)
database.createTable()

def addUserMovie():
    title = input("Movie Title: ")
    releaseDate = input("Release Date (DD-MM-YYYY): ")
    newDate = datetime.datetime.strptime(releaseDate, "%D-%M-%Y")
    timeStamp = newDate.timestamp()
    
    database.addMovie(title, timeStamp)

def printMovies(heading, movies):
    print(f"\t {heading}\t Movies ")
    
    for movie in movies:
        movieDate = datetime.datetime.fromtimestamp(movie[1])
        readableDate = movieDate.strftime("%d %b %Y")
        
        print(f"{movie[0]} (on {readableDate})")
        print("\t\n")

def printWatchedMovies(user, title):
    print(f"\t {user}'s watched movies\t")
    for movie in title:
        print(f"{movie[1]}")
    print("\t\n")

def userWatchedMovie():
    title = input("Enter the title of movie watched: ")
    database.watchedMovie(title)

def printWatchedMovie():
    user = input("Name: ")
    title = input("Movie: ")
    
    database.userWatchedMovie(user, title)

userInput = input(menu)
while (userInput := input(menu) != "5"):
    if (userInput == "1"):
        addUserMovie()
    elif (userInput == "2"):
        movieList = database.getMovies()
        printMovies("All",  movieList)
    elif (userInput == '3'):
        userWatchedMovie()
    elif (userInput == "4"):
        user = input("Name: ")
        watched = database.getWatched(user)
        printWatchedMovie(user, watched)
    else:
        print("Must be one of the inputs given")
import sqlite3
 
DB_FILENAME = 'songs.sqlite3.db'
SQL_SELECT_GENRES = 'SELECT name FROM genres'
SQL_INSERT_GENRE = "INSERT INTO genres(name) VALUES(?);"

def main_menu():
	print("Welcome to the music database!")
	print("\t1. Display all song information.")
	print("\t2. Add a new genere.")
	print("\t3. Add a new album.")
	print("\t4. Add a new artist.")
	print("\t5. Add a new song.")
	print("\t6. Exit.")
	choice = raw_input("Enter a choice: ")
	try:
		choice = int(choice)
		if (choice == 1): display_songs()
		elif (choice == 2): add_genre();
		elif (choice == 3): add_album();
		elif (choice == 4): add_artist();
		elif (choice == 5): add_song();
		elif(choice ==6): print("Goodbye.  Thanks for coming.")
		else: invalid_input()
	except ValueError:
		invalid_input()
	

def display_songs():
	#display and add songs
	print("the songs")
	main_menu()

def add_genre():
	#prints genres
	print("Genres in the database:")
	for row in cursor.execute(SQL_SELECT_GENRES):
		print("%s" % row)
	new_genre = str(raw_input("Enter new genre name or leave blank to exit to menu:"))
	#if something was entered, add it as a genre
	if (len(new_genre) != 0): cursor.execute(SQL_INSERT_GENRE,(new_genre,))
	main_menu()
	

def add_album():
	#show and add an albums
	print("the albums")
	main_menu()
	
def add_artist():
	#show and add an artists
	print("the artists")
	main_menu()

def add_song():
	#show and add a songs
	print("the songs")
	main_menu()
	
def invalid_input():
	print("Invalid input.  Please try again")
	main_menu()
	
	
#connects to the db
db_connection = sqlite3.connect(DB_FILENAME)
 
#creates a cursor, a pointer to a point in a collection of data
cursor = db_connection.cursor() 

main_menu()

#closes connection to the db
db_connection.close()
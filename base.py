import sqlite3
 
DB_FILENAME = 'songs.sqlite3.db'
SQL_SELECT_GENRES = 'SELECT name FROM genres'
SQL_INSERT_GENRE = 'INSERT INTO genres(name) VALUES(?);'
SQL_SELECT_ALBUMS = 'SELECT albums.name, artists.name FROM albums,artists WHERE artists.id  = albums.artist_id'
SQL_INSERT_ALBUM = 'INSERT INTO albums(name, artist_id) VALUES(?,?);'
SQL_SELECT_ARTISTS = 'SELECT id, name FROM artists'

def main_menu():
	print('Welcome to the music database!')
	print('\t1. Display all song information.')
	print('\t2. Add a new genere.')
	print('\t3. Add a new album.')
	print('\t4. Add a new artist.')
	print('\t5. Add a new song.')
	print('\t6. Exit.')
	choice = raw_input('Enter a choice: ')
	try:
		choice = int(choice)
		if (choice == 1): display_songs()
		elif (choice == 2): add_genre();
		elif (choice == 3): add_album();
		elif (choice == 4): add_artist();
		elif (choice == 5): add_song();
		elif(choice ==6): exit_program();
		else: invalid_input()
	except ValueError:
		invalid_input()
	

def display_songs():
	#display and add songs
	print('the songs')
	main_menu()

def add_genre():
	#prints genres
	print('Genres in the database:')
	for row in cursor.execute(SQL_SELECT_GENRES):
		print('%s' % row)
	new_genre = str(raw_input('Enter new genre name or leave blank to exit to menu:'))
	#if something was entered, add it as a genre
	if (len(new_genre) != 0): cursor.execute(SQL_INSERT_GENRE,(new_genre,))
	main_menu()
	

def add_album():
	#prints albums
	print('Albums in the database:')
	for row in cursor.execute(SQL_SELECT_ALBUMS):
		print('Album: %s. Artist: %s' % (row[0], row[1]))
	new_album = str(raw_input('Enter new album name or leave blank to exit to menu: '))
	if (len(new_album) != 0):
		for row in cursor.execute(SQL_SELECT_ARTISTS):
			print('%d. %s' %(int(row[0]), row[1]))
		artist = str(raw_input('Enter the number of the artist for this album or leave blank to exit to menu: '))
		#add error checking for invalid artist
		if(len(artist) != 0): cursor.execute(SQL_INSERT_ALBUM,(new_album, artist,));
	main_menu()
	
def add_artist():
	#show and add an artists
	print('the artists')
	main_menu()

def add_song():
	#show and add a songs
	print('the songs')
	main_menu()
	
def invalid_input():
	print('Invalid input.  Please try again')
	main_menu()
	
def exit_program():
	choice = raw_input('Would you like to save changes to the database? (y/n):')
	if (choice.lower() == 'y'):
		db_connection.commit()
		print('Changes saved.\nGoodbye.  Thanks for coming.')
	elif (choice.lower() == 'n'):
		print('Changes not saved.\nGoodbye.  Thanks for coming.')
	else:
		print('Invalid input.  Please try again')
		exit_program()
	
	
#connects to the db
db_connection = sqlite3.connect(DB_FILENAME)
 
#creates a cursor, a pointer to a point in a collection of data
cursor = db_connection.cursor() 

main_menu()

#closes connection to the db
db_connection.close()
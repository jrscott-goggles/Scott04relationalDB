import sqlite3
 
DB_FILENAME = 'songs.sqlite3.db'
SQL_SELECT_GENRES = 'SELECT id, name FROM genres'
SQL_INSERT_GENRE = 'INSERT INTO genres(name) VALUES(?);'
SQL_SELECT_ALBUMS = 'SELECT albums.id, albums.name, artists.name FROM albums,artists WHERE artists.id  = albums.artist_id'
SQL_INSERT_ALBUM = 'INSERT INTO albums(name, artist_id) VALUES(?,?);'
SQL_SELECT_ARTISTS = 'SELECT id, name FROM artists'
SQL_INSERT_ARTIST = 'INSERT INTO artists(name) VALUES(?)'

stay = True

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

def add_genre():
	#prints genres
	print('Genres in the database:')
	for row in cursor.execute(SQL_SELECT_GENRES):
		print('%d. %s' % (int(row[0]), row[1]))
	new_genre = str(raw_input('Enter new genre name or leave blank to exit to menu:'))
	#if something was entered, add it as a genre
	if (len(new_genre) != 0): cursor.execute(SQL_INSERT_GENRE,(new_genre,))

def add_album():
	#prints albums
	print('Albums in the database:')
	for row in cursor.execute(SQL_SELECT_ALBUMS):
		print('%d. Album: %s. Artist: %s' % (int(row[0]), row[1], row[2]))
	new_album = str(raw_input('Enter new album name or leave blank to exit to menu: '))
	if (len(new_album) != 0):
		artist_id_list = []
		for row in cursor.execute(SQL_SELECT_ARTISTS):
			print('%d. %s' %(int(row[0]), row[1]))
			artist_id_list.append(int(row[0]))
		
		artist_id = raw_input('Enter the number of the artist for this album or leave blank to exit to menu: ')
		try:
			artist_id = int(artist_id)
			if(artist_id in artist_id_list): cursor.execute(SQL_INSERT_ALBUM,(new_album, artist_id,))
			else: invalid_input()
		except ValueError:
			invalid_input()

def add_artist():
	for row in cursor.execute(SQL_SELECT_ARTISTS):
		print('%d. %s' %(int(row[0]), row[1]))
	new_artist = str(raw_input('Enter new artist name or leave blank to exit to menu: '))
	if (len(new_artist) != 0): cursor.execute(SQL_INSERT_ARTIST, (new_artist,))

def add_song():
	#Add a songs
	print('Add a new song!')
	
def invalid_input():
	print('Invalid input.  Please try again')
	
def exit_program():
	global stay
	choice = raw_input('Would you like to save changes to the database? (y/n):')
	if (choice.lower() == 'y'):
		db_connection.commit()
		print('Changes saved.\nGoodbye.  Thanks for coming!')
		stay = False
	elif (choice.lower() == 'n'):
		print('Changes not saved.\nGoodbye.  Thanks for coming!')
		stay = False
	else:
		invalid_input()
		exit_program()

#connects to the db
db_connection = sqlite3.connect(DB_FILENAME)
 
#creates a cursor, a pointer to a point in a collection of data
cursor = db_connection.cursor() 

while stay:
	main_menu()

#closes connection to the db
db_connection.close()
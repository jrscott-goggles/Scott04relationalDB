#Justin Scott
#Project 4: Relational Database Management
#Consle interface for displaying and adding data to a SQLite song database

import sqlite3
 
DB_FILENAME = 'songs.sqlite3.db'
SQL_SELECT_GENRES = 'SELECT id, name FROM genres'
SQL_INSERT_GENRE = 'INSERT INTO genres(name) VALUES(?);'
SQL_SELECT_ALBUMS = 'SELECT albums.id, albums.name, artists.name FROM albums,artists WHERE artists.id  = albums.artist_id'
SQL_INSERT_ALBUM = 'INSERT INTO albums(name, artist_id) VALUES(?,?);'
SQL_SELECT_ARTISTS = 'SELECT id, name FROM artists'
SQL_INSERT_ARTIST = 'INSERT INTO artists(name) VALUES(?)'
SQL_SELECT_SONGS = 'SELECT songs.name, genres.name, artists.name, albums.name FROM songs, genres, artists, albums WHERE genres.id = songs.genre_id AND artists.id = albums.artist_id AND albums.id = songs.album_id'
SQL_INSERT_SONG = 'INSERT INTO songs(name, genre_id, album_id) VALUES(?,?,?);'

stay = True

def main_menu():
	print('------------------------------\nWelcome to the music database!')
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
	#align these
	print('------------------------------\nLook at all this nice music:')
	print("Song-Genre-Artist-Album")
	for row in cursor.execute(SQL_SELECT_SONGS):
		print('%s\t%s\t%s\t%s\t' %(row[0], row[1], row[2], row[3]))

def add_genre():
	#prints genres
	print('------------------------------\nGenres in the database:')
	for row in cursor.execute(SQL_SELECT_GENRES):
		print('%d. %s' % (int(row[0]), row[1]))
	new_genre = str(raw_input('Enter new genre name or leave blank to exit to menu:'))
	#if something was entered, add it as a genre
	if (len(new_genre) != 0): cursor.execute(SQL_INSERT_GENRE,(new_genre,))

def add_album():
	#prints albums
	#align these
	print('------------------------------\nAlbums in the database:')
	for row in cursor.execute(SQL_SELECT_ALBUMS):
		print('%d. %s by %s' % (int(row[0]), row[1], row[2]))
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
			if(len(str(artist_id)) != 0): invalid_input()

def add_artist():
	print("------------------------------\nArtists in the database:")
	for row in cursor.execute(SQL_SELECT_ARTISTS):
		print('%d. %s' %(int(row[0]), row[1]))
	new_artist = str(raw_input('Enter new artist name or leave blank to exit to menu: '))
	if (len(new_artist) != 0): cursor.execute(SQL_INSERT_ARTIST, (new_artist,))

def add_song():
	#Add a songs
	print('------------------------------\nAdd a new song!')
	new_song = str(raw_input('Enter new song name or leave blank to exit to menu: '))
	if (len(new_song) != 0):
		genre_id_list = []
		print("Genres:")
		for row in cursor.execute(SQL_SELECT_GENRES):
			print('%d. %s' % (int(row[0]), row[1]))
			genre_id_list.append(int(row[0]))
		genre_id = raw_input('Enter genre number or leave blank to exit to menu: ')
		try:
			genre_id = int(genre_id)
			if(genre_id in genre_id_list):
				#keep going with album then insert it
				album_id_list = []
				print("Albums:")
				for row in cursor.execute(SQL_SELECT_ALBUMS):
					print('%d. %s' % (int(row[0]), row[1]))
					album_id_list.append(int(row[0]))
				album_id = raw_input('Enter album number or leave blank to exit to menu: ')
				try:
					album_id = int(album_id)
					if(album_id in album_id_list): cursor.execute(SQL_INSERT_SONG, (new_song, genre_id, album_id,))
					else: invalid_input()
				except ValueError:
					if(len(str(album_id)) != 0): invalid_input()
			else: invalid_input()
		except ValueError:
			if(len(str(genre_id)) != 0): invalid_input()

def invalid_input():
	print('Invalid input.  Please try again.')
	
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
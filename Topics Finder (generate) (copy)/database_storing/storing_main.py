# from pymongo import MongoClient
from Description import descript
from Data import formatter
from Contents import TOC
from pprint import pprint
import sys , os , sqlite3

def main():
	DATABASE_DIR = str(os.path.abspath(os.getcwd()))
	# builds the sqlite3 database

	conn = sqlite3.connect(DATABASE_DIR + '/database')
	cursor = conn.cursor()

	# print 'Creating database, stored at the top-level'
	# cursor.execute('''create table if not exists description_temp (id integer, isbn , title , author , dept_course , descript_raw );''')


	book_list = cursor.execute('''select * from book_info;''').fetchall()
	# temp_book_list = cursor.execute('''select * from description_temp''').fetchall()

	# if it is already populated, don't bother with it
	if not book_list:
		print 'Database created, proceeding to populate it, this will take some time'
		formatter.format_file('Data/spreadsheet.csv')
		book_list = cursor.execute('''select * from book_info;''').fetchall()

	else:
		print 'Database previously created, proceeding to updata values'

	print 'Database populated with basic information'
	print 'Filling the database with descriptions and table of contents'

	conn.commit()
	#if(books.count() == 0):
	#	print "Updating the datastore "
	#	formatter.format_file('Data/spreadsheet.csv')
	#	print "Datastore successfully updated with " + str(books.count()) + " entries"
		
	#else:
	#	print "File is already formatted, finding descriptions for " + str(books.count()) + " books"
	current_number = 1
	print 'Doing Description first'

	for book in book_list:
		sys.stdout.flush()
		isbn = book[1]
		sys.stdout.write(str(current_number) + "/" + str(len(book_list))+"\r")
		sys.stdout.flush()			
		#already_done = False
		
		#for temp_book in temp_book_list:
		#	if temp_book[1] == isbn:
		#		already_done = True
		#		break

		#if not already_done:
		
		if current_number == 10:
			break
			
		summary , url = descript.get_descript(isbn)

		if(summary == "" or summary is None):
			cursor.execute('''update book_info 
			set descript_raw = ?, descript_url = ? 
			where isbn = ?;'''  , ('Description Not Found' , url , isbn))
			current_number += 1
			
			continue
					
		cursor.execute('''update book_info 
			set descript_raw = ?, descript_url = ? 
			where isbn = ?;'''  , (summary, url , isbn))
		conn.commit()

		current_number += 1
		
	
	conn.commit()	
	current_number = 1
	
	print 'Description completed'
	print 'Proceeding to do the table of contents'

	for book in book_list:
		sys.stdout.flush()
		isbn = book[1]
		sys.stdout.write(str(current_number) + "/" + str(len(book_list))+"\r")
		sys.stdout.flush()			
		#already_done = False
		
		#for temp_book in temp_book_list:
		#	if temp_book[1] == isbn:
		#		already_done = True
		#		break

		#if not already_done:
		
		if current_number == 10:
			break
			
		summary , url = TOC.get_toc(isbn)

		if(summary == "" or summary is None):
			cursor.execute('''update book_info 
			set toc_raw = ?, toc_url = ? 
			where isbn = ?;'''  , ('Table Not Found' , url , isbn))
			current_number += 1
			
			continue
					
		cursor.execute('''update book_info 
			set toc_raw = ?, toc_url = ? 
			where isbn = ?;'''  , (summary, url , isbn))
		conn.commit()

		current_number += 1
		
	
		
	conn.close()

if __name__ == "__main__":
	main()


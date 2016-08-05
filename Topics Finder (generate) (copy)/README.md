Hi!

This project was created by Ameer Takieddin (Summer 2016)

The dependencies are:
	Sqlite3
	Mallet (version 20080618)
	Django (version 1.9.7)
	BeautifulSoup (version 4.2.1)

How this package works:

	One inital download, folder structure should be:
			|--Topics Finder (Where the main.py file is stored)
				|--database_storing (Where the information is stored)
					|--Contents
					|--Data (Put CSV file here)
					|--Description
				|--topics (Where the topic modeling happens)
					|--Mallet
				|--website (Django folder) (Alot of folders...)
				|--lib

	To get started:
		1) Insert your CSV file spreadsheet into this path:
				Topics Finder/database-storing/Data
			Make sure to save it has "spreadsheet.csv"
			Need to have a least three columns:
				"Author		Title	ISBN	Dept/Course"
			!!! WARNING !!! Changes need to be made if not in this exact format

		2) Once that is inserted, run:
			python main.py
			in the root directory

		3) Running this should give you prompts, answer them and wait for the model to finish

		4) Navigate to 127.0.0.1:8000 to see the information in website format

		5) Done!

	Re-running the program
		If the program ran once already, it will detect this and prompt you to see if you would like to work off of old data already provided and just run the model with different parameters, or if you would like to reset the whole thing

		!!! WARNING !!! The website can only display one model at a time, and reseting the website deletes the other model's information. If you would like to save the model's data, choose to save it in the prompts or rename the file

# ApostleCorp
Proof of concept for the development of multiple bots on the Instagram platform. 

## Instagrapi and TextBlob is mandatory for this program
https://github.com/subzeroid/instagrapi/tree/master
https://textblob.readthedocs.io/en/dev/
Install using:
```
pip install instagrapi
pip install textblob
```

## Installation
Unfortunately, all bots need to be created manually and inserted into a text file.
1) Clone the repository using
```
git clone https://github.com/cynicalmrjones/ApostleCorp
```
2) Create a file named InstagrapiLogins.txt 
	* Format the file using the gmail account followed by password
	ex.
		
		
   		>****@gmail.com passwd
		>
  		>******@gmail.com passwd2
		>
		>*******@gmail.com passwd3
3) Add comment prompts to and pictures to associated folders
    * Comment prompts are formatted as sperate lines for each statement

        > "This is a line of text.
        > "This is another line of text.

    * Pictues work best in JPEG format

4) Execute by running the python compiler on helios.py
	```
	python3 helios.py
	```
## Functionality
1) Like media using a select bot
2) Comment on media using a select bot
3) Post media using a select bot
4) Like media using a range of bots in text file
5) Comment on media using a range of bots in text file
6) Sort comments generated through ChatGPT

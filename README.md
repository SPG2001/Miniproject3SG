# Miniproject3SG

## Description
This is a basic Flask website that is used to store the data of enemies, which is manually entered in. In order to
do so, the user must regitser using a name and password before they are allowed to enter in any data.
The data fields are the enemy name, health, resistance, and rank.

In order to run, download the zip file and extract it to your desired directory.
Once you are done with that, go into your command line and change the directory to
where you extracted the files. Once you are there, run this command:

```
pip install -e
```

After that, run this command to enable the database:

```
flask --app flaskwiz init-db
```

And lastly, to engage the website:

```
flask --app flaskwiz run
```

Once you are done with this, direct your browser to 127.0.0.1:5000, and you will be
at the index.html page.

In my final project, what I would have done was replace the display for the posts with graphs showing the data.
This data would have been sent to the SQLite database. From there, my graphs would be created.

Lastly, instead of enemy data being stored in posts, they would have been directly stored in an SQLite database, which
would give the information to the bot. How it would have given the corect information would be with a picture of the
enemy's health portrait, which gives the name and health. Once the server finds the match, it sends back the resistances
an enemy has, which would assist the bot's calculations. Once the battle is over, the bot would send the drop data back 
to the SQLite database, which would add the data. It knows which drop table to send the data thanks to the enemy
confirmation.
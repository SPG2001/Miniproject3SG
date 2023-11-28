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
# CodenamesGame
Website for playing the Codenames spy game.

Once you clone the code to your local machine, you need to create a PostgreSQL database with an arbitrary name. Then add a local\_settings.py module as a sibling to the settings.py module, if it doesn't already exist. The local\_setings.py is imported by settings.py, and it overrides the DATABASES dictionary with the appropriate settings to connect to the PostgreSQL database you created above.

Here is a sample for local\_settings.py:

	DATABASES = {
    	'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '<database_name>',
        'USER': '<your_username>',
        'PASSWORD': '<your_password>',
        'HOST': 'localhost',
        'PORT': '',
    			}
	}

In the Django project folder run migrations on the project to build and initialize the database tables. The 

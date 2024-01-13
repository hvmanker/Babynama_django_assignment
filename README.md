# FavoriteTunes

FavoriteTunes is a Django application that allows users to add and display their favorite songs and the artists who perform them.

## Setting up the project

### Prerequisites

Make sure you have the following installed on your machine:

- Python (version 3.x)
- Django (version 4.2.3)

### Clone the repository


### Create a virtual environment (optional but recommended)

python -m venv venv
### Activate the virtual environment

On Windows:
venv\Scripts\activate

On macOS/Linux:
source venv/bin/activate

### Install dependencies

pip install django

### Run migrations
python manage.py migrate

### Create a superuser account (for accessing the admin site)

python manage.py createsuperuser
Follow the prompts to create a superuser account.

### Running the project

python manage.py runserver
Visit http://127.0.0.1:8000/ in your browser to access the application.

### Paths
Accessing the admin site
Visit http://127.0.0.1:8000/admin/ and log in with the superuser account created earlier.

Adding songs and artists
Navigate to http://127.0.0.1:8000/add_song/ to add a new song.
Navigate to http://127.0.0.1:8000/add_artist/ to add a new artist.


Viewing the song list and artist list
Song List: http://127.0.0.1:8000/songs/
Artist List And Song count : http://127.0.0.1:8000/artists/

Feel free to explore and enjoy FavoriteTunes!

# Pur Beurre

Pur beurre is the 8th Open Classroom's project. The goal is to make a website from wireframes able to do research between similar product to get highers nutriscore. The project must be available on the website heroku. The url of mine is https://titouan-oc-p8.herokuapp.com

## Instalation

First, you have to install the libraries required using the command :
```
pip install
```

Now you have to create a postgreSQL database and change the settings.py file.
You also have to run the migrations with :
```
py manage.py makemigrations
py manage.py migrate
```

Then, you can launch the project using :
```
py manage.py runserver
```

End voila ! The local server is launched end you can access it by django's provided url.

For more information, please consult the [django documentation](https://docs.djangoproject.com/en/4.0/).

## Usage

Create an admin :
```
py manage.py createsuperuser
```

Fill the database with the chosen category with chosen number of pages :
```
py manage.py filldatabase cakes 10
```


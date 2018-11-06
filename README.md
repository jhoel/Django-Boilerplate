# Django-Boilerplate

This is a boilerplate used for Django development purposes.
What comes with a boilerplate for your django projects?

# Features

- A django debug toolbar
- Settings modules configured for development/production ready
- Keeps Keys and other sensitive information hidden in production

# Dependencies

[Django Debug Toolbar](https://django-debug-toolbar.readthedocs.io/en/latest/)

[Python De-Couple](https://github.com/henriquebastos/python-decouple)

# Instructions

- Clone Repo
  git clone `git@github.com:teaglebuilt/Django-Boilerplate.git`

- cd into Django-Boilerplate

- Create virtual environment
  `virtualenv {name of env}`

- Activate virtual environment
  `source {name of env}/bin/activate`

- Install requirements for boilerplate
  `pip install -r requirements.txt`

- Create folder "static_in_env" at the same level as manage.py

- Run python manage.py runserver

## Note

You will see the debug server on the right side. There will be no page found. You can connect the URLS and views to configure as usual.

Hope this helps.

![alt text](https://s3.amazonaws.com/clarityfm-production/attachments/6605/default/django.png?1442839704 "Django Boilerplate")

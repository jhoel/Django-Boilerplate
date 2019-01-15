# Django-Boilerplate

This is a boilerplate used for Django development purposes.
What comes with a boilerplate for your django projects?

# Features

- A django debug toolbar
- Settings modules configured for development/production ready
- A list of commands for project configuration
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

## Commands

```

python manage.py rename { project name }

```

Note: If run this command more than once. You will need to change this file core/management/commands/rename.py. FIll in "{ current-project-name }" with the current project name.

```py

def handle(self, *args, **kwargs):
        new_project_name = kwargs['new_project_name']

        files_to_rename = ['{ current-project-name }/settings/base.py',
                           '{ current-project-name }/wsgi.py', 'manage.py']
        folder_to_rename = '{ current-project-name }'

        for f in files_to_rename:
            with open(f, 'r') as file:
                filedata = file.read()

            filedata = filedata.replace('{ current-project-name }', new_project_name)

```

## Note

You will see the debug server on the right side. There will be no page found. You can connect the URLS and views to configure as usual.

Hope this helps.

![alt text](https://s3.amazonaws.com/clarityfm-production/attachments/6605/default/django.png?1442839704 "Django Boilerplate")
# django_chat
# django_chat

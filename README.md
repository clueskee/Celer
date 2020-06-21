# Celer Helpdesk

**This project was created for demonstration purposes.**

A web-based helpdesk application. Using django-admin with django-jet as a part for employees and a modern bootstrap4 based frontend for clients. Still at an early stage probably not suitable for implementation but you can be forked for experiments.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. 

### Prerequisites

* Django==2.2
* django-bootstrap-modal-forms==1.5.0
* django-crispy-forms==1.9.1
* django-filebrowser-no-grappelli==3.8.0
* django-jet==1.0.8
* django-tinymce4-lite==1.8.0
* django-widget-tweaks==1.4.8

### Installing

1) Clone this repository
2) `wirtualenv -p python3 venv`
3) `source venv/bin/activete`
4) `pip install requiremnts.txt`
5) `python manage.py makemigrations`
6) `python manage.py migrate`
7) `python manage.py runserver`
8) Go to `127.0.0.1\celer` and have fun!

## Built With

* [Django](https://github.com/django/django) -  The Web framework for perfectionists with deadlines. 
* [Django Jet](https://github.com/geex-arts/django-jet) - Modern template for Django admin interface with improved functionality. 
* [django-crispy-forms](https://github.com/django-crispy-forms/django-crispy-forms) - The best way to have Django DRY forms. 

## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE](LICENSE) file for details
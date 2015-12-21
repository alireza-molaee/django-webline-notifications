Django Simple Notifications
===========================
![screen shot](screen_shot.png)
this is a django application to avoid user about events. you can notify everything to user or users you want too easy. 
###Feature
 * chose icon for notification
 * chose yor notification status or color
 * notification can be link
 * sent notification to list of user
 
##How to install
###Downloading the package
Probably the best way to install is by using PIP:
```
$ pip install django_simple_notifications
```
If you want to stay on the bleeding edge of the app:
```
$ git clone https://github.com/alireza-molaee/django_simple_notifications.git
$ cd django_simple_notifications
$ python setup.py install
```
###install on django
now you can add django-simple-notifications to the settings.py file:
```
INSTALLED_APPS = (
    ...
    'simple-notifications',
)
```
Then run migrations:
```
$ python manage.py migrate simple-notifications
```
Then collectstatic:
```
$ python manage.py collectstatic
```
now if run server you can see notifications in django admin:
```
$ python manage.py runserver
```
##TODO
- [x] add test for models
- [x] add font-awesome to admin
- [x] add template tags to use any template
- [x] add view to change see status
- [ ] add view to delete notifications wich seen more than one day 
- [ ] add test for view 
- [ ] add defult settings
 - [ ] font file
 - [ ] defult notification count to show
 - [ ] max of notification can be archived
- [x] handle all event by ajax

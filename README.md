Django Simple Notifications
===========================
![screen shot](http://i.imgur.com/TxoZeaG.png)

This is a django application to notify user about events.
You can simply inform user about all kind of updates.

###Features
 * Chose notification status and color
 * Thumbnail for notification
 * Notification has a URL, can passed in other notifications
 * Send group (to list of users) notification
 
##How to install
###Downloading the package
Probably the best way to install is by using PIP:
```
$ pip install git+https://github.com/alireza-molaee/django_simple_notifications.git#egg=django_simple_notifications
```
If you want to clone the main repository:
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
- [ ] add view to delete notifications which seen more than one day 
- [ ] add test for view 
- [ ] add default settings
 - [ ] font file
 - [ ] default notification count to show
 - [ ] max of notification can be archived
- [x] handle all event by AJAX

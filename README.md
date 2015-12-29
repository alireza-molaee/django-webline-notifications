Django webline Notifications
===========================
###Screen shot
![screen shot](http://i.imgur.com/TxoZeaG.png)

###What is Django webline Notifications
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
$ pip install django-webline-notifications
```
If you want to clone the main repository:

```
$ git clone https://github.com/alireza-molaee/django-webline-notifications.git
$ cd django-webline-notifications
$ python setup.py install
```
###install on django
now you can add django-simple-notifications to the settings.py file:

```
INSTALLED_APPS = (
    ...
    'webline_notifications',
    'django.contrib.admin',
)
```
Then run migrations:

```
$ python manage.py migrate webline-notifications
```
Then collectstatic:

```
$ python manage.py collectstatic
```
now if run server you can see notifications in django admin:

```
$ python manage.py runserver
```
##Settings
you can limit archive notification for all user by `WEBLINE_NOTIFICATIONS_LIMIT` default is `False` it mean (no limit)
for example `myproject.settings.py`:

```
...  
WEBLINE_NOTIFICATIONS_LIMIT = 50  
...
```

##Usage
to notify every thing you want:

 1. import Notification
 2. use Notification.send to send notification

```
from webline_notification.model import Notification

Notification.send(
	...
)
```
#####send option:

 1. list of user:  
	list of user object that you want to receive this notification `[obj, obj, ...]`
 2. content:   
	a small text about event `'some one join us'`
 3. icon:  
	icon css class `'fa-info'`
 4. color:  
	color hex id `'#c3c3c3'`
 5. link:  
	you notification can have a url to where reason of event `'http://www.google.com/'` *(optional)*
 	
you can use default color in Notification `Notification.COLOR_DANGER`
you can filter notification by color in django admin if you use default color

#####defult colors:  

* <span style="color:#f39c12;">COLOR_WARNING</span>
* <span style="color:#f56954;">COLOR_DANGER</span>
* <span style="color:#00c0ef;">COLOR_INFO</span>
* <span style="color:#00a65a;">COLOR_SUCCESS</span>
* <span style="color:#3c8dbc;">COLOR_PRIMARY</span>
* <span style="color:#d2d6de;">COLOR_GRAY</span>
* <span style="color:#111111;">COLOR_BLACK</span>

#####example:

```
from webline_notifications.models import Notification
from django.contrib.auth.models import User

user = User.objects.get(pk=1)

Notification.send(
            [user],
            'foo',
            'fa-info',
            Notification.COLOR_DANGER,
            url='http://www.google.com/'
            )
```


 	
##TODO
- [x] add test for models
- [x] add template tags to use any template
- [x] add view to change see status
- [x] add test for view 
- [ ] add default settings
 - [ ] font files
 - [x] default notification count to show
 - [x] max of notification can be archived
- [x] handle events by AJAX

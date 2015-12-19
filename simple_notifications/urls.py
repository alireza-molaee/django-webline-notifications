from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^see-all/$',
        views.see_all_notification, name='see_all_notification'),
]
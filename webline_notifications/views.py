from django.contrib.auth.decorators import login_required
from models import Notification
from django.http import HttpResponse, HttpResponseForbidden


@login_required
def see_all_notification(request):
    if request.is_ajax():
        Notification.seen_all(request.user)
        return HttpResponse()
    else:
        return HttpResponseForbidden('<h1>Forbidden</h1>you cant use this url in this way')
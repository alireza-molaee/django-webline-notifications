from django.contrib.auth.decorators import login_required
from models import Notification
from django.http import HttpResponse


@login_required
def see_all_notification(request):
    user = request.user
    Notification.seen_all(user)
    html = ("<h2>see notifications</h2><br>cheek seen for %s" % user.get_full_name)
    return HttpResponse(html)

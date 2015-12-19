from django.template import Library
from simple_notifications.models import Notification
from django.template.defaultfilters import stringfilter

register = Library()


@register.inclusion_tag('notification/nav_link.html')
def notifications_link(user, limit=None):
    all_count = Notification.objects.count()
    not_seen_count = Notification.objects.not_seen(user).count()
    if limit is None:
        notifications = Notification.objects.filter(
            user=user
        )
    else:
        notifications = Notification.objects.filter(
            user=user
        )[:limit]
    notifications_list = []
    for n in notifications:
        notifications_dic = {
            'icon': n.icon,
            'color': n.color,
            'content': n.content,
            'send_date': n.send_date,
            'seen_date': n.seen_date,
            'url': n.url}
        notifications_list.append(notifications_dic)
    return {'notifications': notifications_list, 'all_count': all_count,
            'not_seen_count': not_seen_count}


@register.filter(name='icon_type')
@stringfilter
def icon_type(value):
    return value.split('-')[0]
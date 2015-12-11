from django.contrib import admin
from models import Notification


class NotificationAdmin(admin.ModelAdmin):
    raw_id_fields = ["user"]
    list_filter = ["color", "send_date"]
    list_display = ["user", "get_icon_html", "seen_date", "send_date",
                    "get_link"]
    search_fields = ["user"]
    
admin.site.register(Notification, NotificationAdmin) #TODO: add it to setting

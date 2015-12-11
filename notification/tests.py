from django.test import TestCase
from models import Notification
from django.contrib.auth.models import User


class NotificationsTestCase(TestCase):
    fixtures = ['users.json']
    
    @classmethod
    def setUpTestData(cls):
        admin = User.objects.get(pk=1)
        students = User.objects.filter(groups__name='student')
        arc = User.objects.get_by_natural_key('arc')
        cls.n2_admin = Notification.send(
            [admin],
            'test notification to admin',
            'fa-error',
            Notification.COLOR_DANGER,
            url='http://www.google.com/'
            )
        cls.n2_arc = Notification.send(
            [arc],
            'test notifications to arc',
            'fa-alert',
            Notification.COLOR_DANGER,
        )
        cls.n2_students = Notification.send(
            students,
            'test notifications to students',
            'fa-alert',
            Notification.COLOR_WARNING,
            ''
        )
        
    def test_icon_str(self):
        icon_str = self.n2_admin[0].icon
        self.assertEqual(
            icon_str,
            'fa-error')

    def test_icon_html(self):
        icon_html = self.n2_admin[0].get_icon_html()
        self.assertEqual(
            icon_html,
            '<i class="fa fa-error" style="color:#f56954;"></i>'
        )
    
    def test_get_link(self):
        link = self.n2_admin[0].get_link()
        self.assertEqual(
            link,
            '<a href="http://www.google.com/"><i class="fa fa-link"></i>Link</a>'
        )
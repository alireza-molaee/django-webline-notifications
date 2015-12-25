from django.test import TestCase
from models import Notification
from django.contrib.auth.models import User


class NotificationsTestCase(TestCase):
    fixtures = ['users.json']
    
    @classmethod
    def setUpTestData(cls):
        admin = User.objects.get(pk=1)
        group_foo = User.objects.filter(groups__name='group_foo')
        staff = User.objects.get_by_natural_key('staff')
        cls.admin_user = admin
        cls.n2_admin = Notification.send(
            [admin],
            'test notification to admin',
            'fa-info',
            Notification.COLOR_DANGER,
            url='http://www.google.com/'
            )
        cls.n2_staff = Notification.send(
            [staff],
            'test notifications to staff',
            'fa-bell',
            Notification.COLOR_DANGER,
        )
        cls.n2_group_foo = Notification.send(
            group_foo,
            'test notifications to client',
            'fa-bell',
            Notification.COLOR_WARNING,
            ''
        )
        
    def test_icon_str(self):
        icon_str1 = self.n2_admin[0].icon
        icon_str2 = self.n2_staff[0].icon
        icon_str3 = self.n2_group_foo[0].icon
        self.assertEqual(
            icon_str1,
            'fa-info'
        )

        self.assertEqual(
            icon_str2,
            'fa-bell'
        )

        self.assertEqual(
            icon_str3,
            'fa-bell'
        )

    def test_icon_html(self):
        icon_html1 = self.n2_admin[0].get_icon_html()
        icon_html2 = self.n2_staff[0].get_icon_html()
        icon_html3 = self.n2_group_foo[0].get_icon_html()
        self.assertEqual(
            icon_html1,
            '<i class="fa fa-info" style="color:#f56954;width:100%;text-align:center;"></i>'
        )

        self.assertEqual(
            icon_html2,
            '<i class="fa fa-bell" style="color:#f56954;width:100%;text-align:center;"></i>'
        )

        self.assertEqual(
            icon_html3,
            '<i class="fa fa-bell" style="color:#f39c12;width:100%;text-align:center;"></i>'
        )
    
    def test_get_link(self):
        link1 = self.n2_admin[0].get_link()
        link2 = self.n2_staff[0].get_link()
        link3 = self.n2_group_foo[0].get_link()
        self.assertEqual(
            link1,
            '<a href="http://www.google.com/"><i class="fa fa-link"></i>&nbspLink</a>'
        )
        self.assertEqual(
            link2,
            None
        )
        self.assertEqual(
            link3,
            None
        )
        
    def test_seen(self):
        seen_befor = self.n2_admin[0].seen
        self.assertEqual(
            seen_befor,
            False
        )
        
        Notification.seen_all(self.admin_user)
        seen_after = Notification.objects.get(pk=self.n2_admin[0].pk).seen
        self.assertEqual(
            seen_after,
            True
        )
        
    def test_limit_notification(self):
        Notification.objects.get(pk=self.n2_admin[0].pk).delete()
        for i in range(8):
            Notification.send(
                [self.admin_user],
                'test {}'.format(i),
                'fa-info',
                Notification.COLOR_DANGER,
                url='http://www.google.com/'
            )
        with self.settings(SIMPLE_NOTIFICATIONS_LIMIT=5):
            Notification.objects.filter(
                user=self.admin_user
            )[0].limit_notification()
            all_n_after = Notification.objects.filter(user=self.admin_user)
            count = all_n_after.count()
            first_content = all_n_after.order_by('send_date')[0].content
            last_content = all_n_after.order_by('-send_date')[0].content
            self.assertEqual(
                count,
                5
            )
            self.assertEqual(
                first_content,
                'test 3'
            )
            self.assertEqual(
                last_content,
                'test 7'
            )
        with self.settings(SIMPLE_NOTIFICATIONS_LIMIT=False):
            Notification.objects.filter(
                user=self.admin_user
            )[0].limit_notification()
            all_n_after = Notification.objects.filter(user=self.admin_user)
            count = all_n_after.count()
            self.assertEqual(
                count,
                5
            )
            
    def test_see_view(self):
        self.assertEqual(
            self.client.get('/en-us/notifications/see-all/').status_code,
            302
        )
        self.client.login(username='admin', password='123')
        self.assertEqual(
            self.client.get('/en-us/notifications/see-all/').status_code,
            403
        )
        self.assertEqual(
            self.client.get('/en-us/notifications/see-all/', HTTP_X_REQUESTED_WITH='XMLHttpRequest').status_code,
            200
        )
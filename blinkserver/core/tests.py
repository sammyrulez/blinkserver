from blinkserver.core.models import BlinkStatus ,Hook
from blinkserver import settings
from django.test import TestCase
from datetime import timedelta ,datetime


class MockBlinkManager(object):
    def play(self):
        pass
    def set_pattern(self,pattern):
        pass
    def stop(self):
        pass


settings.BLINK_MANAGER = MockBlinkManager()

class HookViewTest(TestCase):

    fixtures = ['users', 'hooks']

    def test_public_hook(self):

        response = self.client.get('/hook/publichook/')
        self.assertEqual(200, response.status_code)


    def test_private_hook(self):
        response = self.client.get('/hook/privatehook/')
        self.assertEqual(401, response.status_code)
        self.client.login(username='defuser', password='defuser')
        response = self.client.get('/privatehook/privatehook/')
        self.assertEqual(401, response.status_code)
        self.client.logout()
        self.client.login(username='admin', password='admin')
        response = self.client.get('/privatehook/privatehook/')
        self.assertEqual(200, response.status_code)

    def test_shutdown(self):
        response = self.client.get('/admin/stop_blink/')
        self.assertEqual(302, response.status_code)
        self.client.login(username='admin', password='admin')
        response = self.client.get('/admin/stop_blink/',follow=True)
        self.assertEqual(200, response.status_code)
        response = self.client.get('/admin/stop_blink/')
        self.assertEqual(302, response.status_code)



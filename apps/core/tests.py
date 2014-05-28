from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

# TODO: Use django urls.py instead of static urls in these tests


def create_user():
    user = User.objects.create_user('test123', 'user@localhost', 'test123')
    return user


class CoreViewsTestCase(TestCase):
    def test_get_index(self):
        resp = self.client.get(reverse('index'))
        self.assertEqual(resp.status_code, 200)

    def test_get_login(self):
        resp = self.client.get(reverse('auth_login'))
        self.assertEqual(resp.status_code, 200)

    def test_post_login_wrong(self):
        create_user()
        resp = self.client.post(
            reverse('auth_login'),
            data={
                'username': 'idontexist',
                'password': 'meneither'})
        self.assertContains(
            resp,
            'Please enter a correct username and password',
            status_code=200,)

    def test_post_login_good(self):
        create_user()
        resp = self.client.post(
            reverse('auth_login'),
            data={
                'username': 'test123',
                'password': 'test123'})
        self.assertEqual(resp.status_code, 302)

    def test_get_about(self):
        resp = self.client.get(reverse('about'))
        self.assertEqual(resp.status_code, 200)

    def test_get_secret_no_login(self):
        resp = self.client.get(reverse('secret'))
        self.assertEqual(resp.status_code, 302)

    def test_get_secret_login(self):
        create_user()
        self.client.login(username='test123', password='test123')
        resp = self.client.get(reverse('secret'))
        self.assertEqual(resp.status_code, 200)

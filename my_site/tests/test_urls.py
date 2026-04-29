from django.test import SimpleTestCase
from django.urls import reverse, resolve

class TestUrls(SimpleTestCase):
    def test_main_index_url(self):
        url = reverse('main:index')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_posts_filter_url(self):
        url = reverse('posts:filter')
        self.assertEqual(resolve(url).func.__name__, 'filter')

    def test_posts_create_url(self):
        url = reverse('posts:create')
        self.assertEqual(resolve(url).func.__name__, 'create')

    def test_music_index_url(self):
        url = reverse('music:index')
        self.assertEqual(resolve(url).func.__name__, 'index')

    def test_users_login_url(self):
        url = reverse('users:login')
        self.assertEqual(resolve(url).func.__name__, 'login_user')

    def test_users_register_url(self):
        url = reverse('users:register')
        self.assertEqual(resolve(url).func.__name__, 'registration')

    def test_profile_main_url(self):
        url = reverse('profile:main')
        self.assertEqual(resolve(url).func.__name__, 'profile')

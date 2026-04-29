from django.test import TestCase
from django.contrib.auth import get_user_model
from posts.models import Post

User = get_user_model()

class PostModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create_user(username='testuser', password='password')
        cls.post = Post.objects.create(
            title='Test Title',
            text='Test Text',
            author=cls.user
        )

    def test_post_creation(self):
        self.assertTrue(isinstance(self.post, Post))
        self.assertEqual(self.post.__str__(), self.post.title)

    def test_post_fields(self):
        self.assertEqual(self.post.title, 'Test Title')
        self.assertEqual(self.post.text, 'Test Text')
        self.assertEqual(self.post.author, self.user)

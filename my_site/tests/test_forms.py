from django.test import TestCase
from users.forms import LoginUserForm, RegisterUserForm
from profil.forms import ProfileUserForm
from django.contrib.auth import get_user_model

User = get_user_model()

class TestForms(TestCase):
    def test_login_form_valid(self):
        form = LoginUserForm(data={'username': 'testuser', 'password': 'password'})
        self.assertTrue(form.is_valid())

    def test_login_form_invalid(self):
        form = LoginUserForm(data={'username': '', 'password': ''})
        self.assertFalse(form.is_valid())

    def test_register_form_valid(self):
        form = RegisterUserForm(data={
            'username': 'newuser',
            'email': 'new@example.com',
            'first_name': 'First',
            'last_name': 'Last',
            'password1': '7yef7huIH',
            'password2': '7yef7huIH'
        })
        self.assertTrue(form.is_valid())

    def test_register_form_invalid_email(self):
        User.objects.create_user(username='existing', email='test@example.com', password='password')
        form = RegisterUserForm(data={
            'username': 'newuser',
            'email': 'test@example.com',
            'first_name': 'First',
            'last_name': 'Last',
            'password1': 'password123',
            'password2': 'password123'
        })
        self.assertFalse(form.is_valid())
        self.assertIn('email', form.errors)

    def test_profile_form_readonly_fields(self):
        user = User.objects.create_user(username='testuser', email='test@example.com')
        form = ProfileUserForm(instance=user)
        self.assertEqual(form.fields['username'].widget.attrs.get('readonly'), 'readonly')
        self.assertEqual(form.fields['email'].widget.attrs.get('readonly'), 'readonly')


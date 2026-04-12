from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserChangeForm, PasswordChangeForm

User = get_user_model()


class ProfileUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        if 'username' in self.fields:
            self.fields['username'].widget.attrs.update({
                'readonly': 'readonly',
                'class': 'readonly-field'
            })

        if 'email' in self.fields:
            self.fields['email'].widget.attrs.update(
                {
                    'readonly': 'readonly',
                    'class': 'readonly'
                }
            )


class ResetUserForm(PasswordChangeForm):
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
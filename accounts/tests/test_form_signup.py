from django.test import TestCase
from accounts.forms import SingUpForm


class SingUpFormTest(TestCase):
    def test_form_has_fields(self):
        form = SingUpForm()
        expected = ['username', 'email', 'password1', 'password2',]
        actual = list(form.fields)
        self.assertSequenceEqual(expected, actual)

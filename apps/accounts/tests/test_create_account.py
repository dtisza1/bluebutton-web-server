from django.test import TestCase
from django.test.client import Client
from django.contrib.auth.models import Group
from django.core.urlresolvers import reverse
from apps.accounts.models import Invitation

class CreateAccountTestCase(TestCase):
    """Test Account Creation"""

    def setUp(self):
        Invitation.objects.create(code="1234", email="fred@example.com")
        Group.objects.create(name="BlueButton")
        self.client = Client()
        self.url = reverse('accounts_create')
        
    def test_valid_account_create(self):
        """Create an Account Valid"""
        form_data = {"invitation_code": "1234",
                     "email": "fred@example.com",
                     "username":"fred",
                     "password1":"bedrocks",
                     "password2":"bedrocks",
                     "first_name": "Fred",
                     "last_name": "Flinstone"
                     }
        response = self.client.post(self.url, form_data, follow=True)
        #print(response.content)
        
        
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Please check your email to verify your account.")


    def test_account_create_shold_fail_when_password_too_short(self):
        """Create account should fail if password is too short"""
        form_data = {"invitation_code": "1234",
                     "username":"fred",
                     "password1":"p",
                     "password2":"p",
                     "first_name": "Fred",
                     "last_name": "Flinstone"
                     }
        response = self.client.post(self.url, form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "too short")

    def test_account_create_shold_fail_when_password_too_common(self):
        """Create account should fail if password is too common"""
        form_data = {"invitation_code": "1234",
                     "username":"fred",
                     "password1":"password",
                     "password2":"password",
                     "first_name": "Fred",
                     "last_name": "Flinstone"
                     }
        response = self.client.post(self.url, form_data, follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "too common")
   
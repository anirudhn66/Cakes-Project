from unittest.mock import patch

from django.test import SimpleTestCase
from rest_framework.test import APIRequestFactory

from .views import RegisterView


class RegisterViewTests(SimpleTestCase):

    def test_invalid_email_is_rejected_before_sending_mail(self):
        request = APIRequestFactory().post(
            '/register/',
            {
                'username': 'lebronejames202657mailinator.com',
                'first_name': 'Lebrone James',
                'role': 'User',
                'password': 'lebronejames',
            },
            format='json',
        )

        with patch('authentication.views.send_mail') as send_mail:
            response = RegisterView.as_view()(request)

        self.assertEqual(response.status_code, 400)
        self.assertIn('username', response.data)
        send_mail.assert_not_called()

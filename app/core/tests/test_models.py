from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTest(TestCase):
    def test_successful_creation_of_user_with_email(self):
        email = "test@example.com"
        password = "P@$$w0rd!"
        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        smaple_emails = [
            ['test1@EXAMPLE.com', 'test1@example.com'],
            ['Test2@Example.com', 'Test2@example.com'],
            ['TEST3@EXAMPLE.COM', 'TEST3@example.com'],
            ['test4@example.COM', 'test4@example.com']
        ]
        for email, expected_email in smaple_emails:
            user = get_user_model().objects.create_user(
                email=email, password='123456'
            )
            self.assertEqual(user.email, expected_email)

    def test_new_user_without_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user('', 'Passw0rd')

    def test_create_super_user(self):
        user = get_user_model().objects.create_superuser(
            'superUserEmail@example.com',
            'pass1word!'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
        
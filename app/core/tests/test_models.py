from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTestCase(TestCase):

    def test_create_user_with_email_successful(self):
        """ Test creating a new user with email is successful"""
        email = 'ashish@versatil.com'
        password = 'password123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_user_email_is_normalized(self):
        """ Test whether the email part is all lowercase when saved in db"""
        email = 'ashish@VERSATIL.COM'
        password = 'PASSWORD123'
        user = get_user_model().objects.create_user(
            email=email,
            password=password)
        self.assertEqual(user.email, email.lower())

    def test_if_email_provided(self):
        """ Test whether an email is provided"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_if_superuser_created(self):
        """ Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'ashish@versatil.com',
            'pass123'
        )
        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

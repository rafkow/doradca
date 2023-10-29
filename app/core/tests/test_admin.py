"""
Test of extend user model
"""
from django.test import TestCase, SimpleTestCase
from django.contrib.auth import get_user_model


class SampleTest(SimpleTestCase):
    """Test user model"""

    def test_create_user_model(self):
        self.assertFalse(False)
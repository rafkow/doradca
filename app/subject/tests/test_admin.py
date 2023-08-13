from django.test import SimpleTestCase


class SampleTest(SimpleTestCase):
    """Test the test"""

    def test_testing(self):
        self.assertFalse(False)
from django.test import TestCase
from django.db import IntegrityError
from subject.models.address import Address


class AddressTest(TestCase):
    """Test the test"""

    def test_create_address(self):
        """Test of creating address,"""
        address = Address(street="Toruńska", house_number="45")

        address.save()

        saved_address = Address.objects.get(pk=address.pk)

        self.assertEqual(address.street, saved_address.street)

    def test_duplicate_address_raise_integrity_error(self):
        address = Address(street="Toruńska", house_number="45")

        address.save()

        duplicate_address = Address(street="Toruńska", house_number="45")

        with self.assertRaises(IntegrityError):
            duplicate_address.save()

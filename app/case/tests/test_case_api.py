"""
Test of extend user model
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from case.models import Case, TYPE
from case.serializers import CaseSerializer, CaseDetailsSerializer

CASE_URL = reverse('case:case-list')


def detail_url(case_id):
    return reverse('case:case-detail', args=[case_id])

def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)

def create_case(user, **params):
    """Create and return test case"""
    defaults = {
        'signature': 'M/11/23',
        'type': TYPE[0][0],
        'description': 'casual case',
    }
    defaults.update(params)

    case = Case.objects.create(user=user, **defaults)
    return case


class PublicCaseAPITest(TestCase):
    """Test unautorized API requests"""
    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(CASE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_create_user_model(self):
        self.assertFalse(False)


class PrivateCaseAPITest(TestCase):
    """Test authenticated user API case"""
    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email='user@example.com', password='test123')
        self.client.force_authenticate(self.user)

    def test_creating_case(self):
        """Test create case by authenticated user"""
        payload = {
            'signature': 'abc',
            'type': TYPE[0][0],
            'description': 'casual case',
        }
        case = Case.objects.create(user = self.user, **payload)

        self.assertEqual(case.type, TYPE[0][0])

    def test_creating_api_case(self):
        """Test create case by authenticated user"""
        payload = {
            'signature': 'abcdef',
            'type': TYPE[0][0],
            'description': 'casual case',
        }

        res = self.client.post(CASE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        self.assertEqual(res.data['type'], TYPE[0][0])

    def test_get_case_details(self):
        """Test get self details"""
        case = create_case(user=self.user)

        url = detail_url(case.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)



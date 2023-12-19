"""
Test of extend user model
"""
from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model

from rest_framework.test import APIClient
from rest_framework import status

from case.models import Case, TYPE
from case.serializers import CaseSerializer


CASE_URL = reverse("case:case-list")


def detail_url(case_id):
    return reverse("case:case-detail", args=[case_id])


def create_user(**params):
    """Create and return a new user."""
    return get_user_model().objects.create_user(**params)


def create_case(user, **params):
    """Create and return test case"""
    defaults = {
        "signature": "M/11/23",
        "type": TYPE[0][0],
        "description": "casual case",
    }
    defaults.update(params)

    case = Case.objects.create(user=user, **defaults)
    return case


class PublicCaseAPITest(TestCase):
    """Test unauthorized API requests"""

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        """Test auth is required to call API."""
        res = self.client.get(CASE_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateCaseAPITest(TestCase):
    """Test authenticated user API case"""

    def setUp(self):
        self.client = APIClient()
        self.user = create_user(email="user@example.com", password="test123")
        self.client.force_authenticate(self.user)

    def test_receiving_cases(self):
        create_case(user=self.user)

        res = self.client.get(CASE_URL)
        cases = Case.objects.all().order_by("id")
        serializer = CaseSerializer(cases, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_creating_case(self):
        """Test create case by authenticated user"""
        payload = {
            "signature": "abc",
            "type": TYPE[0][0],
            "description": "casual case",
        }
        case = Case.objects.create(user=self.user, **payload)

        self.assertEqual(case.type, TYPE[0][0])

    def test_creating_api_case(self):
        """Test create case by authenticated user"""
        payload = {
            "signature": "abcdef",
            "type": TYPE[0][0],
            "description": "casual case",
        }

        res = self.client.post(CASE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        self.assertEqual(res.data["type"], TYPE[0][0])

    def test_get_case_details(self):
        """Test get self details"""
        case = create_case(user=self.user)

        url = detail_url(case.id)
        res = self.client.get(url)

        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_get_case_limited_to_user(self):
        """Test getting cases is limited to authenticated user"""
        other_user = create_user(email="other@example.com", password="test123")
        create_case(user=self.user)
        payload = {"signature": "M/12/23"}
        create_case(user=other_user, **payload)

        res = self.client.get(CASE_URL)

        cases = Case.objects.filter(user=self.user)
        serializer = CaseSerializer(cases, many=True)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_create_case(self):
        """Test create case"""
        payload = {
            "signature": "A/1/1",
            "type": TYPE[0][0],
            "description": "casual case",
        }

        res = self.client.post(CASE_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        case = Case.objects.get(id=res.data["id"])
        for k, v in payload.items():
            self.assertEqual(getattr(case, k), v)
        self.assertEqual(case.user, self.user)

    def test_partial_case(self):
        """Test partial update of a case."""
        case = create_case(
            user=self.user,
            signature="Q/1/2",
            type=TYPE[0][0],
            description="sample case",
        )

        payload = {"description": "new case desc"}
        url = detail_url(case.id)
        res = self.client.patch(url, payload)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        case.refresh_from_db()
        self.assertEqual(case.description, payload["description"])
        self.assertEqual(case.signature, "Q/1/2")
        self.assertEqual(case.user, self.user)

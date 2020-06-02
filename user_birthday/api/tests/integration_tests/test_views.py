from django.urls import reverse
from rest_framework.test import APITestCase, APIClient
from rest_framework.views import status
from api.models import User
from api.serializers import UserSerializer
from django.db.models import Q


class BaseViewTest(APITestCase):
    client = APIClient()

    @staticmethod
    def create_user(**kwargs):
        serializer = UserSerializer(
            data=kwargs
        )
        if serializer.is_valid(True):
            serializer.save()

    def setUp(self):
        # add test data
        self.create_user(first_name="Alexander",
                         last_name="Kurilov",
                         email="akurilov92@gmail.com",
                         birthday="18.12.1992")
        self.create_user(first_name="Troy",
                         last_name="Barnes",
                         email="troy.barnes@gmail.com",
                         birthday="04.12.1989")
        self.create_user(first_name="Shirley",
                         last_name="Bennet",
                         email="shirley.bennet@greendale.com",
                         birthday="12.08.1971")
        self.create_user(first_name="Bob",
                         last_name="Smith",
                         email="annie.smith@gmail.com",
                         birthday="02.03.1994")


class GetAllUsersTest(BaseViewTest):

    def test_get_all_users(self):
        response = self.client.get(
            reverse("users-from-to"),
            {
                'from_dt': '1108',
                'to_dt': '1912'
            }
        )
        expected = [
            User(first_name="Alexander",
                 last_name="Kurilov",
                 email="akurilov92@gmail.com",
                 birthday="18.12.1992"),
            User(first_name="Shirley",
                 last_name="Bennet",
                 email="shirley.bennet@greendale.com",
                 birthday="12.08.1971")
        ]
        serialized = UserSerializer(expected, many=True)
        self.assertEqual(response.data, serialized.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class GetAverageAgeTest(BaseViewTest):

    def test_average_age(self):
        response = self.client.get(
            reverse("users-average-age")
        )
        expected = {'avg': 32.75}
        response_data = response.data[0]
        self.assertEquals(response_data, expected)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class CreateUsersViewTest(BaseViewTest):
    def test_insert_single_user(self):
        test_data = {
                "first_name": "Test",
                "last_name": "User",
                "email": "test.user@gmail.com",
                "birthday": "01.02.1982"
            }
        response = self.client.post(
            reverse("users-insert-bulk"),
            test_data,
            'json'
        )
        actual_user = UserSerializer(User.objects.get(email="test.user@gmail.com")).data
        expected_user = UserSerializer(test_data).data
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(actual_user, expected_user)

    def test_insert_multiple_users(self):
        test_data = [
            {
                "first_name": "Test",
                "last_name": "User1",
                "email": "test.user1@gmail.com",
                "birthday": "01.02.1981"
            },
            {
                "first_name": "Test2",
                "last_name": "User2",
                "email": "test.user2@gmail.com",
                "birthday": "01.02.1982"
            },
        ]
        response = self.client.post(
            reverse("users-insert-bulk"),
            test_data,
            'json'
        )
        actual_user = UserSerializer(
            User.objects.filter(Q(email="test.user1@gmail.com") | Q(email="test.user2@gmail.com")), many=True
        ).data
        expected_user = UserSerializer(test_data, many=True).data
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
        self.assertEquals(actual_user, expected_user)

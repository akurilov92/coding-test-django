from django.test import SimpleTestCase
from user_birthday.serializers import UserSerializer
from user_birthday.models import User


class TestSerializer(SimpleTestCase):

    def test_user_serializer(self):
        expected_serialized_data = {
            "first_name": "Alexander",
            "last_name": "Kurilov",
            "email": "akurilov92@gmail.com",
            "birthday": "18.12.1992"
        }
        self.assertEquals(UserSerializer(User(first_name="Alexander",
                                              last_name="Kurilov",
                                              email="akurilov92@gmail.com",
                                              birthday="18.12.1992")).data,
                          expected_serialized_data)

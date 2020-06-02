from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework.views import status


class LetterCasePermutationViewTest(APITestCase):
    def test_letter_case_permutation_view(self):
        response = self.client.get(
            reverse("letter-permutation"),
            {'input_string': 'a2b'}
        )
        expected = ['a2b', 'a2B', 'A2B', 'A2b']
        response_data = response.data
        self.assertEquals(set(response_data), set(expected))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

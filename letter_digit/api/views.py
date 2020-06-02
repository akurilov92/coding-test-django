from rest_framework.response import Response
from rest_framework.exceptions import ParseError
from rest_framework import views
from . import letter_case_permutation


class LetterCasePermutationView(views.APIView):
    def get(self, request):
        input_string = self.request.query_params.get('input_string')
        if input_string is None:
            raise ParseError('missing required parameter: input_string')
        return Response(letter_case_permutation.letter_case_permutation(input_string))

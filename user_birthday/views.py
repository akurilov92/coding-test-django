from rest_framework import generics, status
from .models import User
from .serializers import UserSerializer
from rest_framework.response import Response
from .query_param_validation import parse_birthday_filter
from rest_framework.exceptions import ParseError
from rest_framework import views
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from letter_digit.letter_case_permutation import letter_case_permutation


class CreateUsersView(generics.CreateAPIView):
    model = User
    serializer_class = UserSerializer

    def create(self, request, *args, **kwargs):
        is_many = isinstance(request.data, list)
        serializer = self.get_serializer(data=request.data, many=is_many)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class ListUsersView(generics.ListAPIView):
    serializer_class = UserSerializer

    def get_queryset(self):
        from_dt_str, to_dt_str = self.request.query_params.get('from_dt'), self.request.query_params.get('to_dt')
        if from_dt_str is None:
            raise ParseError('missing required parameter: from_dt')
        if to_dt_str is None:
            raise ParseError('missing required parameter: to_dt')
        from_dt, to_dt = parse_birthday_filter(from_dt_str), parse_birthday_filter(to_dt_str)
        queryset = User.objects.filter(birthday__day__gte=from_dt.day,
                                       birthday__month__gte=from_dt.month,
                                       birthday__day__lte=to_dt.day,
                                       birthday__month__lte=to_dt.month)
        return queryset


class AverageAgeView(views.APIView):
    @method_decorator(cache_page(60))
    def get(self, request):
        avg_age = User.objects.extra({'avg': 'AVG(extract (year from AGE(birthday)))'}).values('avg')
        return Response(avg_age)

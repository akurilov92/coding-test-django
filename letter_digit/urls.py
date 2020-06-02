from django.urls import path

from . import views

urlpatterns = [
    path('letter_digit', views.LetterCasePermutationView.as_view(), name='letter-permutation')
]

from django.urls import path

from . import views

urlpatterns = [
    path('', views.LetterCasePermutationView.as_view(), name='letter-permutation')
]

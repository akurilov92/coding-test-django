from django.urls import path

from . import views

urlpatterns = [
    path('letter-permutation', views.LetterCasePermutationView.as_view(), name='letter-permutation')
]

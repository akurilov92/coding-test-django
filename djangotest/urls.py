from django.urls import path

from . import views

urlpatterns = [
    path('users-from-to', views.ListUsersView.as_view(), name='users-from-to'),
    path('users-insert-bulk', views.CreateUsersView.as_view(), name='users-insert-bulk'),
    path('users-average-age', views.AverageAgeView.as_view(), name='users-average-age'),
    path('letter-permutation', views.LetterCasePermutationView.as_view(), name='letter-permutation')
]

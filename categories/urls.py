from django.urls import path
from .api import CategoriesApi, CategoryApi,CategoryCreateAPI

app_name = "articles"
# app_name will help us do a reverse look-up latter.
urlpatterns = [
    path('categories/', CategoriesApi.as_view()),
    path('categories/<int:pk>', CategoryApi.as_view()),
    path('categories/create', CategoryCreateAPI.as_view()),
    ]

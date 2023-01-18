from django.urls import path, include

from .views import LatestProductList

urlpatterns = [
    path('product/', LatestProductList.as_view()),
]
from django.contrib import admin
from django.urls import path

from ads.views import StartView, AdsDataView, AdsView, AdsEntityView
from categories.views import CategoriesDataView, CategoriesView, CategoriesEntityView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', StartView.as_view()),

    path('ad/', AdsView.as_view()),
    path('ad/data/', AdsDataView.as_view()),
    path('ad/<int:pk>/', AdsEntityView.as_view()),

    path('cat/', CategoriesView.as_view()),
    path('cat/data/', CategoriesDataView.as_view()),
    path('cat/<int:pk>/', CategoriesEntityView.as_view()),
]

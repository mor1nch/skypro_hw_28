from django.urls import path

from categories import views

urlpatterns = [
    path('', views.CategoryListView.as_view()),
    path('<int:pk>/', views.CategoriesDetailView.as_view()),
    path('create/', views.CategoryCreateView.as_view()),
    path('<int:pk>/update/', views.CategoryUpdateView.as_view()),
    path('<int:pk>/delete/', views.CategoryDeleteView.as_view()),
]
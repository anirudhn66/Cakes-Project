from django.urls import path
from .import views

urlpatterns = [
    path('cakes/', views.CakeCreateListCreateView.as_view()),
    path('cakes/<int:id>/', views.CakeRetrieveUpdateDestroyView.as_view()),
    path('categories/', views.CategoryCreateListCreateView.as_view()),
    path('categories/<int:id>/', views.CategoryRetrieveUpdateDestroyView.as_view()),
    path('shape/', views.ShapeCreateListCreateView.as_view()),
    path('shape/<int:id>/', views.ShapeRetrieveUpdateDestroyView.as_view()),
    path('weight/', views.WeightCreateListCreateView.as_view()),
    path('weight/<int:id>/', views.WeightRetrieveUpdateDestroyView.as_view()),
]

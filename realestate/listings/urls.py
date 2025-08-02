from django.urls import path
from . import views

urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property-list'),
    path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property-detail'),
    path('property/new/', views.PropertyCreateView.as_view(), name='property-create'),
    path('property/<int:pk>/update/', views.PropertyUpdateView.as_view(), name='property-update'),
    path('property/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property-delete'),
]

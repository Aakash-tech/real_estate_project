from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('', views.PropertyListView.as_view(), name='property-list'),
    path('property/<int:pk>/', views.PropertyDetailView.as_view(), name='property-detail'),
    path('property/new/', views.PropertyCreateView.as_view(), name='property-create'),
    path('property/<int:pk>/update/', views.PropertyUpdateView.as_view(), name='property-update'),
    path('property/<int:pk>/delete/', views.PropertyDeleteView.as_view(), name='property-delete'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='listings/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='listings/logout.html'), name='logout'),
]

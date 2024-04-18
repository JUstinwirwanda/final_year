from django.urls import path
from . import views
from .views import dashboard

urlpatterns = [
    path('', views.home, name='home'), 
    path('about/', views.about, name='about'),
    path('contact/', views.contact, name='contact'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('profile/', views.profile, name='profile'),
    path('profile/settings/submit/', views.profile_settings_submit, name='profile_settings_submit'),
    path('contact/submit/', views.contact_form_submit, name='contact_form_submit'), 
    path('terms-of-service/', views.terms_of_service, name='terms_of_service'),
    path('privacy-policy/', views.privacy_policy, name='privacy_policy'),
    path('search/', views.search_results, name='search_results'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('ideas/', views.idea_list, name='idea_list'),  
    path('post-awareness/', views.post_awareness, name='post_awareness'),
    path('post-others/', views.post_others, name='post_others'),
    path('post-reporting/', views.post_reporting, name='post_reporting'),
    path('post-emergency/', views.post_emergency, name='post_emergency'),
    path('post-recommendations/', views.post_recommendations, name='post_recommendations'),  # Add this line
    path('post-innovation/', views.post_innovation, name='post_innovation'),  # Add this line
    path('post-suggestions/', views.post_suggestions, name='post_suggestions'),  # Add this line
    path('post-complain/', views.post_complain, name='post_complain'),  # Add this line
    path('ideas/<int:pk>/', views.idea_detail, name='idea_detail'),  # URL pattern for retrieving a single idea
    # Add more URL patterns as needed for your app's functionalities
]

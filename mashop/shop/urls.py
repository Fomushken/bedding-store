from django.urls import path
from . import views


urlpatterns = [
    path('', views.AerienHome.as_view(), name='home'),
    path('about/', views.AerienAbout.as_view(), name='about'),
    path('catalog/', views.AerienCatalog.as_view(), name='catalog'),
    path('reviews/', views.AerienReviews.as_view(), name='reviews'),
    path('contacts/', views.AerienContacts.as_view(), name='contacts'),
]
